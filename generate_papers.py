#!/usr/bin/env python3.8

import json
from sys import argv
from pathlib import Path
from typing import Dict, List
from operator import attrgetter


class Paper():
    def __init__(self, id: str, title: str, authors: str, url: str, or_id: str, oral: str, short: str,
                 abstract: str):
        self.id: int = int(id)
        self.title: str = title
        self.authors: List[str] = authors.split(', ')
        self.url: str = url
        self.or_id: str = or_id
        self.oral: bool = oral == "True"
        self.short: bool = short == "True"
        self.poster: bool = (not self.short) and (not self.oral)
        self.abstract: str = abstract

        assert not (self.oral and self.short)
        if self.short:
            assert not self.oral

        self.conf_sign: str = "O" if self.oral else ("S" if self.short else "P")

        self.conf_id: str = f"{self.conf_sign}{self.id:03d}"

        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        self.sanitized_abstract = repr(sanitized_abstract)

        # self.__class__.__name__: str = "Paper"

    def __str__(self) -> str:
        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        sanitized_abstract = repr(sanitized_abstract)
        # sanitized_abstract: str = repr(self.abstract)

        return f'''{{{{ paper(\'{self.title}\',
        \'{f'{", ".join(self.authors)}'}\',
        openreview=\'{f'https://openreview.net/forum?id={self.or_id}'}\',
        id='{self.conf_id}',
        paper='{self.url}',
        abstract={sanitized_abstract})
}}}}'''


class PaperEncoder(json.JSONEncoder):
    def default(self, paper):
        if isinstance(paper, Paper):
            return {"id": str(paper.id),
                    "title": paper.title,
                    "authors": ", ".join(paper.authors),
                    "url": paper.url,
                    "or_id": paper.or_id,
                    "oral": str(paper.oral),
                    "short": str(paper.short),
                    "abstract": paper.abstract}

        return json.JSONEncoder.default(self, paper)


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
        result = result.replace("TITLE", paper.title)
        result = result.replace("AUTHORS", ", ".join(paper.authors))
        result = result.replace("ORID", paper.or_id)
        result = result.replace("ABSTRACT", paper.sanitized_abstract)

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
