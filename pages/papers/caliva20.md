---
title: "Breaking Speed Limits with Simultaneous Ultra-Fast MRI Reconstruction and Tissue Segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P239 - Breaking Speed Limits with Simultaneous Ultra-Fast MRI Reconstruction and Tissue Segmentation

### Francesco Calivá, Rutwik Shah, Upasana Upadhyay Bharadwaj, Sharmila Majumdar, Peder Larson, Valentina Pedoia

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=sXONwA0ex">Paper</a>
- <a href="https://openreview.net/forum?id=sXONwA0ex">Reviews</a>
{{ teaser('vnACGxIEQwE') }}

<p>
    <span class="abstract">
        Magnetic Resonance Image (MRI) acquisition, reconstruction and tissue segmentation are usually considered separate problems. This can be limiting when it comes to rapidly extracting relevant clinical parameters. In many applications, availability of reconstructed images with high fidelity may not be a priority as long as biomarker extraction is reliable and feasible. Built upon this concept, we demonstrate that it is possible to perform tissue segmentation directly from highly undersampled k-space and obtain quality results comparable to those in fully-sampled scenarios. We propose \'TB-recon\', a 3D task-based reconstruction framework. TB-recon simultaneously reconstructs MRIs from raw data and segments tissues of interest. To do so, we devised a network architecture with a shared encoding path and two task-related decoders where features flow among tasks. We deployed TB-recon on a set of (up to $24\times$) retrospectively undersampled MRIs from the Osteoarthritis Initiative dataset, where we automatically segmented knee cartilage and menisci. An experimental study was conducted showing the superior performance of the proposed method over a combination of a standard MRI reconstruction and segmentation method, as well as alternative deep learning based solutions. In addition, our ablation study highlighted the importance of skip connections among the decoders for the segmentation task. Ultimately, we conducted a reader study, where two musculoskeletal radiologists assessed the proposed model’s reconstruction performance.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #4  - 14:30 - 16:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/p239") }}
[% / %]

---

### Spotlight presentation

---

{{ presentation('T6Ru9B5Eubc', '/slides/caliva20.pdf', 720, 450) }}