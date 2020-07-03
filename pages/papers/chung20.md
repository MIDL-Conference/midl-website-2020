---
title: "Low-dose CT Enhancement Network with a Perceptual Loss Function in the Spatial Frequency and Image Domains"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S059 - Low-dose CT Enhancement Network with a Perceptual Loss Function in the Spatial Frequency and Image Domains


### Kevin J. Chung, Roberto Souza, Richard Frayne, Ting-Yim Lee

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=rw5BswbvMB">Paper</a>
        - <a href="https://openreview.net/forum?id=rw5BswbvMB">Reviews</a>
        {{ teaser('') }}

<span class="paper_abstract">
        We propose a dual-domain cascade of U-nets (i.e. a W-net\") operating in both the spatial frequency and image domains to enhance low-dose CT (LDCT) images without the need for proprietary x-ray projection data. The central slice theorem motivated the use of the spatial frequency domain in place of the raw sinogram. Data were obtained from the AAPM Low-dose Grand Challenge. A combination of Fourier space (F) and/or image domain (I) U-nets and W-nets were trained with a multi-scale structural similarity and mean absolute error loss function to denoise filtered back projected (FBP) LDCT images while maintaining perceptual features important for diagnostic accuracy. Deep learning enhancements were superior to FBP LDCT images in quantitative and qualitative performance with the dual-domain W-nets outperforming single-domain U-net cascades. Our results suggest that spatial frequency learning in conjunction with image-domain processing can produce superior LDCT enhancement than image-domain-only networks. 
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 13:30-15:00 UTC-4 - Poster Session #2
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/s059") }} -->

---

### Short paper

---

