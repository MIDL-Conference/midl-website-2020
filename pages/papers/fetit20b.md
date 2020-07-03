---
title: "A deep learning approach to segmentation of the developing cortex in fetal brain MRI with minimal manual labeling"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# P136 - A deep learning approach to segmentation of the developing cortex in fetal brain MRI with minimal manual labeling


### Ahmed E. Fetit, Amir Alansary, Lucilio Cordero-Grande, John Cupitt, Alice B. Davidson, A. David Edwards, Joseph V. Hajnal, Emer Hughes, Konstantinos Kamnitsas, Vanessa Kyriakopoulou, Antonios Makropoulos, Prachi A. Patkee, Anthony N. Price, Mary A. Rutherford, Daniel Rueckert

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=VtVIlHSc0">Paper</a>
        - <a href="https://openreview.net/forum?id=VtVIlHSc0">Reviews</a>
        {{ teaser('CJIAB_ryWGs') }}

<span class="paper_abstract">
        We developed an automated system based on deep neural networks for fast and sensitive 3D image segmentation of cortical gray matter from fetal brain MRI. The lack of extensive/publicly available annotations presented a key challenge, as large amounts of labeled data are typically required for training sensitive models with deep learning. To address this, we: (i) generated preliminary tissue labels using the Draw-EM algorithm, which uses Expectation-Maximization and was originally designed for tissue segmentation in the neonatal domain; and (ii) employed a human-in-the-loop approach, whereby an expert fetal imaging annotator assessed and refined the performance of the model. By using a hybrid approach that combined automatically generated labels with manual refinements by an expert, we amplified the utility of ground truth annotations while immensely reducing their cost (283 slices). The deep learning system was developed, refined, and validated on 249 3D T2-weighted scans obtained from the Developing Human Connectome Project\'s fetal cohort, acquired at 3T. Analysis of the system showed that it is invariant to gestational age at scan, as it generalized well to a wide age range (21 – 38 weeks) despite variations in cortical morphology and intensity  across the fetal distribution. It was also found to be invariant to intensities in regions surrounding the brain (amniotic fluid), which often present a major obstacle to the processing of neuroimaging data in the fetal domain.  
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        TUE 9:30-11:00 UTC-4 - Poster Session #3
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/p136") }}

---

### Spotlight presentation

---

{{ presentation('AahUnVAA2VU', '/slides/fetit20b.pdf', 720, 450) }}