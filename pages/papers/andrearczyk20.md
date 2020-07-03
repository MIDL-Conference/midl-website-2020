---
title: "Automatic Segmentation of Head and Neck Tumors and Nodal Metastases in PET-CT scans"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P205 - Automatic Segmentation of Head and Neck Tumors and Nodal Metastases in PET-CT scans

### Vincent Andrearczyk, Valentin Oreiller, Martin Vallières, Joel Castelli, Hesham Elhalawani, Sarah Boughdad, Mario Jreige, John O. Prior and Adrien Depeursinge

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=1Ql71nEERx">Paper</a>
- <a href="https://openreview.net/forum?id=1Ql71nEERx">Reviews</a>
{{ teaser('t0IWfoGVpoc') }}

<p>
    <span class="abstract">
        Radiomics, the prediction of disease characteristics using quantitative image biomarkers from medical images, relies on expensive manual annotations of Regions of Interest (ROI) to focus the analysis. In this paper, we propose an automatic segmentation of Head and Neck (H&N) tumors and nodal metastases from FDG-PET and CT images. A fully-convolutional network (2D and 3D V-Net) is trained on PET-CT images using ground truth ROIs that were manually delineated by radiation oncologists for 202 patients. The results show the complementarity of the two modalities with a statistically significant improvement from 48.7% and 58.2% Dice Score Coefficients (DSC) with CT- and PET-only segmentation respectively, to 60.6% with a bimodal late fusion approach. We also note that, on this task, a 2D implementation slightly outperforms a similar 3D design (60.6% vs 59.7% for the best results respectively). The data is publicly available and the code will be shared on our GitHub repository.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #1  - 9:30 - 11:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p205") }} -->
[% / %]

---

### Spotlight presentation

---

{{ presentation('ov3rkG8yQok', '/slides/andrearczyk20.pdf', 720, 450) }}