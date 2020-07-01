#!/usr/bin/env python3.8

import json
from sys import argv
from subprocess import check_output, CalledProcessError
from pathlib import Path
from typing import Dict

from paper import Paper


CREATE_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
 -H "X-User-Id: {USERID}" \\
 -H "Content-type: application/json" \\
 http://localhost:3000/api/v1/channels.create \\
 -d '{{ "name": "{title}" }}' '''

GETID_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
     -H "X-User-Id: {USERID}" \\
     http://localhost:3000/api/v1/channels.info?roomName={title} '''

TOPIC_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
     -H "X-User-Id: {USERID}" \\
     -H "Content-type: application/json" \\
     http://localhost:3000/api/v1/channels.setTopic \\
     -d '{{ "roomId": "{id_}", "topic": "{topic}" }}' '''

DESC_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
     -H "X-User-Id: {USERID}" \\
     -H "Content-type: application/json" \\
     http://localhost:3000/api/v1/channels.setDescription \\
     -d '{{ "roomId": "{id_}", "description": "{desc}" }}' '''

EXIST_TOPIC_ERROR = 'The channel topic is the same as what it would be changed to.'
EXIST_DESC_ERROR = 'The channel description is the same as what it would be changed to.'

DESC_LEN: int = 52


if __name__ == "__main__":
    assert len(argv) == 4

    papers_path: Path = Path(argv[1])
    assert papers_path.exists()

    TOKEN: str = argv[2]
    USERID: str = argv[3]

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    for paper in papers.values():
        print(f">>> Creating room for paper {paper.conf_id}")
        try:
            # Pay attention: I do not lower case the name, but the channel url will be lowercased
            create_json = json.loads(check_output(CREATE_TEMPLATE.format(TOKEN=TOKEN,
                                                                         USERID=USERID,
                                                                         title=paper.conf_id),
                                                  shell=True))
        except CalledProcessError as e:
            print(e.output)
            print(e.args)
            exit(-1)

        print(f"\t{create_json}")
        _id: str
        if create_json["success"]:
            _id = create_json['channel']["_id"]
        elif not create_json["success"] and create_json['errorType'] == 'error-duplicate-channel-name':
            getid_json = json.loads(check_output(GETID_TEMPLATE.format(TOKEN=TOKEN,
                                                                       USERID=USERID,
                                                                       title=paper.conf_id.casefold()),
                                                 shell=True))
            print(f"\t{getid_json}")
            _id = getid_json['channel']["_id"]
        else:
            exit(-1)

        topic_json = json.loads(check_output(TOPIC_TEMPLATE.format(TOKEN=TOKEN,
                                                                   USERID=USERID,
                                                                   id_=_id,
                                                                   topic=paper.title),
                                             shell=True))
        if not topic_json["success"] and topic_json['error'] != EXIST_TOPIC_ERROR:
            print(f"\t{topic_json}")
            exit(-1)

        authors: str = f"Authors: {', '.join(paper.authors)}"
        filler: str = ' ' * (len(authors) % DESC_LEN)
        sched: str = '\\n'.join(paper.schedule)
        # desc: str = f"Authors: {', '.join(paper.authors)}\\\n\\\nAbstract: {paper.sanitized_abstract}\\\n\\\nSchedule: {sched}"
        desc: str = f"{authors}"
        # print(desc)
        filled_desc_template = DESC_TEMPLATE.format(TOKEN=TOKEN,
                                                    USERID=USERID,
                                                    id_=_id,
                                                    desc=desc)
        print(filled_desc_template)
        desc_output = check_output(filled_desc_template,
                                   shell=True)
        print(desc_output)
        desc_json = json.loads(desc_output)

        if not desc_json["success"] and desc_json["error"] != EXIST_DESC_ERROR:
            print(f"\t{desc_json}")
            exit(-1)

        # exit(-1)
