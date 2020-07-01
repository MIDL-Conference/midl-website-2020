#!/usr/bin/env python3.8

import json
from typing import List


class Paper():
    def __init__(self, id: str, title: str, authors: str, url: str, or_id: str, oral: str, short: str,
                 abstract: str, schedule: str = "", slides: str = "", yt_teaser: str = "",
                 yt_full: str = "", ignore_schedule: bool = False):
        self.id: int = int(id)
        self.title: str = title
        self.authors: List[str] = authors.split(', ')
        self.url: str = url
        self.or_id: str = or_id
        self.oral: bool = oral == "True"
        self.short: bool = short == "True"
        self.poster: bool = (not self.short) and (not self.oral)
        self.abstract: str = abstract
        self.slides: str = slides
        self.yt_teaser: str = yt_teaser
        self.yt_full: str = yt_full

        self.schedule: List[str]
        if not schedule:
            self.schedule = []
        else:
            self.schedule = schedule.split('\n')

        assert not (self.oral and self.short)
        if self.short:
            assert not self.oral

        if not ignore_schedule:
            try:
                if not self.oral:
                    assert len(self.schedule) == 1
                else:
                    assert len(self.schedule) == 2
            except AssertionError:
                print(self.id, self.schedule)

        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        self.sanitized_abstract = sanitized_abstract

        self.conf_sign: str = "O" if self.oral else ("S" if self.short else "P")

        self.conf_id: str = f"{self.conf_sign}{self.id:03d}"

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
        pdf=\'{f'https://openreview.net/pdf?id={self.or_id}'}\',
        id='{self.conf_id}',
        url='{self.url}',
        teaser=\'{f'https://youtu.be/{self.yt_teaser}' if self.yt_teaser else ""}\',
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
                    "abstract": paper.abstract,
                    "schedule": "\n".join(paper.schedule),
                    "slides": paper.slides,
                    "yt_teaser": paper.yt_teaser,
                    "yt_full": paper.yt_full}

        return json.JSONEncoder.default(self, paper)
