---
title: "Red-GAN: Attacking class imbalance via conditioned generation. Yet another medical imaging perspective"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P071 - Red-GAN: Attacking class imbalance via conditioned generation. Yet another medical imaging perspective

### Ahmad B Qasim, Ivan Ezhov, Suprosanna Shit, Oliver Schoppe, Johannes Paetzold, Anjany Sekuboyina, Florian Kofler, Jana Lipkova, Hongwei Li, Bjoern Menze

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=UHtZuvXHoA">Paper</a>
- <a href="https://openreview.net/forum?id=UHtZuvXHoA">Reviews</a>
{{ teaser('HCP2X8z44VI') }}

<p>
    <span class="abstract">
        Exploiting learning algorithms under scarce data regimes is a limitation and a reality of the medical imaging field. In an attempt to mitigate the problem, we propose a data augmentation protocol based on generative adversarial networks. The networks are conditioned at a pixel-level (segmentation mask) and at a global-level information (acquisition environment or lesion type). Such conditioning provides immediate access to the image-label pairs while controlling class specific appearance of the synthesized images. To stimulate synthesis of the features relevant for the segmentation task, an additional passive player in a form of segmentor is introduced into the the adversarial game.      We validate the approach on two medical datasets: BraTS, ISIC. By controlling the class distribution through injection of synthetic images into the training set we achieve control over the accuracy levels of the datasets\' classes.  
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

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p071") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('HCP2X8z44VI') }}