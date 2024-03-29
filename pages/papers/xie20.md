---
title: "Beyond Classification: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O305 - Beyond Classification: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning

#### Chensu Xie, Hassan Muhammad, Chad M. Vanderbilt, Raul Caso, Dig Vijay Kumar Yarlagadda, Gabriele Campanella, Thomas J. Fuchs

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="http://proceedings.mlr.press/v121/xie20a.html">Proceedings</a>
- <a href="https://openreview.net/pdf?id=aqOfnZx4-N">PDF</a>
- <a href="https://openreview.net/forum?id=aqOfnZx4-N">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        An emerging technology in cancer care and research is the use of histopathology whole slide images (WSI). Leveraging computation methods to aid in WSI assessment poses unique challenges. WSIs, being extremely high resolution giga-pixel images, cannot be directly processed by convolutional neural networks (CNN) due to huge computational cost. For this reason, state-of-the-art methods for WSI analysis adopt a two-stage approach where the training of a tile encoder is decoupled from the tile aggregation. This results in a trade-off between learning diverse and discriminative features. In contrast, we propose end-to-end part learning (EPL) which is able to learn diverse features while ensuring that learned features are discriminative. Each WSI is modeled as consisting of $k$ groups of tiles with similar features, defined as parts. A loss with respect to the slide label is backpropagated through an integrated CNN model to $k$ input tiles that are used to represent each part. Our experiments show that EPL is capable of clinical grade prediction of prostate and basal cell carcinoma. Further, we show that diverse discriminative features produced by EPL succeeds in multi-label classification of lung cancer architectural subtypes. Beyond classification, our method provides rich information of slides for high quality clinical decision support.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #3 - Networks for Histology  - 8:30 - 9:30 UTC-4 (Tuesday)<br>Poster Session #3  - 9:30 - 11:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o305") }}
[% / %]

---


### Oral presentation

---

{{ presentation('Iees9O3TiCo', '/slides/xie20.pdf', 720, 450) }}