---
title: "Towards multi-sequence MR image recovery from undersampled k-space data"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O018 - Towards multi-sequence MR image recovery from undersampled k-space data

### Cheng Peng, Wei-An Lin, Rama Chellappa, S. Kevin Zhou

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=Pk7In-gVEd">Paper</a>
- <a href="https://openreview.net/forum?id=Pk7In-gVEd">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        Undersampled MR image recovery has been widely studied for accelerated MR acquisition. However, it has been mostly studied under a single sequence scenario, despite the fact that multi-sequence MR scan is common in practice. In this paper, we aim to optimize multi-sequence MR image recovery from undersampled k-space data under an overall time constraint while considering the difference in acquisition time for various sequences. We first formulate it as a constrained optimization problem and then show that finding the optimal sampling strategy for all sequences and the best recovery model at the same time is combinatorial and hence computationally prohibitive. To solve this problem, we propose a blind recovery model that simultaneously recovers multiple sequences, and an efficient approach to find proper combination of sampling strategy and recovery model. Our experiments demonstrate that the proposed method outperforms sequence-wise recovery, and sheds light on how to decide the undersampling strategy for sequences within an overall time budget.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #5 - Image Generation  - 8:30 - 9:30 UTC-4 (Wednesday)<br>Poster Session #5  - 9:30 - 11:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/o018") }} -->
[% / %]

---

### Oral presentation

---

{{ presentation('nK-JLpor-vM', '/slides/peng20b.pdf', 720, 450) }}