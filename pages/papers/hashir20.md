---
title: "Quantifying the Value of Lateral Views in Deep Learning for Chest X-rays"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P035 - Quantifying the Value of Lateral Views in Deep Learning for Chest X-rays

### Mohammad Hashir, Hadrien Bertrand, Joseph Paul Cohen

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=rY3bgRRHnD">Paper</a>
- <a href="https://openreview.net/forum?id=rY3bgRRHnD">Reviews</a>
{{ teaser('___k6jBuPEo') }}

<p>
    <span class="abstract">
        Most deep learning models in chest X-ray prediction utilize the posteroanterior (PA) view due to the lack of other views available. PadChest is a large-scale chest X-ray dataset that has almost 200 labels and multiple views available. In this work, we use PadChest to explore multiple approaches to merging the PA and lateral views for predicting the radiological labels associated with the X-ray image. We find that different methods of merging the model utilize the lateral view differently. We also find that including the lateral view increases performance for 32 labels in the dataset, while being neutral for the others.      The increase in overall performance is comparable to the one obtained by using only the PA view with twice the amount of patients in the training set.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p035") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('5VjZyIR1224', '/slides/hashir20.pdf', 720, 450) }}