---
title: "Joint Liver Lesion Segmentation and Classification via Transfer Learning"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S322 - Joint Liver Lesion Segmentation and Classification via Transfer Learning


### Michal Heker, Hayit Greenspan

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=8gSjgXg5U">Paper</a>
        - <a href="https://openreview.net/forum?id=8gSjgXg5U">Reviews</a>
        {{ teaser('AFLwTiY2xKU') }}

<span class="paper_abstract">
        Transfer learning and joint learning approaches are extensively used to improve the performance of Convolutional Neural Networks (CNNs). In medical imaging applications in which the target dataset is typically very small, transfer learning improves feature learning while joint learning has shown effectiveness in improving the network\'s generalization and robustness. In this work, we study the combination of these two approaches for the problem of liver lesion segmentation and classification.      For this purpose, 332 abdominal CT slices containing lesion segmentation and classification of three lesion types are evaluated. For feature learning, the dataset of MICCAI 2017 Liver Tumor Segmentation (LiTS) Challenge is used.      Joint learning shows improvement in both segmentation and classification results.      We show that a simple joint framework outperforms the commonly used multi-task architecture (Y-Net), achieving an improvement of 10% in classification accuracy, compared to 3% improvement with Y-Net.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 9:30-11:00 ET - Poster Session #5
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s322") }}

---

### Short paper

---

{{ youtube('AFLwTiY2xKU') }}