---
title: "4D Semantic Cardiac Magnetic Resonance Image Synthesis on XCAT Anatomical Model"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P200 - 4D Semantic Cardiac Magnetic Resonance Image Synthesis on XCAT Anatomical Model

### Samaneh Abbasi-Sureshjani, Sina Amirrajab, Cristian Lorenz, Juergen Weese, Josien Pluim, Marcel Breeuwer

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=tRdOL-DcPA">Paper</a>
- <a href="https://openreview.net/forum?id=tRdOL-DcPA">Reviews</a>
{{ teaser('w5fCCvv-94w') }}

<p>
    <span class="abstract">
        We  propose  a  hybrid  controllable  image  generation  method  to  synthesize  anatomically meaningful 3D+t labeled Cardiac Magnetic Resonance (CMR) images.  Our hybrid method takes the mechanistic 4D eXtended CArdiac Torso (XCAT) heart model as the anatomical  ground  truth  and  synthesizes  CMR  images via a data-driven  Generative  Adversarial Network (GAN). We employ the state-of-the-art SPatially Adaptive De-normalization (SPADE) technique for conditional image synthesis to preserve the semantic spatial information  of  ground  truth  anatomy.  Using  the  parameterized  motion  model  of  the  XCAT heart,  we generate labels for 25 time frames of the heart for one cardiac cycle at 18 locations  for  the  short  axis  view.   Subsequently,  realistic  images  are  generated  from  these labels,  with  modality-specific  features  that  are  learned  from  real  CMR  image  data.   We  demonstrate that style transfer from another cardiac image can be accomplished by using a  style  encoder  network.   Due  to  the  flexibility  of  XCAT  in  creating  new  heart  models, this  approach  can  result  in  a  realistic  virtual  population  to  address  different  challenges the medical image analysis research community is facing such as expensive data collection. Our proposed method has a great potential to synthesize 4D controllable CMR images with annotations and adaptable styles to be used in various supervised multi-site, multi-vendor applications in medical image analysis.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #2 *13:30 - 15:00 UTC-4 (Monday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p200") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('w5fCCvv-94w') }}