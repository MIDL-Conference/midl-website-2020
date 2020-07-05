#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Dict, List

from paper import Paper, PaperEncoder


if __name__ == "__main__":
    assert len(argv) == 2

    papers_path: Path = Path(argv[1])
    assert papers_path.exists()

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    for paper in papers.values():
        paper.slides = paper.url.replace("html", "pdf").replace("papers/", "/slides/")

    with open(papers_path, 'w') as sink:
        json.dump({p.id: p for p in papers.values()}, sink, cls=PaperEncoder, indent=4, sort_keys=True)
