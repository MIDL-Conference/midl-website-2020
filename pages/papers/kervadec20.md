---
title: "Bounding boxes for weakly supervised segmentation: Global constraints get close to full supervision"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O001 - Bounding boxes for weakly supervised segmentation: Global constraints get close to full supervision

### Hoel Kervadec, Jose Dolz, Shanshan Wang, Eric Granger, Ismail Ben Ayed

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=m7HZ-yil_-">Paper</a>
- <a href="https://openreview.net/forum?id=m7HZ-yil_-">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        We propose a novel weakly supervised learning segmentation based on several global constraints derived from box annotations. Particularly, we leverage a classical tightness prior to a deep learning setting via imposing a set of constraints on the network outputs. Such a powerful topological prior prevents solutions from excessive shrinking by enforcing any horizontal or vertical line within the bounding box to contain, at least, one pixel of the foreground region. Furthermore, we integrate our deep tightness prior with a global background emptiness constraint, guiding training with information outside the bounding box. We demonstrate experimentally that such a global constraint is much more powerful than standard cross-entropy for the background class. Our optimization problem is challenging as it takes the form of a large set of inequality constraints on the outputs of deep networks. We solve it with sequence of unconstrained losses based on a recent powerful extension of the log-barrier method, which is well-known in the context of interior-point methods. This accommodates standard stochastic gradient descent (SGD) for training deep networks, while avoiding computationally expensive and unstable Lagrangian dual steps and projections. Extensive experiments over two different public data sets and applications (prostate and brain lesions) demonstrate that the synergy between our global tightness and emptiness priors yield very competitive performances, approaching full supervision and outperforming significantly DeepCut. Furthermore, our approach removes the need for computationally expensive proposal generation. Our code is shared anonymously.   
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #2 - Limited Data  - 12:30 - 13:30 UTC-4 (Monday)<br>Poster Session #2  - 13:30 - 15:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o001") }}
[% / %]

---


### Oral presentation

---

{{ presentation('1HIK_z-XeMU', '/slides/kervadec20.pdf', 720, 450) }}