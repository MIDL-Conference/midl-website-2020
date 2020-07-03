---
title: "Domain adaptation model for retinopathy detection from cross-domain OCT images"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P334 - Domain adaptation model for retinopathy detection from cross-domain OCT images


### Jing Wang, Yiwei Chen, Wanyue Li, Wen Kong, Yi He, Chunhui Jiang, Guohua Shi

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=h5z-R09QRm">Paper</a>
        - <a href="https://openreview.net/forum?id=h5z-R09QRm">Reviews</a>
        {{ teaser('Noi1JIBsITk') }}

<span class="paper_abstract">
        A deep neural network (DNN) can assist in retinopathy screening by automatically classifying patients into normal and abnormal categories according to optical coherence tomography (OCT) images. Typically, OCT images captured from different devices show heterogeneous appearances because of different scan settings; thus, the DNN model trained from one domain may fail if applied directly to a new domain. As data labels are difficult to acquire, we proposed a generative adversarial network-based domain adaptation model to address the cross-domain OCT images classification task, which can extract invariant and discriminative characteristics shared by different domains without incurring additional labeling cost. A feature generator, a Wasserstein distance estimator, a domain discriminator, and a classifier were included in the model to enforce the extraction of domain invariant representations. We applied the model to OCT images as well as public digit images. Results show that the model can significantly improve the classification accuracy of cross-domain images.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 9:30-11:00 UTC-4 - Poster Session #5
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p334") }} -->

---

### Spotlight presentation

---

{{ youtube('Noi1JIBsITk') }}