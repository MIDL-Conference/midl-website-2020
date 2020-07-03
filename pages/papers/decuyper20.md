---
title: "Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion"
page_class: "paper-page"
---

{% from "_macros.html" import presentation %}
{% from "_macros.html" import button %}
{% from "_macros.html" import teaser %}
{% from "_macros.html" import youtube %}

# S116 - Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion


### Milan Decuyper, Stijn Bonte, Karel Deblaere, Roel Van Holen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>
        - <a href="https://openreview.net/pdf?id=J5iep2t90F">Paper</a>
        - <a href="https://openreview.net/forum?id=J5iep2t90F">Reviews</a>
        {{ teaser('HmU_h8GaUQM') }}

<span class="paper_abstract">
        In the WHO glioma classification guidelines grade, IDH mutation and 1p19q co-deletion play a central role as they are important markers for prognosis and optimal therapy planning. Therefore, we propose a fully automatic, MRI based, 3D pipeline for glioma segmentation and classification. The designed segmentation network was a 3D U-Net achieving an average whole tumor dice score of 90%. After segmentation, the 3D tumor ROI is extracted and fed into the multi-task classification network. The network was trained and evaluated on a large heterogeneous dataset of 628 patients, collected from The Cancer Imaging Archive and BraTS 2019 databases. Additionally, the network was validated on an independent dataset of 110 patients retrospectively acquired at the Ghent University Hospital (GUH). Classification AUC scores are 0.93, 0.94 and 0.82 on the TCIA test data and 0.94, 0.86 and 0.87 on the GUH data for grade, IDH and 1p19q status respectively. 
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 UTC-4 - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/s116") }}

---

### Short paper

---

{{ presentation('HmU_h8GaUQM', '/slides/decuyper20.pdf', 720, 450) }}