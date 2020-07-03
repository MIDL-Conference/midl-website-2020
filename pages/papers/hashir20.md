---
title: "Quantifying the Value of Lateral Views in Deep Learning for Chest X-rays"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P035 - Quantifying the Value of Lateral Views in Deep Learning for Chest X-rays


### Mohammad Hashir, Hadrien Bertrand, Joseph Paul Cohen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=rY3bgRRHnD">Paper</a>
        - <a href="https://openreview.net/forum?id=rY3bgRRHnD">Reviews</a>
        {{ teaser('___k6jBuPEo') }}

<span class="paper_abstract">
        Most deep learning models in chest X-ray prediction utilize the posteroanterior (PA) view due to the lack of other views available. PadChest is a large-scale chest X-ray dataset that has almost 200 labels and multiple views available. In this work, we use PadChest to explore multiple approaches to merging the PA and lateral views for predicting the radiological labels associated with the X-ray image. We find that different methods of merging the model utilize the lateral view differently. We also find that including the lateral view increases performance for 32 labels in the dataset, while being neutral for the others.      The increase in overall performance is comparable to the one obtained by using only the PA view with twice the amount of patients in the training set.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 13:30-15:00 UTC-4 - Poster Session #2
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p035") }} -->

---

### Spotlight presentation

---

{{ youtube('___k6jBuPEo') }}