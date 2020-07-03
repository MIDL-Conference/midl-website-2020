---
title: "Pathology GAN: Learning deep representations of cancer tissue"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P150 - Pathology GAN: Learning deep representations of cancer tissue


### Adalberto Claudio Quiros, Roderick Murray-Smith, Ke Yuan

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=CwgSEEQkad">Paper</a>
        - <a href="https://openreview.net/forum?id=CwgSEEQkad">Reviews</a>
        {{ teaser('wGx78e1mHQQ') }}

<span class="paper_abstract">
        We apply Generative Adversarial Networks (GANs) to the domain of digital pathology. Current machine learning research for digital pathology focuses on diagnosis, but we suggest a different approach and advocate that generative models could drive forward the understanding of morphological characteristics of cancer tissue. In this paper, we develop a framework which allows GANs to capture key tissue features and uses these characteristics to give structure to its latent space. To this end, we trained our model on 249K H&E breast cancer tissue images.          We show that our model generates high quality images, with a Frechet Inception Distance (FID) of 16.65. We additionally assess the quality of the images with cancer tissue characteristics (e.g. count of cancer, lymphocytes, or stromal cells), using quantitative information to calculate the FID and showing consistent performance of 9.86. Additionally, the latent space of our model shows an interpretable structure and allows semantic vector operations that translate into tissue feature transformations. Furthermore, ratings from two expert pathologists found no significant difference between our generated tissue images from real ones.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 UTC-4 - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p150") }}

---

### Spotlight presentation

---

{{ presentation('RlBo4lAWtvM', '/slides/quiros20.pdf', 720, 450) }}