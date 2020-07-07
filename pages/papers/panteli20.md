---
title: "Siamese Tracking of Cell Behaviour Patterns"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P109 - Siamese Tracking of Cell Behaviour Patterns

### Andreas Panteli, Deepak K. Gupta, Nathan de Bruin, Efstratios Gavves

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=V3ZrDLgNgu">Paper</a>
- <a href="https://openreview.net/forum?id=V3ZrDLgNgu">Reviews</a>
{{ teaser('48HXH_WYi6k') }}

<p>
    <span class="abstract">
        Tracking and segmentation of biological cells in video sequences is a challenging problem, especially due to the similarity of the cells and high levels of inherent noise. Most machine learning-based approaches lack robustness and suffer from sensitivity to less prominent events such as mitosis, apoptosis and cell collisions. Due to the large variance in medical image characteristics, most approaches are dataset-specific and do not generalise well on other datasets.      In this paper, we propose a simple end-to-end cascade neural architecture able to model the movement behaviour of biological cells and predict collision and mitosis events. Our approach uses U-Net for an initial segmentation which is then improved through processing by a siamese tracker capable of matching each cell along the temporal axis. By facilitating the re-segmentation of collided and mitotic cells, our method demonstrates its capability to handle volatile trajectories and unpredictable cell locations while being invariant to cell morphology. We demonstrate that our tracking approach achieves state-of-the-art results on  PhC-C2DL-PSC and Fluo-N2DH-SIM+ datasets and ranks second on the DIC-C2DH-HeLa dataset of the cell tracking challenge benchmarks. 
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p109") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('AnEDZ76eOmY', '/slides/panteli20.pdf', 720, 450) }}