---
title: "A Deep Learning Approach for Motion Forecasting Using 4D OCT Data"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S156 - A Deep Learning Approach for Motion Forecasting Using 4D OCT Data

### Marcel Bengs, Nils Gessert, Alexander Schlaefer

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=WVd56kgRV">Paper</a>
- <a href="https://openreview.net/forum?id=WVd56kgRV">Reviews</a>
{{ teaser('32BZ5eOHzTk') }}

<p>
    <span class="abstract">
        Forecasting motion of a specific target object is a common problem for surgical interventions, e.g. for localization of a target region, guidance for surgical interventions, or motion compensation. Optical coherence tomography (OCT) is an imaging modality with a high spatial and temporal resolution. Recently, deep learning methods have shown promising performance for OCT-based motion estimation based on two volumetric images. We extend this approach and investigate whether using a time series of volumes enables motion forecasting. We propose 4D spatio-temporal deep learning for end-to-end motion forecasting and estimation using a stream of OCT volumes. We design and evaluate five different 3D and 4D deep learning methods using a tissue data set. Our best performing 4D method  achieves motion forecasting with an overall average correlation coefficient of 97.41%, while also improving motion estimation performance by a factor of 2.5 compared to a previous 3D approach. 
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

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/s156") }} -->
[% / %]

---

### Short paper

---

{{ presentation('32BZ5eOHzTk', '/slides/bengs20.pdf', 720, 450) }}