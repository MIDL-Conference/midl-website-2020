---
title: "Deep learning-based retinal vessel segmentation with cross-modal evaluation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P249 - Deep learning-based retinal vessel segmentation with cross-modal evaluation

### Luisa Sanchez Brea, Danilo Andrade De Jesus, Stefan Klein, Theo van Walsum

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=-3UtpvQHNX">Paper</a>
- <a href="https://openreview.net/forum?id=-3UtpvQHNX">Reviews</a>
{{ teaser('3Va3V4-2wl8') }}

<p>
    <span class="abstract">
        This work proposes a general pipeline for retinal vessel segmentation on en-face images. The main goal is to analyse if a model trained in one of two modalities, Fundus Photography (FP) or Scanning Laser Ophthalmoscopy (SLO), is transferable to the other modality accurately. This is motivated by the lack of development and data available in en-face imaging modalities other than FP. FP and SLO images of four and two publicly available datasets, respectively, were used. First, the current approaches were reviewed in order to define a basic pipeline for vessel segmentation. A state-of-art deep learning architecture (U-net) was used, and the effect of varying the patch size and number of patches was studied by training, validating, and testing on each dataset individually. Next, the model was trained in either FP or SLO images, using the available datasets for a given modality combined. Finally, the performance of each network was tested on the other modality. The models trained on each dataset showed a performance comparable to the state-of-the art and to the inter-rater reliability. Overall, the best performance was observed for the largest patch size (256) and the maximum number of overlapped images in each dataset, with a mean sensitivity, specificity, accuracy, and Dice score of 0.89$\pm$0.05, 0.95$\pm$0.02, 0.95$\pm$0.02, and 0.73$\pm$0.07, respectively. Models trained and tested on the same modality presented a sensitivity, specificity, and accuracy equal or higher than 0.9. The validation on a different modality has shown significantly better sensitivity and Dice on those trained on FP.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #5 *9:30 - 11:00 UTC-4 (Wednesday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p249") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('3Va3V4-2wl8') }}