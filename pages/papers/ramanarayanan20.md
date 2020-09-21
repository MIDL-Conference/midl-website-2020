---
title: "MAC-ReconNet: A Multiple Acquisition Context based Convolutional Neural Network for MR Image Reconstruction using Dynamic Weight Prediction"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O056 - MAC-ReconNet: A Multiple Acquisition Context based Convolutional Neural Network for MR Image Reconstruction using Dynamic Weight Prediction

#### Sriprabha Ramanarayanan, Balamurali Murugesan, Keerthi Ram, Mohanasankar Sivaprakasam

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="http://proceedings.mlr.press/v121/ramanarayanan20a.html">Proceedings</a>
- <a href="https://openreview.net/pdf?id=pMHk_HIZf7">PDF</a>
- <a href="https://openreview.net/forum?id=pMHk_HIZf7">Reviews</a>
{{ teaser('_rzsMOcyV3o') }}

<p>
    <span class="abstract">
        Convolutional Neural network based MR reconstruction methods have shown to provide fast and high quality reconstructions.  A primary drawback with a CNN-based model is that it lacks flexibility and can effectively operate only for a specific acquisition context limiting practical applicability.  By acquisition context, we mean a specific combination of three input settings considered namely, the anatomy under study, undersampling mask pattern and acceleration  factor  for  undersampling.   The  model  could be  trained  jointly  on  images  combining multiple contexts.  However the model does not meet the performance of context specific models nor extensible to contexts unseen at train time.  This necessitates a modification to the existing architecture in generating context specific weights so as to incorporate flexibility to multiple contexts. We propose a multiple acquisition context based network, called MAC-ReconNet for MRI reconstruction, flexible to multiple acquisition contexts and generalizable to unseen contexts for applicability in real scenarios. The proposed network has an MRI reconstruction module and a dynamic weight prediction (DWP) module.  The DWP module takes the corresponding acquisition context information  as  input  and  learns  the context-specific weights  of  the  reconstruction module which changes dynamically with context at run time.  We show that the proposed approach can handle multiple contexts  based on Cardiac and Brain datasets, Gaussian and Cartesian undersampling patterns and five acceleration factors. The proposed network outperforms the naive  jointly  trained model  and  gives  competitive results  with  the  context-specific  models both quantitatively and qualitatively.  We also demonstrate the generalizability of our model by testing on contexts unseen at train time.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #5 - Image Generation  - 8:30 - 9:30 UTC-4 (Wednesday)<br>Poster Session #5  - 9:30 - 11:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o056") }}
[% / %]

---

## Runner-up for best paper Award
### Oral presentation

---

{{ presentation('HQ1ioGUwhcE', '/slides/ramanarayanan20.pdf', 720, 450) }}