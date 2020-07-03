---
title: "Vispi: Automatic Visual Perception and Interpretation of Chest X-rays"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S276 - Vispi: Automatic Visual Perception and Interpretation of Chest X-rays


### Xin Li, Rui Cao, Dongxiao Zhu

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=otswIbmgYA">Paper</a>
        - <a href="https://openreview.net/forum?id=otswIbmgYA">Reviews</a>
        {{ teaser('-un_xVu-hu0') }}

<span class="paper_abstract">
        Computer-aided medical image visual perception and interpretation with deep learning remain a challenging task, due to the lack of high-quality annotated image-report pairs and tailor-made generative models for sufficient extraction and exploitation of localized semantic features associated with abnormalities. To tackle these challenges, we present Vispi, an automatic medical image interpretation system, which first annotates an image via classifying and localizing common thoracic diseases with visual support and then followed by report generation from an attentive LSTM model. Analyzing an open IU X-ray dataset, we demonstrate a superior performance of Vispi in disease classification, localization and report generation using automatic performance evaluation metrics ROUGE and CIDEr.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 13:30-15:00 UTC-4 - Poster Session #6
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s276") }}

---

### Short paper

---

{{ presentation('-un_xVu-hu0', '/slides/li20c.pdf', 720, 450) }}