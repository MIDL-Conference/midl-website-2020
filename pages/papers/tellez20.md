---
title: "Extending Unsupervised Neural Image Compression With Supervised Multitask Learning"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}

# O096 - Extending Unsupervised Neural Image Compression With Supervised Multitask Learning


### David Tellez, Diederik Hoppener, Cornelis Verhoef, Dirk Grunhagen, Pieter Nierop, Michal Drozdzal, Jeroen van der Laak, Francesco Ciompi

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/forum?id=oepOBj_A7E">Reviews</a>
        {{ teaser('') }}

<span class="paper_abstract">
        We focus on the problem of training convolutional neural networks on gigapixel histopathology images to predict image-level targets. For this purpose, we extend Neural Image Compression (NIC), an image compression framework that reduces the dimensionality of these images using an encoder network trained unsupervisedly. We propose to train this encoder using supervised multitask learning (MTL) instead. We applied the proposed MTL NIC to two histopathology datasets and three tasks. First, we obtained state-of-the-art results in the Tumor Proliferation Assessment Challenge of 2016 (TUPAC16). Second, we successfully classified histopathological growth patterns in images with colorectal liver metastasis (CLM). Third, we predicted patient risk of death by learning directly from overall survival in the same CLM data. Our experimental results suggest that the representations learned by the MTL objective are: (1) highly specific, due to the supervised training signal, and (2) transferable, since the same features perform well across different tasks. Additionally, we trained multiple encoders with different training objectives, e.g. unsupervised and variants of MTL, and observed a positive correlation between the number of tasks in MTL and the system performance on the TUPAC16 dataset.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        TUE 8:30-9:30 ET - Oral Session #3 - Networks for Histology<br/>TUE 9:30-11:00 ET - Poster Session #3
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/o096") }}

---

### Oral presentation

---

