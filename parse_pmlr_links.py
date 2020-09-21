#!/usr/bin/env python3.8

import json
from typing import Dict

from bs4 import BeautifulSoup

from paper import Paper, PaperEncoder


if __name__ == "__main__":
        paper_json: str = "papers.json"
        pmlr_file: str = "http_proceedings.mlr.press_v121.html"

        raw_papers: Dict[str, Dict]
        with open(paper_json, 'r') as pf:
                raw_papers = json.load(pf)
        papers: Dict[str, Paper] = {v["title"].lower(): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

        with open(pmlr_file, 'r') as f:
                pmlr_soup = BeautifulSoup(f.read(), 'html.parser')

        for div in pmlr_soup.find_all("div", {"class": "paper"}):
                title: str = div.find("p", {"class": "title"}).get_text()

                if title.lower() not in papers.keys():
                        if title.lower() == "preface":
                                continue

                        print(title)

                url: str = div.find("p", {"class": "links"}).find_all('a', href=True)[0]['href']
                assert url[-4:] == "html"

                papers[title.lower()].pmlr_url = url

        with open(paper_json, 'w') as sink:
                json.dump({p.id: p for p in papers.values()}, sink, cls=PaperEncoder, indent=4, sort_keys=True)
