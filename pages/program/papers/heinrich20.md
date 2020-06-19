---
title: "Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies"
---
<style>
.paper_abstract {
  display: none;
  font-size: 90%;
  line-height: 1.35;
  text-align: justify;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}

.paper_qa {
  display: none;
  line-height: 1.35;
  text-align: center;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}
</style>

{% from "_macros.html" import button %}

# S131 - Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies


##### Mattias P Heinrich, Lasse Hansen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=wbZM-DcJB9">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'Multimodal image registration is a very challenging problem for deep learning approaches. Most current work focuses on either supervised learning that requires labelled training scans and may yield models that bias towards annotated structures or unsupervised approaches that are based on hand-crafted similarity metrics and may therefore not outperform their classical non-trained counterparts. We believe that unsupervised domain adaptation can be beneficial in overcoming the current limitations for multimodal registration, where good metrics are hard to define.      Domain adaptation has so far been mainly limited to classification problems. We propose the first use of unsupervised domain adaptation for discrete multimodal registration. Based on a source domain for which quantised displacement labels are available as supervision, we transfer the output distribution of the network to better resemble the target domain (other modality) using classifier discrepancies. To improve upon the sliced Wasserstein metric for 2D histograms, we present a novel approximation that projects predictions into 1D and computes the L1 distance of their cumulative sums. Our proof-of-concept demonstrates the applicability of domain transfer from mono- to multimodal 2D registration of canine MRI scans and improves the registration accuracy from 33% (using sliced Wasserstein) to 44%.'
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/S131") }}

---

### Short paper
