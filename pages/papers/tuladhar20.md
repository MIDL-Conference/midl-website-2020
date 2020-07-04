---
title: "Automatic segmentation of stroke lesions in non-contrast computed tomography with convolutional neural networks"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S161 - Automatic segmentation of stroke lesions in non-contrast computed tomography with convolutional neural networks

### Anup Tuladhar, Serena Schimert, Deepthi Rajashekar, Helge C. Kniep, Jens Fiehler, Nils D. Forkert

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=ehpiBRHu07">Paper</a>
- <a href="https://openreview.net/forum?id=ehpiBRHu07">Reviews</a>
{{ teaser('eRF7h5lT04k') }}

<p>
    <span class="abstract">
        Manual lesion segmentation for non-contrast computed tomography (NCCT), a common modality for volumetric follow-up assessment of ischemic strokes, is time-consuming and subject to high inter-observer variability. Our approach uses a combination of a 3D convolutional neural network (CNN) combined with post-processing methods. A total of 272 multi-center clinical NCCT datasets were used: 204 for CNN training, 48 for validation and developing post-processing methods, and 20 for testing. The testing datasets were from centers that did not contribute to the training and validation sets, and were segmented by two neuroradiologists. We achieved a median Dice score of 0.63, which was significantly improved to 0.66 with post-processing. The automatically segmented lesion volumes were not significantly different from the lesion volumes determined by the two manual observers. As the model was trained on datasets from multiple centers, it is broadly applicable. 
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

{{ button("Access paper channel", "https://chat.midl.io/channel/s161") }}
[% / %]

---

### Short paper

---

{{ presentation('eRF7h5lT04k', '/slides/tuladhar20.pdf', 720, 450) }}