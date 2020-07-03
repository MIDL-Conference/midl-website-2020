---
title: "End-to-end learning of convolutional neural net and dynamic programming for left ventricle segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P011 - End-to-end learning of convolutional neural net and dynamic programming for left ventricle segmentation

### Nhat M. Nguyen, Nilanjan Ray

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=_4_RPMYWN">Paper</a>
- <a href="https://openreview.net/forum?id=_4_RPMYWN">Reviews</a>
{{ teaser('X0hBhXi-laY') }}

<p>
    <span class="abstract">
        Differentiable programming is able to combine different functions or modules in a data processing pipeline with the goal of applying gradient descent-based end-to-end learning or optimization. A significant impediment to differentiable programming is the non-differentiable nature of some functions.  We propose to overcome this difficulty by using neural networks to approximate such modules.  An approximating neural network provides synthetic gradients (SG) for backpropagation across a non-differentiable module.  Our design is grounded on a well-known theory that gradient of an approximating neural network can approximate a sub-gradient of a weakly differentiable function.  We apply SG to combine convolutional neural  network  (CNN)  with  dynamic  programming  (DP)  in  end-to-end  learning  for  segmenting left ventricle from short axis view of heart MRI. Our experiments show that end-to-end combination of CNN and DP requires fewer labeled images to achieve a significantly better segmentation accuracy than using only CNN.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #4 *14:30 - 16:00 UTC-4 (Tuesday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p011") }} -->
[% / %]

---

### Spotlight presentation

---

{{ youtube('X0hBhXi-laY') }}