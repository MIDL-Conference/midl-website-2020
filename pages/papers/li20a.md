---
title: "Generating Fundus Fluorescence Angiography Images from Structure Fundus Images Using Generative Adversarial Networks"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P333 - Generating Fundus Fluorescence Angiography Images from Structure Fundus Images Using Generative Adversarial Networks

### Wanyue Li, Wen Kong, Yiwei Chen, Jing Wang, Yi He, Guohua Shi, Guohua Deng

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=qhZM390B4">Paper</a>
- <a href="https://openreview.net/forum?id=qhZM390B4">Reviews</a>
{{ teaser('Lk5lHf9fvDw') }}

<p>
    <span class="abstract">
        Fluorescein angiography can provide a map of retinal vascular structure and function, which is commonly used in ophthalmology diagnosis, however, this imaging modality may pose risks of harm to the patients. To help physicians reduce the potential risks of diagnosis, an image translation method is adopted. In this work, we proposed a conditional generative adversarial network (GAN)-based method to directly learn the mapping relationship between structure fundus images and fundus fluorescence angiography (FFA) images. Moreover, local saliency maps, which define each pixel’s importance, are used to define a novel saliency loss in the GAN cost function. This facilitates more accurate learning of small-vessel and fluorescein leakage features. The proposed method was validated on our dataset and the publicly available Isfahan MISP dataset with the metrics of peak signal-to-noise ratio (PSNR) and structural similarity (SSIM). The experimental results indicate that the proposed method can accurately generate both retinal vascular and fluorescein leakage structures, which has great practical significance for clinical diagnosis and analysis.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p333") }}
[% / %]

---


### Poster presentation

---

{{ presentation('Iqo8KB32IxY', '/slides/li20a.pdf', 720, 450) }}