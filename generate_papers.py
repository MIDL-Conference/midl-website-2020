#!/usr/bin/env python3.8

import json
from sys import argv
from pathlib import Path
from typing import Dict, List
from operator import attrgetter

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 5

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    dest_path: Path = Path(argv[3])

    root_slides: Path = Path(argv[4])

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

        if paper.award:
            result = result.replace("AWARD", f"## {paper.award}")
        else:
            result = result.replace("AWARD", "")

        if paper.yt_teaser:
            result = result.replace("EMBEDEDTEASE", f"{{{{ youtube('{paper.yt_teaser}') }}}}")
        else:
            result = result.replace("EMBEDEDTEASE", "")

        if paper.short:
            result = result.replace("PROCEEDINGS", "")
        else:
            result = result.replace("PROCEEDINGS", f'\n- <a href="{paper.pmlr_url}">Proceedings</a>')

        # slides_path: Path = Path(paper.slides)

        if not (root_slides / paper.slides[1:]).exists():
            print(f"\tPaper {paper.conf_id} without slides: {paper.url} {(root_slides / paper.slides)}")

        # yt_link = paper.yt_teaser if paper.short else paper.yt_full
        yt_link = paper.yt_full

        if yt_link and (root_slides / paper.slides[1:]).exists():
            result = result.replace("PRESENTATION", f"{{{{ presentation('{yt_link}', '{paper.slides}', 720, 450) }}}}")
        elif yt_link:
            result = result.replace("PRESENTATION", f"{{{{ youtube('{yt_link}') }}}}")
        else:
            result = result.replace("PRESENTATION", "")
            print(f"\tPaper {paper.conf_id} with neither slides or presentation.")

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
