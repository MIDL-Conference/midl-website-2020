---
title: "On the effectiveness of GAN generated cardiac MRIs for segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S118 - On the effectiveness of GAN generated cardiac MRIs for segmentation

### Youssef Skandarani, Nathan Painchaud, Pierre-Marc Jodoin, Alain Lalande

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=f9Pl3Qj3_Q">Paper</a>
- <a href="https://openreview.net/forum?id=f9Pl3Qj3_Q">Reviews</a>
{{ teaser('lIVWmPNFG1E') }}

<p>
    <span class="abstract">
        In this work, we propose a Variational Autoencoder (VAE) - Generative Adversarial Networks (GAN) model that can produce highly realistic MRI together with its pixel accurate groundtruth for the application of cine-MR image cardiac segmentation.  On one side of our model is a Variational Autoencoder (VAE) trained to learn the latent representations of cardiac shapes.  On the other side is a GAN that uses  ”SPatially-Adaptive (DE)Normalization” (SPADE) modules to generate realistic MR images tailored to a given anatomical map.  At test time, the sampling of the VAE latent space allows to generate an arbitrary large number of cardiac shapes, which are fed to the GAN that subsequently generates MR images whose cardiac structure fits that of the cardiac shapes.  In other words, our system can generate a large volume of realistic yet labeled cardiac MR images.  We show that segmentation with CNNs trained with our synthetic annotated images gets competitive results compared to traditional techniques.      We also show that combining data augmentation with our GAN-generated images lead to an improvement in the Dice score of up to 12 percent while allowing for better generalization capabilities on  other datasets.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #1  - 9:30 - 11:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/s118") }}
[% / %]

---


### Short paper

---

{{ presentation('iteI5M0BcFY', '/slides/skandarani20.pdf', 720, 450) }}