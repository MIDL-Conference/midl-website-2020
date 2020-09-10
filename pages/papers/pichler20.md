---
title: "On Direct Distribution Matching for Adapting Segmentation Networks"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P045 - On Direct Distribution Matching for Adapting Segmentation Networks

#### Georg Pichler, Jose Dolz, Ismail Ben Ayed, Pablo Piantanida

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=-C9f-eGAuV">Paper</a>
- <a href="https://openreview.net/forum?id=-C9f-eGAuV">Reviews</a>
{{ teaser('6RQxDpWY6OE') }}

<p>
    <span class="abstract">
        Minimization of distribution matching losses is a principled approach to domain adaptation in the context of image classification. However, it is largely overlooked in adapting segmentation networks, which is currently dominated by adversarial models. We propose a class of loss functions, which encourage direct kernel density matching in the network-output space, up to some geometric transformations computed from unlabeled inputs. Rather than using an intermediate domain discriminator, our direct approach unifies distribution matching and segmentation in a single loss. Therefore, it simplifies segmentation adaptation by avoiding extra adversarial steps, while improving quality, stability and efficiency of training. We juxtapose our approach to state-of-the-art segmentation adaptation via adversarial training in the network-output space. In the challenging task of adapting brain segmentation across different magnetic resonance imaging (MRI) modalities, our approach achieves significantly better results both in terms of accuracy and stability.      
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p045") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('OX1qKZ8NR8I', '/slides/pichler20.pdf', 720, 450) }}