---
title: "Adversarial Domain Adaptation for Cell Segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P336 - Adversarial Domain Adaptation for Cell Segmentation

### Mohammad Minhazul Haq, Junzhou Huang

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=mgvieZlHlv">Paper</a>
- <a href="https://openreview.net/forum?id=mgvieZlHlv">Reviews</a>
{{ teaser('pZe6N4pro4E') }}

<p>
    <span class="abstract">
        To successfully train a cell segmentation network in fully-supervised manner for a particular type of organ or cancer, we need the dataset with ground-truth annotations. However, high unavailability of such annotated dataset and tedious labeling process enforce us to discover a way for training with unlabeled dataset. In this paper, we propose a network named CellSegUDA for cell segmentation on the unlabeled dataset (target domain). It is achieved by applying unsupervised domain adaptation (UDA) technique with the help of another labeled dataset (source domain) that may come from other organs or sources. We validate our proposed CellSegUDA on two public cell segmentation datasets and obtain significant improvement as compared with the baseline methods. Finally, considering the scenario when we have a small number of annotations available from the target domain, we extend our work to CellSegSSDA, a semi-supervised domain adaptation (SSDA) based approach. Our SSDA model also gives excellent results which are quite close to the fully-supervised upper bound in target domain.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #6 *13:30 - 15:00 UTC-4 (Wednesday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p336") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('pZe6N4pro4E') }}