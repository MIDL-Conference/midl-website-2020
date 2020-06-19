---
title: "Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion"
---
<style>
.paper_abstract {
  display: none;
  font-size: 90%;
  line-height: 1.35;
  text-align: justify;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}

.paper_qa {
  display: none;
  line-height: 1.35;
  text-align: center;
  margin-top: 4px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 4px;

  .actions {
    display: block;
    text-align: center;
    margin-top: 4px;
  }
}
</style>

{% from "_macros.html" import button %}

# S116 - Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion


##### Milan Decuyper, Stijn Bonte, Karel Deblaere, Roel Van Holen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=J5iep2t90F">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'In the WHO glioma classification guidelines grade, IDH mutation and 1p19q co-deletion play a central role as they are important markers for prognosis and optimal therapy planning. Therefore, we propose a fully automatic, MRI based, 3D pipeline for glioma segmentation and classification. The designed segmentation network was a 3D U-Net achieving an average whole tumor dice score of 90%. After segmentation, the 3D tumor ROI is extracted and fed into the multi-task classification network. The network was trained and evaluated on a large heterogeneous dataset of 628 patients, collected from The Cancer Imaging Archive and BraTS 2019 databases. Additionally, the network was validated on an independent dataset of 110 patients retrospectively acquired at the Ghent University Hospital (GUH). Classification AUC scores are 0.93, 0.94 and 0.82 on the TCIA test data and 0.94, 0.86 and 0.87 on the GUH data for grade, IDH and 1p19q status respectively. '
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/S116") }}

---

### Short paper
