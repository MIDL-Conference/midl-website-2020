---
title: "Mutual information based deep clustering for semi-supervised segmentation"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P099 - Mutual information based deep clustering for semi-supervised segmentation


### Jizong Peng, Marco Pedersoli, Christian Desrosiers

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=iunvffXgPm">Paper</a>
        - <a href="https://openreview.net/forum?id=iunvffXgPm">Reviews</a>
        {{ teaser('') }}

<span class="paper_abstract">
        The scarcity of labeled data often limits the application of deep learning to medical image segmentation. Semi-supervised learning helps overcome this limitation by leveraging unlabeled images to guide the learning process. In this paper, we propose using a clustering loss based on mutual information that explicitly enforces prediction consistency between nearby pixels in unlabeled images, and for random perturbation of these images, while imposing the network to predict the correct labels for annotated images. Since mutual information does not require a strict ordering of clusters in two different cluster assignments, we propose to incorporate another consistency regularization loss which forces the alignment of class probabilities at each pixel of perturbed unlabeled images. We evaluate the method on three challenging publicly-available medical datasets for image segmentation. Experimental results show our method to outperform recently-proposed approaches for semi-supervised and yield a performance comparable to fully-supervised training.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 13:30-15:00 UTC-4 - Poster Session #2
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p099") }}

---

### Spotlight presentation

---

