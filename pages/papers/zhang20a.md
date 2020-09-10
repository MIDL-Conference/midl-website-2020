---
title: "Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O006 - Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping

#### Jinwei Zhang, Hang Zhang, Mert Sabuncu, Pascal Spincemaille, Thanh Nguyen, Yi Wang

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=DuWrLOZ27k">Paper</a>
- <a href="https://openreview.net/forum?id=DuWrLOZ27k">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        A learning-based posterior distribution estimation method, Probabilistic Dipole Inversion (PDI), is proposed to solve quantitative susceptibility mapping (QSM) inverse problem in MRI with uncertainty estimation. A deep convolutional neural network (CNN) is used to represent the multivariate Gaussian distribution as the approximated posterior distribution of susceptibility given the input measured field. In PDI, such CNN is firstly trained on healthy subjects\' data with labels by maximizing the posterior Gaussian distribution loss function as used in Bayesian deep learning. When testing on each patient\' data without any label, PDI updates the pre-trained CNN\'s weights in an unsupervised fashion by minimizing the Kullback–Leibler divergence between the approximated posterior distribution represented by CNN and the true posterior distribution given the likelihood distribution from known physical model and pre-defined prior distribution. Based on our experiments, PDI provides additional uncertainty estimation compared to the conventional MAP approach, meanwhile addressing the potential discrepancy issue of CNN when test data deviates from training dataset.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral #4 - Imaging  - 13:30 - 14:30 UTC-4 (Tuesday)<br>Poster Session #4  - 14:30 - 16:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o006") }}
[% / %]

---


### Oral presentation

---

{{ presentation('v9f6DjIbDbI', '/slides/zhang20a.pdf', 720, 450) }}