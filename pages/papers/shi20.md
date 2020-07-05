---
title: "Automatic Diagnosis of Pulmonary Embolism Using an Attention-guided Framework: A Large-scale Study"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O042 - Automatic Diagnosis of Pulmonary Embolism Using an Attention-guided Framework: A Large-scale Study

### Luyao Shi, Deepta Rajan, Shafiq Abedin, David Beymer, Ehsan Dehghan

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=hsGCHJDRm2">Paper</a>
- <a href="https://openreview.net/forum?id=hsGCHJDRm2">Reviews</a>
{{ teaser('GSQIJjNgytQ') }}

<p>
    <span class="abstract">
        Pulmonary Embolism (PE) is a life-threatening disorder associated with high mortality and morbidity. Prompt diagnosis and immediate initiation of therapeutic action is important. We explored a deep learning model to detect PE on volumetric contrast-enhanced chest CT scans using a 2-stage training strategy. First, a residual convolutional neural network (ResNet) was trained using annotated 2D images. In addition to the classification loss, an attention loss was added during training to help the network focus attention on PE. Next, a recurrent network was used to scan sequentially through the features provided by the pre-trained ResNet to detect PE. This combination allows the network to be trained using both a limited and sparse set of pixel-level annotated images and a large number of easily obtainable patient-level image-label pairs. We used 1,670 sparsely annotated studies and more than 10,000 labeled studies in our training. On a test set with 2,160 patient studies, the proposed method achieved an area under the ROC curve (AUC) of 0.812. The proposed framework is also able to provide localized attention maps that indicate possible PE lesions, which could potentially help radiologists accelerate the diagnostic process.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #6 - Attention  - 12:30 - 13:30 UTC-4 (Wednesday)<br>Poster Session #6  - 13:30 - 15:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o042") }}
[% / %]

---

### Oral presentation

---

{{ presentation('gg9f4XEScec', '/slides/shi20.pdf', 720, 450) }}