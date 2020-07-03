---
title: "Assessing the validity of saliency maps for abnormality localization in medical imaging"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S107 - Assessing the validity of saliency maps for abnormality localization in medical imaging

### Nishanth Thumbavanam Arun, Nathan Gaw, Praveer Singh, Ken Chang, Katharina Viktoria Hoebel, Jay Patel, Mishka Gidwani, Jayashree Kalpathy-Cramer

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=02X3kfP6W4">Paper</a>
- <a href="https://openreview.net/forum?id=02X3kfP6W4">Reviews</a>
{{ teaser('8V99wNHzJbQ') }}

<p>
    <span class="abstract">
        Saliency maps have become a widely used method to assess which areas of the input image are most pertinent to the prediction of a trained neural network.  However, in the context of medical imaging, there is no study to our knowledge that has examined the efficacy of these techniques and quantified them using overlap with ground truth bounding boxes. In this work, we explored the credibility of the various existing saliency map methods on the RSNA  Pneumonia  dataset. We  found  that  GradCAM  was  the  most  sensitive  to  model parameter and label randomization, and was highly agnostic to model architecture.
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

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/s107") }} -->
[% / %]

---

### Short paper

---

{{ presentation('8V99wNHzJbQ', '/slides/arun20.pdf', 720, 450) }}