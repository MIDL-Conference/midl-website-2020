---
title: "Deep Reinforcement Learning for Organ Localization in CT"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P128 - Deep Reinforcement Learning for Organ Localization in CT

#### Fernando Navarro, Anjany Sekuboyina, Diana Waldmannstetter, Jan C. Peeken, Stephanie E. Combs, Bjoern H. Menze

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="http://proceedings.mlr.press/v121/navarro20a.html">Proceedings</a>
- <a href="https://openreview.net/pdf?id=0vDeD2UD0S">PDF</a>
- <a href="https://openreview.net/forum?id=0vDeD2UD0S">Reviews</a>
{{ teaser('Rk6gCh7eYkU') }}

<p>
    <span class="abstract">
        Robust localization of organs in computed tomography scans is a constant pre-processing requirement for organ-specific image retrieval, radiotherapy planning, and interventional image analysis. In contrast to current solutions based on exhaustive search or region proposals, which require large amounts of annotated data, we propose a deep reinforcement learning approach for organ localization in CT. In this work, an artificial agent is actively self-taught to localize organs in CT by learning from its asserts and mistakes. Within the context of reinforcement learning, we propose a novel set of actions tailored for organ localization in CT. Our method can use as a plug-and-play module for localizing any organ of interest. We evaluate the proposed solution on the public VISCERAL dataset containing CT scans with varying fields of view and multiple organs. We achieved an overall intersection over union of 0.63, an absolute median wall distance of 2.25 mm and a median distance between centroids of 3.65 mm.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p128") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('tQVNgKCWs9I', '/slides/navarro20.pdf', 720, 450) }}