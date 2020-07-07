---
title: "Spatiotemporal motion prediction in free-breathing liver scans via a recurrent multi-scale encoder decoder"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S057 - Spatiotemporal motion prediction in free-breathing liver scans via a recurrent multi-scale encoder decoder

### Liset Vazquez Romaguera, Rosalie Plantefeve, Samuel Kadoury

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=901HZmWDHH">Paper</a>
- <a href="https://openreview.net/forum?id=901HZmWDHH">Reviews</a>
{{ teaser('zjI5M5zf8do') }}

<p>
    <span class="abstract">
        In this work we propose a multi-scale recurrent encoder-decoder architecture to predict the breathing induced organ deformation in future frames. The model was trained end-to-end from input images to predict a sequence of motion labels. Targets were created by quantizing the motion fields obtained from deformable image registration. We propose a multi-scale feature extraction scheme in the spatial encoder which processes the input at different resolutions. We report results using MRI free-breathing acquisitions from 12 volunteers. Experiments were aimed at investigating the proposed multi-scale design and the effect of increasing the number of predicted frames on the overall accuracy of the model. The proposed model was able to predict vessel positions in the next temporal image with a mean accuracy of 2.03 (2.89) mm showing increased performance in comparison with state-of-the-art approaches.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #2  - 13:30 - 15:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/s057") }}
[% / %]

---


### Short paper

---

{{ presentation('Yf8q0Nq9QQc', '/slides/romaguera20.pdf', 720, 450) }}