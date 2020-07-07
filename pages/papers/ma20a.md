---
title: "How Distance Transform Maps Boost Segmentation CNNs: An Empirical Study"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P002 - How Distance Transform Maps Boost Segmentation CNNs: An Empirical Study

### Jun Ma, Zhan Wei, Yiwen Zhang, Yixin Wang, Rongfei Lv, Cheng Zhu, Gaoxiang Chen, Jianan Liu, Chao Peng, Lei Wang, Yunpeng Wang, Jianan Chen

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=hM4pNbXWst">Paper</a>
- <a href="https://openreview.net/forum?id=hM4pNbXWst">Reviews</a>
{{ teaser('G23FofuAOFM') }}

<p>
    <span class="abstract">
        Incorporating distance transform maps of ground truth into segmentation CNNs has been an interesting new trend in the last year. Despite many great works leading to improvements on a variety of segmentation tasks, the comparison among these methods has not been well studied.      In this paper, our \emph{first contribution} is to summarize the latest developments of these methods in the 3D medical segmentation field.      The \emph{second contribution} is that we systematically evaluated five benchmark methods on two representative public datasets.      These experiments highlight that all the five benchmark methods can bring performance gains to baseline V-Net. However, the implementation details have a noticeable impact on the performance, and not all the methods hold the benefits in different datasets.      Finally, we suggest the best practices and indicate unsolved problems for incorporating distance transform maps into CNNs, which we hope will be useful for the community. The codes and trained models are publicly available at \url{https://github.com/JunMa11/SegWithDistMap}.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p002") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('lqfGw0tDy3k', '/slides/ma20a.pdf', 720, 450) }}