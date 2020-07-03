---
title: "Deep learning-based parameter mapping for joint relaxation and diffusion tensor MR Fingerprinting"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P182 - Deep learning-based parameter mapping for joint relaxation and diffusion tensor MR Fingerprinting


### Carolin M. Pirkl, Pedro A. Gómez, Ilona Lipp, Guido Buonincontri, Miguel Molina-Romero, Anjany Sekuboyina, Diana Waldmannstetter, Jonathan Dannenberg, Sebastian Endt, Alberto Merola, Joseph R. Whittaker, Valentina Tomassini, Michela Tosetti, Derek K. Jones, Bjoern H. Menze, Marion I. Menzel

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=wthvY6Y9e">Paper</a>
        - <a href="https://openreview.net/forum?id=wthvY6Y9e">Reviews</a>
        {{ teaser('SMIQgihtEWE') }}

<span class="paper_abstract">
        Magnetic Resonance Fingerprinting (MRF) enables the simultaneous quantification of multiple properties of biological tissues. It relies on a pseudo-random acquisition and the matching of acquired signal evolutions to a precomputed dictionary. However, the dictionary is not scalable to higher-parametric spaces, limiting MRF to the simultaneous mapping of only a small number of parameters (proton density, T1 and T2 in general). Inspired by diffusion-weighted SSFP imaging, we present a proof-of-concept of a novel MRF sequence with embedded diffusion-encoding gradients along all three axes to efficiently encode orientational diffusion and T1 and T2 relaxation. We take advantage of a convolutional neural network (CNN) to reconstruct multiple quantitative maps from this single, highly undersampled acquisition. We bypass expensive dictionary matching by learning the implicit physical relationships between the spatiotemporal MRF data and the T1, T2 and diffusion tensor parameters. The predicted parameter maps and the derived scalar diffusion metrics agree well with state-of-the-art reference protocols. Orientational diffusion information is captured as seen from the estimated primary diffusion directions. In addition to this, the joint acquisition and reconstruction framework proves capable of preserving tissue abnormalities in multiple sclerosis lesions.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 UTC-4 - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p182") }} -->

---

### Spotlight presentation

---

{{ youtube('SMIQgihtEWE') }}