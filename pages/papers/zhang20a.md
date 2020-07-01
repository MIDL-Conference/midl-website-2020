---
title: "Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}

# O006 - Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping


### Jinwei Zhang, Hang Zhang, Mert Sabuncu, Pascal Spincemaille, Thanh Nguyen, Yi Wang

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/forum?id=DuWrLOZ27k">Reviews</a>
        {{ teaser('') }}

<span class="paper_abstract">
        A learning-based posterior distribution estimation method, Probabilistic Dipole Inversion (PDI), is proposed to solve quantitative susceptibility mapping (QSM) inverse problem in MRI with uncertainty estimation. A deep convolutional neural network (CNN) is used to represent the multivariate Gaussian distribution as the approximated posterior distribution of susceptibility given the input measured field. In PDI, such CNN is firstly trained on healthy subjects\' data with labels by maximizing the posterior Gaussian distribution loss function as used in Bayesian deep learning. When testing on each patient\' data without any label, PDI updates the pre-trained CNN\'s weights in an unsupervised fashion by minimizing the Kullback–Leibler divergence between the approximated posterior distribution represented by CNN and the true posterior distribution given the likelihood distribution from known physical model and pre-defined prior distribution. Based on our experiments, PDI provides additional uncertainty estimation compared to the conventional MAP approach, meanwhile addressing the potential discrepancy issue of CNN when test data deviates from training dataset.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        TUE 13:30-14:30 ET - Oral #4 - Imaging<br/>TUE 14:30-16:00 ET - Poster Session #4
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/o006") }}

---

### Oral presentation

---

