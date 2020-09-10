---
title: "An Auxiliary Task for Learning Nuclei Segmentation in 3D Microscopy Images"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P017 - An Auxiliary Task for Learning Nuclei Segmentation in 3D Microscopy Images

#### Peter Hirsch, Dagmar Kainmueller

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=iJVionbWNX">Paper</a>
- <a href="https://openreview.net/forum?id=iJVionbWNX">Reviews</a>
{{ teaser('fLaZoYgUpOo') }}

<p>
    <span class="abstract">
        Segmentation of cell nuclei in microscopy images is a prevalent necessity in cell biology.      Especially for three-dimensional datasets, manual segmentation is prohibitively time-consuming, motivating the need for automated methods. Learning-based methods trained on pixel-wise ground-truth segmentations have been shown to yield state-of-the-art results on 2d benchmark image data of nuclei, yet a respective benchmark is missing for 3d image data. In this work, we perform a comparative evaluation of nuclei segmentation algorithms on a database of manually segmented 3d light microscopy volumes. We propose a novel learning strategy that boosts segmentation accuracy by means of a simple auxiliary task, thereby robustly outperforming each of our baselines. Furthermore, we show that one of our baselines, the popular three-label model, when trained with our proposed auxiliary task, outperforms the recent StarDist-3D.      As an additional, practical contribution, we benchmark nuclei segmentation against nuclei detection, i.e. the task of merely pinpointing individual nuclei without generating respective pixel-accurate segmentations. For learning nuclei detection, large 3d training datasets of manually annotated nuclei center points are available. However, the impact on detection accuracy caused by training on such sparse ground truth as opposed to dense pixel-wise ground truth has not yet been quantified. To this end, we compare nuclei detection accuracy yielded by training on dense vs. sparse ground truth. Our results suggest that training on sparse ground truth yields competitive nuclei detection rates. 
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #3  - 9:30 - 11:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/p017") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('9HfD3vEXtHE', '/slides/hirsch20.pdf', 720, 450) }}