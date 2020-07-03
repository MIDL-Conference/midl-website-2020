---
title: "Robust Image Segmentation Quality Assessment"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S093 - Robust Image Segmentation Quality Assessment


### Leixin Zhou, Wenxiang Deng, Xiaodong Wu

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=nyhZXiaotm">Paper</a>
        - <a href="https://openreview.net/forum?id=nyhZXiaotm">Reviews</a>
        {{ teaser('PgTTxpfsQvw') }}

<span class="paper_abstract">
        Deep learning based image segmentation methods have achieved great success, even having human-level accuracy in some applications. However, due to the black box nature of deep learning, the best method may fail in some situations. Thus predicting segmentation quality without ground truth would be very crucial especially in clinical practice. Recently, people proposed to train neural networks to estimate the quality score by regression. Although it can achieve promising prediction accuracy, the network suffers robustness problem, e.g. it is vulnerable to adversarial attacks. In this paper, we propose to alleviate this problem by utilizing the difference between the input image and the reconstructed image, which is conditioned on the segmentation to be assessed, to lower the chance to overfit to the undesired image features  from the original input image, and thus to increase the robustness. Results on ACDC17 dataset demonstrated our method is promising.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 13:30-15:00 UTC-4 - Poster Session #2
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s093") }}

---

### Short paper

---

{{ presentation('PgTTxpfsQvw', '/slides/zhou20.pdf', 720, 450) }}