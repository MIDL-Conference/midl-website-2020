---
title: "A Cross-Stitch Architecture for Joint Registration and Segmentation in Adaptive Radiotherapy"
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

# [A Cross-Stitch Architecture for Joint Registration and Segmentation in Adaptive Radiotherapy](https://chat.midl.io/channel/P197)

##### Laurens Beljaards,Mohamed S. Elmahdy,Fons Verbeek,Marius Staring
###### Keywords: KEYWORDS

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=oFXY64JJQ8">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        Recently, joint registration and segmentation has been formulated in a deep learning setting, by the definition of joint loss functions. In this work, we investigate joining these tasks at the architectural level. We propose a registration network that integrates segmentation propagation between images, and a segmentation network to predict the segmentation directly. These networks are connected into a single joint architecture via so-called cross- stitch units, allowing information to be exchanged between the tasks in a learnable manner. The proposed method is evaluated in the context of adaptive image-guided radiotherapy, using daily prostate CT imaging. Two datasets from different institutes and manufacturers were involved in the study. The first dataset was used for training (12 patients) and validation (6 patients), while the second dataset was used as an independent test set (14 patients). In terms of mean surface distance, our approach achieved 1.06 ± 0.3 mm, 0.91 ± 0.4 mm, 1.27 ± 0.4 mm, and 1.76 ± 0.8 mm on the validation set and 1.82 ± 2.4 mm, 2.45 ± 2.4 mm, 2.45 ± 5.0 mm, and 2.57 ± 2.3 mm on the test set for the prostate, bladder, seminal vesicles, and rectum, respectively. The proposed multi-task network outperformed single-task networks, as well as a network only joined through the loss function, thus demonstrating the capability to leverage the individual strengths of the segmentation and registration tasks. The obtained performance as well as the inference speed make this a promising candidate for daily re-contouring in adaptive radiotherapy, potentially reducing treatment-related side effects and improving quality-of-life after treatment.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

---

### Spotlight presentation
