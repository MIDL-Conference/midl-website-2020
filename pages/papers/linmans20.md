---
title: "Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P140 - Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks

### Jasper Linmans, Jeroen van der Laak, Geert Litjens

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=hRwB2BTRNu">Paper</a>
- <a href="https://openreview.net/forum?id=hRwB2BTRNu">Reviews</a>
{{ teaser('aK8XWnWOKaE') }}

<p>
    <span class="abstract">
        Successful clinical implementation of deep learning in medical imaging depends, in part, on the reliability of the predictions. Specifically, the system should be accurate for classes seen during training while providing calibrated estimates of uncertainty for abnormalities and unseen classes. To efficiently estimate predictive uncertainty, we propose the use of multi-head convolutional neural networks (M-heads). We compare its performance to related and more prevalent approaches, such as deep ensembles, on the task of out-of-distribution (OOD) detection. To this end, we evaluate models, trained to discriminate normal lymph node tissue from breast cancer metastases, on lymph nodes containing lymphoma. We show the ability to discriminate between the in-distribution lymph node tissue and lymphoma by evaluating the AUROC based on the uncertainty signal. Here, the best performing multi-head CNN (91.7) outperforms both Monte Carlo dropout (86.5) and deep ensembles (86.8). Furthermore, we show that the meta-loss function of M-heads improves OOD detection in terms of AUROC from 87.4 to 88.7.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #5  - 9:30 - 11:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p140") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('aK8XWnWOKaE') }}