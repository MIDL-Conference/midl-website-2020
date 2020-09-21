---
title: "Continual Learning for Domain Adaptation in Chest X-ray Classification"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P037 - Continual Learning for Domain Adaptation in Chest X-ray Classification

#### Matthias Lenga, Heinrich Schulz, Axel Saalbach

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="http://proceedings.mlr.press/v121/lenga20a.html">Proceedings</a>
- <a href="https://openreview.net/pdf?id=lgE-MUlU1g">PDF</a>
- <a href="https://openreview.net/forum?id=lgE-MUlU1g">Reviews</a>
{{ teaser('bjuglG8y3q0') }}

<p>
    <span class="abstract">
        Over the last years, Deep Learning has been successfully applied to a broad range of medical applications. Especially in the context of chest X-ray classification, results have been reported which are on par, or even superior to experienced radiologists. Despite this success in controlled experimental environments, it has been noted that the ability of Deep Learning models to generalize to data from a new domain (with potentially different tasks) is often limited. In order to address this challenge, we investigate techniques from the field of Continual Learning (CL) including Joint Training (JT), Elastic Weight Consolidation (EWC) and Learning Without Forgetting (LWF). Using the ChestX-ray14 and the MIMIC-CXR datasets, we demonstrate empirically that these methods provide promising options to improve the performance of Deep Learning models on a target domain and to mitigate effectively catastrophic forgetting for the source domain. To this end, the best overall performance was obtained using JT, while for LWF competitive results could be achieved - even without accessing data from the source domain.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p037") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('qzN4zNk8-Tc', '/slides/lenga20.pdf', 720, 450) }}