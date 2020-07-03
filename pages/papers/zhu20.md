---
title: "Image Translation by Latent Union of Subspaces for Cross-Domain Plaque Segmentation"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S266 - Image Translation by Latent Union of Subspaces for Cross-Domain Plaque Segmentation

### Yingying Zhu, Daniel C. Elton, Sungwon Lee, Perry J. Pickhardt, Ronald M. Summers

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=qJxBTPyVYA">Paper</a>
- <a href="https://openreview.net/forum?id=qJxBTPyVYA">Reviews</a>
{{ teaser('ZD1pL8D2oIE') }}

<p>
    <span class="abstract">
        Calcified plaque in the aorta and pelvic arteries is associated with coronary artery calcification and is a strong predictor of heart attack. Current calcified plaque detection models show poor generalizeability to different domains (ie. pre-contrast vs. post-contrast CT scans). Many recent works have shown how cross domain object detection can be improved using an image translation model which translates between domains using a single shared latent space. However, while current image translation models do a good job preserving global/intermediate level structures they often have trouble preserving tiny structures. In medical imaging applications, preserving small structures is important since these structures can carry information which is highly relevant for disease diagnosis. Recent works on image reconstruction show that complex real-world images are better reconstructed using a union of subspaces approach. Since small image patches are used to train the image translation model, it makes sense to enforce that each patch be represented by a linear combination of subspaces which may correspond to the different parts of the body present in that patch. Motivated by this, we propose an image translation network using a shared union of subspaces constraint and show our approach preserves subtle structures (plaques) better than the conventional method. We further applied our method to a cross domain plaque detection task and show significant improvement compared to the state-of-the art method.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #6 *13:30 - 15:00 UTC-4 (Wednesday)*
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/s266") }} -->
[% / %]

---

### Short paper

---

{{ youtube('ZD1pL8D2oIE') }}