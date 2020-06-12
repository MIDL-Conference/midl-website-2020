---
title: "DRMIME: Differentiable Mutual Information and Matrix Exponential for Multi-Resolution Image Registration"
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

# [DRMIME: Differentiable Mutual Information and Matrix Exponential for Multi-Resolution Image Registration](https://chat.midl.io/channel/P064)

##### Abhishek Nan,Matthew Tennant,Uriel Rubin,Nilanjan Ray
###### Keywords: KEYWORDS

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=Q0Bm5e6dkW">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        In this work, we present a novel unsupervised image registration algorithm. It is differentiable end-to-end and can be used for both multi-modal and mono-modal registration. This is done using mutual information (MI) as a metric. The novelty here is that rather than using traditional ways of approximating MI which are often histogram based, we use a neural estimator called MINE and supplement it with matrix exponential for transformation matrix computation. The introduction of MINE tackles some of the drawbacks of histogram based MI computation and matrix exponential makes the optimization process smoother. We also introduce the idea of a multi-resolution loss, which makes the optimization process faster and more robust. This leads to improved results as compared to the standard algorithms available out-of-the-box in state-of-the-art image registration toolboxes, both in terms of time as well as registration accuracy, which we empirically demonstrate on publicly available datasets.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

---

### Spotlight presentation
