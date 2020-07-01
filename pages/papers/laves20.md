---
title: "Well-Calibrated Regression Uncertainty in Medical Imaging with Deep Learning"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# O212 - Well-Calibrated Regression Uncertainty in Medical Imaging with Deep Learning


### Max-Heinrich Laves, Sontje Ihler, Jacob F. Fast, Lüder A. Kahrs, Tobias Ortmaier

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/forum?id=CecZ_0t79q">Reviews</a>
        {{ teaser('Wo6mZE3dBWI') }}

<span class="paper_abstract">
        The consideration of predictive uncertainty in medical imaging with deep learning is of utmost importance.      We apply estimation of predictive uncertainty by variational Bayesian inference with Monte Carlo dropout to regression tasks and show why predictive uncertainty is systematically underestimated.      We suggest to use $ \sigma $ scaling with a single scalar value; a simple, yet effective calibration method for both aleatoric and epistemic uncertainty.      The performance of our approach is evaluated on a variety of common medical regression data sets using different state-of-the-art convolutional network architectures.      In all experiments, $ \sigma $ scaling is able to reliably recalibrate predictive uncertainty, surpassing more complex calibration methods.      It is easy to implement and maintains the accuracy.      Well-calibrated uncertainty in regression allows robust rejection of unreliable predictions or detection of out-of-distribution samples.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 8:30-9:30 ET - Oral Session #1 - Uncertainty<br/>MON 9:30-11:00 ET - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/o212") }}

---

### Oral presentation

---

{{ youtube('Wo6mZE3dBWI') }}