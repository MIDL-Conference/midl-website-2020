---
title: "Fast Mitochondria Detection for Connectomics"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P327 - Fast Mitochondria Detection for Connectomics


### Vincent Casser, Kai Kang, Hanspeter Pfister, Daniel Haehn

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=dGd1Z9CHAg">Paper</a>
        - <a href="https://openreview.net/forum?id=dGd1Z9CHAg">Reviews</a>
        {{ teaser('QKUjkkbjMxg') }}

<span class="paper_abstract">
        High-resolution connectomics data allows for the identification of dysfunctional mitochondria which are linked to a variety of diseases such as autism or bipolar. However, manual analysis is not feasible since datasets can be petabytes in size. We present a fully automatic mitochondria detector based on a modified U-Net architecture that yields high accuracy and fast processing times. We evaluate our method on multiple real-world connectomics datasets, including an improved version of the EPFL mitochondria benchmark. Our results show a Jaccard index of up to 0.90 with inference times lower than 16ms for a 512x512px image tile. This speed is faster than the acquisition speed of modern electron microscopes, enabling mitochondria detection in real-time. Compared to previous work, our detector ranks first for real-time detection and can be used for image alignment. Our data, results, and code are freely available. 
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        WED 13:30-15:00 UTC-4 - Poster Session #6
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p327") }}

---

### Spotlight presentation

---

{{ youtube('QKUjkkbjMxg') }}