---
title: "Accurate Detection of Out of Body Segments in Surgical Video using Semi-Supervised Learning"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P157 - Accurate Detection of Out of Body Segments in Surgical Video using Semi-Supervised Learning


### Maya Zohar, Omri Bar, Daniel Neimark, Gregory D. Hager, Dotan Asselmann

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=k-ANsPQJxY">Paper</a>
        - <a href="https://openreview.net/forum?id=k-ANsPQJxY">Reviews</a>
        {{ teaser('2-c8hAMEAEo') }}

<span class="paper_abstract">
        Large labeled datasets are an important precondition for deep learning models to achieve state-of-the-art results in computer vision tasks. In the medical imaging domain, privacy concerns have limited the rate of adoption of artificial intelligence methodologies into clinical practice. To alleviate such concerns, and increase comfort levels while sharing and storing surgical video data, we propose a high accuracy method for rapid removal and anonymization of out-of-body and non-relevant surgery segments. Training a deep model to detect out-of-body and non-relevant segments in surgical videos requires suitable labeling. Since annotating surgical videos with per-second relevancy labeling is a tedious task, our proposed framework initiates the learning process from a weakly labeled noisy dataset and iteratively applies Semi-Supervised Learning (SSL) to re-annotate the training data samples. Evaluating our model, on an independent test set, shows a mean detection accuracy of above 97% after several training-annotating iterations. Since our final goal is achieving out-of-body segments detection for anonymization, we evaluate our ability to detect these segments at a high demanding recall of 97%, which leads to a precision of 83.5%. We believe this approach can be applied to similar related medical problems, in which only a coarse set of relevancy labels exists, currently limiting the possibility for supervision training.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 ET - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p157") }}

---

### Spotlight presentation

---

{{ youtube('2-c8hAMEAEo') }}