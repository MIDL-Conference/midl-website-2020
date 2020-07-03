---
title: "4D Deep Learning for Multiple-Sclerosis Lesion Activity Segmentation"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S092 - 4D Deep Learning for Multiple-Sclerosis Lesion Activity Segmentation


### Nils Gessert, Marcel Bengs, Julia Krüger, Roland Opfer, Ann-Christin Ostwaldt, Praveena Manogaran, Sven Schippling, Alexander Schlaefer

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=238UzYB1d9">Paper</a>
        - <a href="https://openreview.net/forum?id=238UzYB1d9">Reviews</a>
        {{ teaser('mISTl-A5EK8') }}

<span class="paper_abstract">
        Multiple sclerosis lesion activity segmentation is the task of detecting new and enlarging lesions that appeared between a baseline and a follow-up brain MRI scan. While deep learning methods for single-scan lesion segmentation are common, deep learning approaches for lesion activity have only been proposed recently. Here, a two-path architecture processes two 3D MRI volumes from two time points. In this work, we investigate whether extending this problem to full 4D deep learning using a history of MRI volumes and thus an extended baseline can improve performance. For this purpose, we design a recurrent multi-encoder-decoder architecture for processing 4D data. We find that adding more temporal information is beneficial and our proposed architecture outperforms previous approaches with a lesion-wise true positive rate of 0.84 at a lesion-wise false positive rate of 0.19.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        TUE 9:30-11:00 UTC-4 - Poster Session #3
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s092") }}

---

### Short paper

---

{{ presentation('mISTl-A5EK8', '/slides/gessert20.pdf', 720, 450) }}