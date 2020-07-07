---
title: "SAU-Net: Efficient 3D Spine MRI Segmentation Using Inter-Slice Attention"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P054 - SAU-Net: Efficient 3D Spine MRI Segmentation Using Inter-Slice Attention

### Yichi Zhang, Lin Yuan, Yujia Wang, Jicong Zhang

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=wlszIiXbfS">Paper</a>
- <a href="https://openreview.net/forum?id=wlszIiXbfS">Reviews</a>
{{ teaser('vqV45k9Wjxc') }}

<p>
    <span class="abstract">
        Accurate segmentation of spine Magnetic Resonance Imaging (MRI) is highly demanded in morphological research, quantitative analysis, and diseases identification, such as spinal canal stenosis, disc herniation and degeneration. However, accurate spine segmentation is challenging because of the irregular shape, artifacts and large variability between slices. To alleviate these problems, spatial information is used for more continuous and accurate segmentation such as by 3D convolutional neural networks (CNN) . However, 3D CNN suffers from higher computational cost, memory cost and risk of over-fitting, especially for medical images where the number of labeled data is limited. To address these problems, we apply the attention mechanism for the utilization of inter-slice information in 3D segmentation tasks based on 2D convolutional networks and propose a spatial attention-based densely connected U-Net (SAU-Net), which consists of Dense U-Net for extraction of intra-slice features and an inter-slice attention module (ISA) to utilize inter-slice information from adjacent slices and refine the segmentation results. Experimental results demonstrate the effectiveness of ISA as well as higher accuracy and efficiency of segmentation results of our method compared with other deep learning methods.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #3  - 9:30 - 11:00 UTC-4 (Tuesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/p054") }}
[% / %]

---


### Poster presentation

---

{{ presentation('tzlzdE_ANuc', '/slides/zhang20b.pdf', 720, 450) }}