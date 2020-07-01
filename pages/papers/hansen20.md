---
title: "Tackling the Problem of Large Deformations in Deep Learning Based Medical Image Registration Using Displacement Embeddings"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S155 - Tackling the Problem of Large Deformations in Deep Learning Based Medical Image Registration Using Displacement Embeddings


### Lasse Hansen, Mattias P. Heinrich

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=kPBUZluVq">Paper</a>
        - <a href="https://openreview.net/forum?id=kPBUZluVq">Reviews</a>
        {{ teaser('2uJ_H0G1f-0') }}

<span class="paper_abstract">
        Though, deep learning based medical image registration is currently starting to show promising advances, often, it still fells behind conventional frameworks in terms of reg- istration accuracy. This is especially true for applications where large deformations exist, such as registration of interpatient abdominal MRI or inhale-to-exhale CT lung registra- tion. Most current works use U-Net-like architectures to predict dense displacement fields from the input images in different supervised and unsupervised settings. We believe that the U-Net architecture itself to some level limits the ability to predict large deformations (even when using multilevel strategies) and therefore propose a novel approach, where the input images are mapped into a displacement space and final registrations are reconstructed from this embedding. Experiments on inhale-to-exhale CT lung registration demonstrate the ability of our architecture to predict large deformations in a single forward path through our network (leading to errors below 2 mm).
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 9:30-11:00 UTC-4 - Poster Session #5
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s155") }}

---

### Short paper

---

{{ youtube('2uJ_H0G1f-0') }}