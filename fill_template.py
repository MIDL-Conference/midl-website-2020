#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Dict, List, Match, Pattern
from operator import attrgetter

from paper import Paper


# class Paper():
#     def __init__(self, id: str, title: str, authors: str, url: str, or_id: str, oral: str, short: str,
#                  abstract: str):
#         self.id: int = int(id)
#         self.title: str = title
#         self.authors: List[str] = authors.split(', ')
#         self.url: str = url
#         self.or_id: str = or_id
#         self.oral: bool = oral == "True"
#         self.short: bool = short == "True"
#         self.poster: bool = (not self.short) and (not self.oral)
#         self.abstract: str = abstract

#         assert not (self.oral and self.short)
#         if self.short:
#             assert not self.oral

#         self.conf_sign: str = "O" if self.oral else ("S" if self.short else "P")

#         self.conf_id: str = f"{self.conf_sign}{self.id:03d}"

#         # self.__class__.__name__: str = "Paper"

#     def __str__(self) -> str:
#         sanitized_abstract: str = self.abstract.replace("'", "\\'")
#         sanitized_abstract = sanitized_abstract.replace('"', '\\"')
#         sanitized_abstract = sanitized_abstract.replace('\n', '')
#         sanitized_abstract = sanitized_abstract.replace('`', '')
#         sanitized_abstract = repr(sanitized_abstract)
#         # sanitized_abstract: str = repr(self.abstract)

#         return f'''{{{{ paper(\'{self.title}\',
#         \'{f'{", ".join(self.authors)}'}\',
#         openreview=\'{f'https://openreview.net/forum?id={self.or_id}'}\',
#         id='{self.conf_id}',
#         paper='{self.url}',
#         abstract={sanitized_abstract})
# }}}}'''


# class PaperEncoder(json.JSONEncoder):
#     def default(self, paper):
#         if isinstance(paper, Paper):
#             return {"id": str(paper.id),
#                     "title": paper.title,
#                     "authors": ", ".join(paper.authors),
#                     "url": paper.url,
#                     "or_id": paper.or_id,
#                     "oral": str(paper.oral),
#                     "short": str(paper.short),
#                     "abstract": paper.abstract}

#         return json.JSONEncoder.default(self, paper)


if __name__ == "__main__":
    assert len(argv) == 4

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    # mode: str = argv[3]
    # assert mode in ["short", "full"]

    dest_path: Path = Path(argv[3])

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(**v) for (k, v) in raw_papers.items()}

    template: str
    with open(template_path, 'r') as f:
        template = f.read()
    filled = template[:]

    regexp: Pattern = re.compile("{{[OSP]([0-9]+)}}")
    matches: List[Match] = list(regexp.finditer(template))

    print(len(matches))
    print(matches)
    for m in matches:
        # id = m[1][2:-2]
        int_id: int = int(m[1])
        # print(m[0], int_id)
        # print(papers[int_id])

        filled = filled.replace(m[0], str(papers[int_id]))

    with open(dest_path, 'w') as sink:
        sink.write(filled)

    # if mode == "full":
    #     with open(template_path, 'r') as f:
    #         template = f.read()

    #     orals: List[Paper] = sorted([p for p in papers.values() if p.oral], key=attrgetter('title'))
    #     assert len(orals) == 18, len(orals)
    #     with_orals = template.replace("ORALS", "\n".join(map(str, orals)))

    #     posters: List[Paper] = sorted([p for p in papers.values() if p.poster], key=attrgetter('title'))
    #     assert len(posters) == 47, len(posters)
    #     with_both = with_orals.replace("POSTERS", "\n".join(map(str, posters)))

    #     with open(dest_path, 'w') as sink:
    #         sink.write(with_both)
    # elif mode == "short":
    #     with open(template_path, 'r') as f:
    #         template = f.read()

    #     shorts: List[Paper] = sorted([p for p in papers.values() if p.short], key=attrgetter('title'))
    #     assert len(shorts) == 41, len(shorts)
    #     with_shorts = template.replace("SHORTS", "\n".join(map(str, shorts)))
