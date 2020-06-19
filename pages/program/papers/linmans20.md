---
title: "Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks"
---
<style>
.paper_abstract {
  display: none;
  font-size: 90%;
  line-height: 1.35;
  text-align: justify;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}

.paper_qa {
  display: none;
  line-height: 1.35;
  text-align: center;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}
</style>

{% from "_macros.html" import button %}

# P140 - Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks


##### Jasper Linmans, Jeroen van der Laak, Geert Litjens

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=hRwB2BTRNu">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'Successful clinical implementation of deep learning in medical imaging depends, in part, on the reliability of the predictions. Specifically, the system should be accurate for classes seen during training while providing calibrated estimates of uncertainty for abnormalities and unseen classes. To efficiently estimate predictive uncertainty, we propose the use of multi-head convolutional neural networks (M-heads). We compare its performance to related and more prevalent approaches, such as deep ensembles, on the task of out-of-distribution (OOD) detection. To this end, we evaluate models, trained to discriminate normal lymph node tissue from breast cancer metastases, on lymph nodes containing lymphoma. We show the ability to discriminate between the in-distribution lymph node tissue and lymphoma by evaluating the AUROC based on the uncertainty signal. Here, the best performing multi-head CNN (91.7) outperforms both Monte Carlo dropout (86.5) and deep ensembles (86.8). Furthermore, we show that the meta-loss function of M-heads improves OOD detection in terms of AUROC from 87.4 to 88.7.'
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/P140") }}

---

### Spotlight presentation
