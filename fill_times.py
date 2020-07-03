#!/usr/bin/env python3.8


import re
from sys import argv
import json
from typing import Dict, List, Match, Pattern

from paper import Paper, PaperEncoder

if __name__ == "__main__":
    papers_source: str = argv[1]
    timing_source: str = argv[2]
    dest: str = argv[3]

    raw_papers: Dict[str, Dict]
    with open(papers_source, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    with open(timing_source, 'r') as f:
        template_content: str = f.read()

    # block_re: Pattern = re.compile("^#+ (.*)\n+((\n)|(\\[.*)|({{[OSP][0-9]+}}))")
    block_re: Pattern = re.compile("#+ (.*)\n+(?:Session.*\n+)?(?:\n|(?:\\[.*\n)|(?:{{[OSP][0-9]+}}\n))+")
    blocks: List[Match] = list(block_re.finditer(template_content))

    id_re: Pattern = re.compile("{{[OSP]([0-9]+)}}")
    for b in blocks:
        print()
        print(b[1])

        formated_time: str = " - ".join(b[1].split('*')[:2])

        id_matches: List[Match] = list(id_re.finditer(b[0]))
        ids: List[int] = [int(e[1]) for e in id_matches]
        print(ids)

        for id_ in ids:
            papers[id_].schedule.append(formated_time)

    print(papers[1].schedule)
    with open(dest, 'w') as sink:
        json.dump({p.id: p for p in papers.values()}, sink, cls=PaperEncoder, indent=4, sort_keys=True)
