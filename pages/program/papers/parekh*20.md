---
title: "Multitask radiological modality invariant landmark localization using deep reinforcement learning"
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

# P273 - Multitask radiological modality invariant landmark localization using deep reinforcement learning


##### Vishwa S. Parekh*, Alex E. Bocchieri*, Michael A. Jacobs

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=XvBdNAyPCk">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'Deep learning techniques are increasingly being developed for several applications in radiology, for example landmark and organ localization with segmentation. However, these applications to date have been limited in nature, in that, they are restricted to just a single task e.g. localization of tumors or to a specific organ using supervised training by an expert. As a result, to develop a radiological decision support system, it would need to be equipped with potentially hundreds of deep learning models with each model trained for a specific task or organ. This would be both space and computationally expensive. In addition, the true potential of deep learning methods in radiology can only be achieved when the model is adaptable and generalizable to multiple different tasks. To that end, we have developed and implemented a multitask modality invariant deep reinforcement learning framework (MIDRL) for landmark localization and segmentation in radiological applications.  MIDRL was evaluated using a diverse data set containing multiparametric MRIs (mpMRI) acquired from different organs and with different imaging parameters. The MIDRL framework was trained to localize six different anatomical structures throughout the body, including, knee, trochanter, heart, kidney, breast nipple, and prostate across T1 weighted, T2 weighted, Dynamic Contrast Enhanced (DCE), Diffusion Weighted Imaging (DWI), and DIXON MRI sequences obtained from twenty-four breast, eight prostate, and twenty five whole body mpMRIs. The trained MIDRL framework produced excellent accuracy in localizing each of the six anatomical landmarks with an average dice similarity$>$0.77, except for breast nipple localization in DCE. In conclusion, we developed  a multitask deep reinforcement learning framework and demonstrated MIDRL’s potential towards the development of a general AI for a radiological decision support system.'
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/P273") }}

---

### Spotlight presentation
