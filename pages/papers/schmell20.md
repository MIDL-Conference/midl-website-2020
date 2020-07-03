---
title: "An interpretable automated detection system for FISH-based HER2 oncogene amplification testing in histo-pathological routine images of breast and gastric cancer diagnostics"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S188 - An interpretable automated detection system for FISH-based HER2 oncogene amplification testing in histo-pathological routine images of breast and gastric cancer diagnostics

### Sarah Schmell, Falk Zakrzewski, Walter de Back, Martin Weigert, Uwe Schmidt, Torsten Wenke, Silke Zeugner, Robert Mantey, Christian Sperling, Ingo Roeder, Pia Hoenscheid, Daniela Aust, Gustavo Baretton

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=qDEYfzeK7k">Paper</a>
- <a href="https://openreview.net/forum?id=qDEYfzeK7k">Reviews</a>
{{ teaser('z1OGEOr32og') }}

<p>
    <span class="abstract">
        Histo-pathological diagnostics are an inherent part of the everyday work but are particularly laborious and often associated with time-consuming manual analysis of image data. In order to cope with the increasing diagnostic case numbers due to the current growth and demographic change of the global population and the progress in personalized medicine, pathologists ask for assistance. Profiting from digital pathology and the use of artificial intelligence, individual solutions can be offered (e.g. to detect labeled cancer tissue sections). The testing of the human epidermal growth factor receptor 2 (HER2) oncogene amplification status via fluorescence in situ hybridization (FISH) is recommended for breast and gastric cancer diagnostics and is regularly performed at clinics. Here, we developed a comprehensible, multi-step deep learning-based pipeline which automates the evaluation of FISH images with respect to HER2 gene amplification testing. It mimics the pathological assessment and relies on the detection and localization of interphase nuclei based on instance segmentation networks. Furthermore, it localizes and classifies fluorescence signals within each nucleus with the help of image classification and object detection convolutional neural networks (CNNs). Finally, the pipeline classifies the whole image regarding its HER2 amplification status. The visualization of pixels on which the networks\' decision occurs, complements an essential part to enable interpretability by pathologists.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #5  - 9:30 - 11:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/s188") }} -->
[% / %]

---

### Short paper

---

{{ presentation('z1OGEOr32og', '/slides/schmell20.pdf', 720, 450) }}