---
title: "A Heteroscedastic Uncertainty Model for Decoupling Sources of MRI Image Quality"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}

# O171 - A Heteroscedastic Uncertainty Model for Decoupling Sources of MRI Image Quality


### Richard Shaw, Carole H. Sudre, Sebastien Ourselin, M. Jorge Cardoso

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/forum?id=NnKIdnPXCr">Reviews</a>
        {{ teaser('') }}

<span class="paper_abstract">
        Quality control (QC) of medical images is essential to ensure that downstream analyses such as segmentation can be performed successfully. Currently, QC is predominantly performed visually at significant time and operator cost. We aim to automate the process by formulating a probabilistic network that estimates uncertainty through a heteroscedastic noise model, hence providing a proxy measure of task-specific image quality that is learnt directly from the data. By augmenting the training data with different types of simulated k-space artefacts, we propose a novel cascading CNN architecture based on a student-teacher framework with a weighted adaptive task loss to decouple sources of uncertainty related to different k-space augmentations in an entirely self-supervised manner. This enables us to predict separate uncertainty quantities for the different types of data degradation. While the uncertainty measures reflect the presence and severity of image artefacts, the network also provides the segmentation predictions given the quality of the data. We show that models trained with simulated artefacts provide more informative measures of uncertainty on real-world images and we validate our uncertainty predictions on problematic images identified by human-raters.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 8:30-9:30 ET - Oral Session #5 - Image Generation<br/>WED 9:30-11:00 ET - Poster Session #5
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/o171") }}

---

### Oral presentation

---

