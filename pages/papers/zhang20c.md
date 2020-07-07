---
title: "Direct estimation of fetal head circumference from ultrasound images based on regression CNN"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P222 - Direct estimation of fetal head circumference from ultrasound images based on regression CNN

### Jing Zhang, Caroline Petitjean, Pierre Lopez, Samia Ainouz

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=RwYqA6AjS">Paper</a>
- <a href="https://openreview.net/forum?id=RwYqA6AjS">Reviews</a>
{{ teaser('y-iXek-lMjE') }}

<p>
    <span class="abstract">
        The measurement of fetal head circumference (HC) is performed throughout the pregnancy as a key biometric to monitor fetus growth. This measurement is performed on ultrasound images, via the manual fitting of an ellipse. The operation is operator-dependent and as such prone to intra and inter-variability error. There have been attempts to design automated segmentation algorithms to segment fetal head, especially based on deep encoding-decoding architectures. In this paper, we depart from this idea and propose to leverage the ability of convolutional neural networks (CNN) to directly measure the head circumference, without having to resort to handcrafted features or manually labeled segmented images. The intuition behind this idea is that the CNN will  learn itself to localize and identify the head contour. Our approach is experimented on the public HC18 dataset, that contains images of all trimesters of the pregnancy. We investigate various architectures and three losses suitable for regression. While room for improvement is left, encouraging results show that it might be possible in the future to directly estimate the HC - without the need for a large dataset of manually segmented ultrasound images. This approach might be extended to other applications where segmentation is just an intermediate step to the computation of biomarkers.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p222") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('9NR127iB94A', '/slides/zhang20c.pdf', 720, 450) }}