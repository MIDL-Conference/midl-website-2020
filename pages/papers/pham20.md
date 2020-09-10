---
title: "Interpreting Chest X-rays via CNNs that Exploit Hierarchical Disease Dependencies and Uncertainty Labels"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S023 - Interpreting Chest X-rays via CNNs that Exploit Hierarchical Disease Dependencies and Uncertainty Labels

#### Hieu H. Pham, Tung T. Le, Dat T. Ngo, Dat Q. Tran, Ha Q. Nguyen

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=4o1GLIIHlh">Paper</a>
- <a href="https://openreview.net/forum?id=4o1GLIIHlh">Reviews</a>
{{ teaser('oOBRZmyJW7o') }}

<p>
    <span class="abstract">
        We present a new approach based on deep convolutional neural networks (CNNs) for predicting the presence of 14 common thoracic diseases and observations. A strong set of CNNs are trained on over 200,000 chest X-ray images provided by CheXpert - a large scale chest X-ray dataset. In particular, dependencies among abnormality labels and uncertain samples are fully exploited during the training and inference stages. Experiments indicate that the proposed method achieves a mean area under the curve (AUC) of 0.940 in predicting 5 selected pathologies. To the best of our knowledge, this is the highest AUC score yet reported on this dataset to date. Additionally, the proposed method is also evaluated on the independent test set of the CheXpert competition and reports a performance level comparable to practicing radiologists. Our obtained result ranks first on the CheXpert leaderboard at the time of writing this paper.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/s023") }}
[% / %]

---


### Short paper

---

{{ presentation('gR8kvihcSk0', '/slides/pham20.pdf', 720, 450) }}