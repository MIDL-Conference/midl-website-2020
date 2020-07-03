---
title: "DRMIME: Differentiable Mutual Information and Matrix Exponential for Multi-Resolution Image Registration"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P064 - DRMIME: Differentiable Mutual Information and Matrix Exponential for Multi-Resolution Image Registration

### Abhishek Nan, Matthew Tennant, Uriel Rubin, Nilanjan Ray

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=Q0Bm5e6dkW">Paper</a>
- <a href="https://openreview.net/forum?id=Q0Bm5e6dkW">Reviews</a>
{{ teaser('RkWDByLlF5M') }}

<p>
    <span class="abstract">
        In this work, we present a novel unsupervised image registration algorithm. It is differentiable end-to-end and can be used for both multi-modal and mono-modal registration. This is done using mutual information (MI) as a metric. The novelty here is that rather than using traditional ways of approximating MI which are often histogram based, we use a neural estimator called MINE and supplement it with matrix exponential for transformation matrix computation. The introduction of MINE tackles some of the drawbacks of histogram based MI computation and matrix exponential makes the optimization process smoother. We also introduce the idea of a multi-resolution loss, which makes the optimization process faster and more robust. This leads to improved results as compared to the standard algorithms available out-of-the-box in state-of-the-art image registration toolboxes, both in terms of time as well as registration accuracy, which we empirically demonstrate on publicly available datasets.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #4  - 14:30 - 16:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p064") }} -->
[% / %]

---

### Spotlight presentation

---

{{ presentation('ryxGwCywVLY', '/slides/nan20.pdf', 720, 450) }}