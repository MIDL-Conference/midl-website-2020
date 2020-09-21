---
title: "Knee Injury Detection using MRI with Efficiently-Layered Network (ELNet)"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P117 - Knee Injury Detection using MRI with Efficiently-Layered Network (ELNet)

#### Chen-Han Tsai, Nahum Kiryati, Eli Konen, Iris Eshed, Arnaldo Mayer

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="http://proceedings.mlr.press/v121/tsai20a.html">Proceedings</a>
- <a href="https://openreview.net/pdf?id=B_NG9y_wqU">PDF</a>
- <a href="https://openreview.net/forum?id=B_NG9y_wqU">Reviews</a>
{{ teaser('8nO-E_2aNcE') }}

<p>
    <span class="abstract">
        Magnetic Resonance Imaging (MRI) is a widely-accepted imaging technique for knee injury analysis. Its advantage of capturing knee structure in three dimensions makes it the ideal tool for radiologists to locate potential tears in the knee. In order to better confront the ever growing workload of musculoskeletal (MSK) radiologists, automated tools for patients\' triage are becoming a real need, reducing delays in the reading of pathological cases. In this work, we present the Efficiently-Layered Network (ELNet), a convolutional neural network (CNN) architecture optimized for the task of initial knee MRI diagnosis for triage. Unlike past approaches, we train ELNet from scratch instead of using a transfer-learning approach. The proposed method is validated quantitatively and qualitatively, and compares favorably against state-of-the-art MRNet while using a single imaging stack (axial or coronal) as input. Additionally, we demonstrate our model\'s capability to locate tears in the knee despite the absence of localization information during training. Lastly, the proposed model is extremely lightweight ($<$ 1MB) and therefore easy to train and deploy in real clinical settings.
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p117") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('ucWYdEJ545k', '/slides/tsai20.pdf', 720, 450) }}