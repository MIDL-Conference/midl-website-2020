---
title: "Siamese Content Loss Networks for Highly Imbalanced Medical Image Segmentation"
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

# P271 - Siamese Content Loss Networks for Highly Imbalanced Medical Image Segmentation


##### Brandon Mac, Alan R. Moody, April Khademi

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=VINrwcDkvA">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'Automatic segmentation of white matter hyperintensities (WMHs) in magnetic resonance imaging (MRI) remains highly sought after due to the potential to streamline and alleviate clinical workflows. WMHs are small relative to whole acquired volume, which leads to class imbalance issues, and instability during the training process of many deep learning based solutions. To address this, we propose a method which is robust to effects of class imbalance, through incorporating multi-scale information in the training process. Our method consists of training an encoder-decoder neural network utilizing a Siamese network as an auxiliary loss function. These Siamese networks take in pairs of image pairs, input images masked with ground truth labels, and input images masked with predictions, and computes multi-resolution feature vector representations and provides gradient feedback in the form of a L2 norm. We leverage transfer learning in our Siamese network, and present positive results without need to further train. It was found these methods are more robust for training segmentation neural networks and provide greater generalizability. Our method was cross-validated on multi-center data, yielding significant overall agreement with manual annotations. '
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/P271") }}

---

### Spotlight presentation
