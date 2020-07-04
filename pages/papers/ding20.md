---
title: "Uncertainty-Aware Training of Neural Networks for Selective Medical Image Segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O102 - Uncertainty-Aware Training of Neural Networks for Selective Medical Image Segmentation

### Yukun Ding, Jinglan Liu, Xiaowei Xu, Meiping Huang, Jian Zhuang, Jinjun Xiong, Yiyu Shi

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=F1MIJCqX2J">Paper</a>
- <a href="https://openreview.net/forum?id=F1MIJCqX2J">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        State-of-the-art deep learning based methods have achieved remarkable performance on medical image segmentation. Their applications in the clinical setting are, however, limited due to the lack of trustworthiness and reliability. Selective image segmentation has been proposed to address this issue by letting a DNN model process instances with high confidence while referring difficult ones with high uncertainty to experienced radiologists. As such, the model performance is only affected by the predictions on the high confidence subset rather than the whole dataset. Existing selective segmentation methods, however, ignore this unique property of selective segmentation and train their DNN models by optimizing accuracy on the entire dataset. Motivated by such a discrepancy, we present a novel method in this paper that considers such uncertainty in the training process to maximize the accuracy on the confident subset rather than the accuracy on the whole dataset. Experimental results using the whole heart and great vessel segmentation and gland segmentation show that such a training scheme can significantly improve the performance of selective segmentation. 
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

{{ button("Access paper channel", "https://chat.midl.io/channel/o102") }}
[% / %]

---

### Oral presentation

---

{{ presentation('iHU9eQV_hiI', '/slides/ding20.pdf', 720, 450) }}