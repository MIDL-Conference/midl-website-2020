---
title: "Medical Image Segmentation via Unsupervised Convolutional Neural Network"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S038 - Medical Image Segmentation via Unsupervised Convolutional Neural Network

#### Junyu Chen, Eric C. Frey

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=XrbnSCv4LU">PDF</a>
- <a href="https://openreview.net/forum?id=XrbnSCv4LU">Reviews</a>
{{ teaser('JOa6zS7TNCI') }}

<p>
    <span class="abstract">
        For the majority of the learning-based segmentation methods, a large quantity of high-quality training data is required. In this paper, we present a novel learning-based segmentation model that could be trained semi- or un- supervised. Specifically, in the unsupervised setting, we parameterize the Active contour without edges (ACWE) framework via a convolutional neural network (ConvNet), and optimize the parameters of the ConvNet using a self-supervised method. In another setting (semi-supervised), the auxiliary segmentation ground truth is used during training. We show that the method provides fast and high-quality bone segmentation in the context of single-photon emission computed tomography (SPECT) image.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #2  - 13:30 - 15:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/s038") }}
[% / %]

---


### Short paper

---

{{ presentation('IVMy-EUeTc8', '/slides/chen20.pdf', 720, 450) }}