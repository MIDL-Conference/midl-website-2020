#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Dict, List

from paper import Paper, PaperEncoder


if __name__ == "__main__":
    assert len(argv) == 3

    videos_path: Path = Path(argv[1])

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    # First reset values
    for paper in papers.values():
        paper.yt_teaser = ""
        paper.yt_full = ""

    print(">>> Finding teasers...")
    videos: List[Path] = list(videos_path.glob("*MIDL 2020*Teaser*"))
    video_names: List[str] = [v.name for v in videos]
    print(video_names)

    for video in video_names:
        conf_id: str = video.split(", ")[1]
        yt_id: str = video.split(' - ')[1]
        int_id: int = int(conf_id[1:])

        print(conf_id, int_id, yt_id)

        papers[int_id].yt_teaser = yt_id

    print(">>> Finding full presentations")
    videos_full: List[Path] = list(videos_path.glob("*MIDL 2020*presentation*"))
    video_full_names: List[str] = [v.name for v in videos_full]
    print(video_full_names)

    for video in video_full_names:
        conf_id = video.split(", ")[1]
        yt_id = video.split(' - ')[1]
        int_id = int(conf_id[1:])

        print(conf_id, int_id, yt_id)

        papers[int_id].yt_full = yt_id

    with open(papers_path, 'w') as sink:
        json.dump({p.id: p for p in papers.values()}, sink, cls=PaperEncoder, indent=4, sort_keys=True)
