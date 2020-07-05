---
title: "A Deep Learning based Fast Signed Distance Map Generation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S033 - A Deep Learning based Fast Signed Distance Map Generation

### Zihao Wang, Clair Vandersteen, Thomas Demarcy, Dan Gnansia, Charles Raffaelli, Nicolas Guevara, Hervé Delingette

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=b2N5ZuEouu">Paper</a>
- <a href="https://openreview.net/forum?id=b2N5ZuEouu">Reviews</a>
{{ teaser('BeWMzeZIjEI') }}

<p>
    <span class="abstract">
        Signed distance map (SDM) is a common representation of surfaces in medical image analysis and machine learning. The computational complexity of SDM for 3D parametric shapes is often a bottleneck in many applications, thus limiting their interest. In this paper, we propose a learning-based SDM generation neural network which is demonstrated on a tridimensional cochlea shape model parameterized by 4 shape parameters.      The proposed SDM Neural Network generates a cochlea signed distance map depending on four input parameters and we show that the deep learning approach leads to a 60 fold improvement in the time of computation compared to more classical SDM generation methods. Therefore, the proposed approach achieves a good trade-off between accuracy and efficiency. 
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

{{ button("Access paper channel", "https://chat.midl.io/channel/s033") }}
[% / %]

---

### Short paper

---

{{ presentation('_o8KzH0ll3o', '/slides/wang20a.pdf', 720, 450) }}