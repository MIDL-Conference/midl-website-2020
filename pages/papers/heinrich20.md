---
title: "Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S131 - Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies


### Mattias P Heinrich, Lasse Hansen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=wbZM-DcJB9">Paper</a>
        - <a href="https://openreview.net/forum?id=wbZM-DcJB9">Reviews</a>
        {{ teaser('MvcUYnalf4U') }}

<span class="paper_abstract">
        Multimodal image registration is a very challenging problem for deep learning approaches. Most current work focuses on either supervised learning that requires labelled training scans and may yield models that bias towards annotated structures or unsupervised approaches that are based on hand-crafted similarity metrics and may therefore not outperform their classical non-trained counterparts. We believe that unsupervised domain adaptation can be beneficial in overcoming the current limitations for multimodal registration, where good metrics are hard to define.      Domain adaptation has so far been mainly limited to classification problems. We propose the first use of unsupervised domain adaptation for discrete multimodal registration. Based on a source domain for which quantised displacement labels are available as supervision, we transfer the output distribution of the network to better resemble the target domain (other modality) using classifier discrepancies. To improve upon the sliced Wasserstein metric for 2D histograms, we present a novel approximation that projects predictions into 1D and computes the L1 distance of their cumulative sums. Our proof-of-concept demonstrates the applicability of domain transfer from mono- to multimodal 2D registration of canine MRI scans and improves the registration accuracy from 33% (using sliced Wasserstein) to 44%.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 UTC-4 - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s131") }}

---

### Short paper

---

{{ presentation('MvcUYnalf4U', '/slides/heinrich20.pdf', 720, 450) }}