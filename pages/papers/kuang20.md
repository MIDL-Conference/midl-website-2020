---
title: "Skull-RCNN: A CNN-based network for the skull fracture detection"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P177 - Skull-RCNN: A CNN-based network for the skull fracture detection

### Zhuo Kuang, Xianbo Deng, Li Yu, Hang Zhang, Xian lin, Hui Ma

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=BUQyqaRhNH">Paper</a>
- <a href="https://openreview.net/forum?id=BUQyqaRhNH">Reviews</a>
{{ teaser('LkHM9w7VDFg') }}

<p>
    <span class="abstract">
        Skull fractures, following head trauma, may bring several complications and cause epidural hematomas. Therefore, it is of great significance to locate the fracture in time. However, the manual detection is time-consuming and laborious, and the previous studies for the automatic detection could not achieve the accuracy and robustness for clinical application. In this work, based on the Faster R-CNN, we propose a novel method for more accurate skull fracture detection results, and we name it as the Skull R-CNN. Guiding by the morphological features of the skull, a skeleton-based region proposal method is proposed to make candidate boxes more concentrated in key regions and reduced invalid boxes. With this advantage, the region proposal network in Faster R-CNN is removed for less computation. On the other hand, a novel full resolution feature network is constructed to obtain more precise features to make the model more snesetive to small objects. Experiment results showed that most of skull fractures could be detected correctly by the proposed method in a short time. Compared to the previous works on the skull fracture detecion, Skull R-CNN significantly reduces the less false positives, and keeps a high sensitivity.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #5 *9:30 - 11:00 UTC-4 (Wednesday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p177") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('LkHM9w7VDFg') }}