---
title: "A Cross-Stitch Architecture for Joint Registration and Segmentation in Adaptive Radiotherapy"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P197 - A Cross-Stitch Architecture for Joint Registration and Segmentation in Adaptive Radiotherapy


### Laurens Beljaards, Mohamed S. Elmahdy, Fons Verbeek, Marius Staring

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=oFXY64JJQ8">Paper</a>
        - <a href="https://openreview.net/forum?id=oFXY64JJQ8">Reviews</a>
        {{ teaser('N8r5sl3ujWU') }}

<span class="paper_abstract">
        Recently, joint registration and segmentation has been formulated in a deep learning setting, by the definition of joint loss functions. In this work, we investigate joining these tasks at the architectural level. We propose a registration network that integrates segmentation propagation between images, and a segmentation network to predict the segmentation directly. These networks are connected into a single joint architecture via so-called cross- stitch units, allowing information to be exchanged between the tasks in a learnable manner. The proposed method is evaluated in the context of adaptive image-guided radiotherapy, using daily prostate CT imaging. Two datasets from different institutes and manufacturers were involved in the study. The first dataset was used for training (12 patients) and validation (6 patients), while the second dataset was used as an independent test set (14 patients). In terms of mean surface distance, our approach achieved 1.06 ± 0.3 mm, 0.91 ± 0.4 mm, 1.27 ± 0.4 mm, and 1.76 ± 0.8 mm on the validation set and 1.82 ± 2.4 mm, 2.45 ± 2.4 mm, 2.45 ± 5.0 mm, and 2.57 ± 2.3 mm on the test set for the prostate, bladder, seminal vesicles, and rectum, respectively. The proposed multi-task network outperformed single-task networks, as well as a network only joined through the loss function, thus demonstrating the capability to leverage the individual strengths of the segmentation and registration tasks. The obtained performance as well as the inference speed make this a promising candidate for daily re-contouring in adaptive radiotherapy, potentially reducing treatment-related side effects and improving quality-of-life after treatment.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 ET - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p197") }}

---

### Spotlight presentation

---

{{ youtube('N8r5sl3ujWU') }}