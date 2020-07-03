---
title: "A learning strategy for contrast-agnostic MRI segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O072 - A learning strategy for contrast-agnostic MRI segmentation

### Benjamin Billot, Douglas N. Greve, Koen Van Leemput, Bruce Fischl, Juan Eugenio Iglesias, Adrian V. Dalca

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=Qz2DgRQGlP">Paper</a>
- <a href="https://openreview.net/forum?id=Qz2DgRQGlP">Reviews</a>
{{ teaser('ewKD9UqwUDk') }}

<p>
    <span class="abstract">
        We present a deep learning strategy for contrast-agnostic semantic segmentation of unpreprocessed brain MRI scans, without requiring additional training or fine-tuning for new modalities. Classical Bayesian methods address this segmentation problem with unsupervised intensity models, but require significant computational resources. In contrast, learning-based methods can be fast at test time, but are sensitive to the data available at training. Our proposed learning method, SynthSeg, leverages a set of training segmentations (no intensity images required) to generate synthetic scans of widely varying contrasts on the fly during training. These scans are produced using the generative model of the classical Bayesian segmentation framework, with randomly sampled parameters for appearance, deformation, noise, and bias field. Because each mini-batch has a different synthetic contrast, the final network is not biased towards any specific MRI contrast. We comprehensively evaluate our approach on four datasets comprising over 1,000 subjects and four MR contrasts. The results show that our approach successfully segments every contrast in the data, performing slightly better than classical Bayesian segmentation, and three orders of magnitude faster. Moreover, even within the same type of MRI contrast, our strategy generalizes significantly better across datasets, compared to training using real images. Finally, we find that synthesizing a broad range of contrasts, even if unrealistic, increases the generalization of the neural network. Our code and model are open source at https://github.com/BBillot/SynthSeg.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #2 - Limited Data *12:30 - 13:30 UTC-4 (Monday)*<br>Poster Session #2 *13:30 - 15:00 UTC-4 (Monday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/o072") }} -->
[% / %]

---

### Oral presentation

---

{{ youtube('ewKD9UqwUDk') }}