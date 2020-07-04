---
title: "Automatic segmentation of the pulmonary lobes with a 3D u-net and optimized loss function"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S014 - Automatic segmentation of the pulmonary lobes with a 3D u-net and optimized loss function

### Bianca Lassen-Schmidt, Alessa Hering, Stefan Krass, Hans Meine

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=AkziGgmwl">Paper</a>
- <a href="https://openreview.net/forum?id=AkziGgmwl">Reviews</a>
{{ teaser('IfeHzhAK1yM') }}

<p>
    <span class="abstract">
        Fully-automatic lung lobe segmentation is challenging due to anatomical variations, pathologies, and incomplete fissures. We trained a 3D u-net for pulmonary lobe segmentation on 49 mainly publically available datasets and introduced a weighted Dice loss function to emphasize the lobar boundaries. To validate the performance of the proposed method we compared the results to two other methods. The new loss function improved the mean distance to 1.46 mm (compared to 2.08 mm for simple loss function without weighting).
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

{{ button("Access paper channel", "https://chat.midl.io/channel/s014") }}
[% / %]

---

### Short paper

---

{{ presentation('IfeHzhAK1yM', '/slides/lassen-schmidt20.pdf', 720, 450) }}