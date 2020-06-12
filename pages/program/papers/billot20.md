---
title: "A learning strategy for contrast-agnostic MRI segmentation"
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

# [A learning strategy for contrast-agnostic MRI segmentation](https://chat.midl.io/channel/O072)

##### Benjamin Billot,Douglas N. Greve,Koen Van Leemput,Bruce Fischl,Juan Eugenio Iglesias,Adrian V. Dalca
###### Keywords: KEYWORDS

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=Qz2DgRQGlP">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        We present a deep learning strategy for contrast-agnostic semantic segmentation of unpreprocessed brain MRI scans, without requiring additional training or fine-tuning for new modalities. Classical Bayesian methods address this segmentation problem with unsupervised intensity models, but require significant computational resources. In contrast, learning-based methods can be fast at test time, but are sensitive to the data available at training. Our proposed learning method, SynthSeg, leverages a set of training segmentations (no intensity images required) to generate synthetic scans of widely varying contrasts on the fly during training. These scans are produced using the generative model of the classical Bayesian segmentation framework, with randomly sampled parameters for appearance, deformation, noise, and bias field. Because each mini-batch has a different synthetic contrast, the final network is not biased towards any specific MRI contrast. We comprehensively evaluate our approach on four datasets comprising over 1,000 subjects and four MR contrasts. The results show that our approach successfully segments every contrast in the data, performing slightly better than classical Bayesian segmentation, and three orders of magnitude faster. Moreover, even within the same type of MRI contrast, our strategy generalizes significantly better across datasets, compared to training using real images. Finally, we find that synthesizing a broad range of contrasts, even if unrealistic, increases the generalization of the neural network. Our code and model are open source at https://github.com/BBillot/SynthSeg.
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

### Oral presentation
