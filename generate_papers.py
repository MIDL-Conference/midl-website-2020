#!/usr/bin/env python3.8

import json
from sys import argv
from pathlib import Path
from typing import Dict, List
from operator import attrgetter

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 4

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    dest_path: Path = Path(argv[3])

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(**v) for (k, v) in raw_papers.items()}

    with open(template_path, 'r') as f:
        empty_template: str = f.read()

    paper: Paper
    for paper in papers.values():
        result: str = empty_template[:]

        result = result.replace("CONF_ID", paper.conf_id)
        result = result.replace("SMALLID", paper.conf_id.casefold())
        result = result.replace("TITLE", paper.title)
        result = result.replace("AUTHORS", ", ".join(paper.authors))
        result = result.replace("ORID", paper.or_id)
        result = result.replace("ABSTRACT", paper.sanitized_abstract)
        result = result.replace("SCHEDULE", "<br>".join(paper.schedule))
        result = result.replace("TEASER", paper.yt_teaser)

        if paper.yt_teaser:
            result = result.replace("EMBEDEDTEASE", f"{{{{ youtube('{paper.yt_teaser}') }}}}")
        else:
            result = result.replace("EMBEDEDTEASE", "")

        if paper.yt_full and paper.slides:
            result = result.replace("PRESENTATION", f"{{{{ presentation('{paper.yt_full}', '{paper.slides}', 720, 450) }}}}")
        else:
            result = result.replace("PRESENTATION", "")

        oral_text: str
        if paper.oral:
            oral_text = "Oral presentation"
        elif paper.poster:
            oral_text = "Spotlight presentation"
        elif paper.short:
            oral_text = "Short paper"

        result = result.replace("ORAL", oral_text)

        with open((dest_path / Path(paper.url)).with_suffix(".md"), 'w') as sink:
            sink.write(result)
