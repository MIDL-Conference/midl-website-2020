---
title: "Uncertainty-based Graph Convolutional Networks for Organ Segmentation Refinement"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O146 - Uncertainty-based Graph Convolutional Networks for Organ Segmentation Refinement

### Roger D. Soberanis-Mukul, Nassir Navab, Shadi Albarqouni

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=UUie86nf5B">Paper</a>
- <a href="https://openreview.net/forum?id=UUie86nf5B">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        Organ segmentation in CT volumes is an important pre-processing step in many computer assisted intervention and diagnosis methods. In recent years, convolutional neural networks have dominated the state of the art in this task. However, since this problem presents a challenging environment due to high variability in the organ\'s shape and similarity between tissues, the generation of false negative and false positive regions in the output segmentation is a common issue. Recent works have shown that the uncertainty analysis of the model can provide us with useful information about potential errors in the segmentation. In this context, we proposed a segmentation refinement method based on uncertainty analysis and graph convolutional networks. We employ the uncertainty levels of the convolutional network in a particular input volume to formulate a semi-supervised graph learning problem that is solved by training a graph convolutional network. To test our method we refine the initial output of a 2D U-Net. We validate our framework with the NIH pancreas dataset and the spleen dataset of the medical segmentation decathlon. We show that our method outperforms the state-of-the art CRF refinement method by improving the dice score by 1% for the pancreas and 2% for spleen, with respect to the original U-Net\'s prediction. Finally, we discuss the results and current limitations of the model for future work in this research direction. For reproducibility purposes, we make our code publicly available
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #1 - Uncertainty  - 8:30 - 9:30 UTC-4 (Monday)<br>Poster Session #1  - 9:30 - 11:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o146") }}
[% / %]

---

### Oral presentation

---

{{ presentation('VwF0KeALAFU', '/slides/soberanis--mukul20.pdf', 720, 450) }}