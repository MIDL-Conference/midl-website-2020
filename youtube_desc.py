#!/usr/bin/env python3.8

import json
from sys import argv
from pathlib import Path
from typing import Dict

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 2

    papers_path: Path = Path(argv[1])
    assert papers_path.exists()

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    for paper in papers.values():
        first_author: str = paper.authors[0].split(' ')[-1]
        mode: str
        if paper.short:
            mode = "Short presentation"
        else:
            if paper.oral:
                mode = "Oral presentation"
            else:
                mode = "Spotlight presentation"

        print("\n>>>")
        print(f"MIDL 2020, {paper.conf_id}, {first_author} et al. {mode}")
        print(f"{paper.conf_id} - {paper.title}\n\n{', '.join(paper.authors)}\n\nConference page: https://2020.midl.io/{paper.url}\nPDF: https://openreview.net/pdf?id={paper.or_id}\n\nAbstract: {paper.sanitized_abstract}")
