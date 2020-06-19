---
title: "Beyond Classfication: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning"
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

# O305 - Beyond Classfication: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning


##### Chensu Xie, Hassan Muhammad, Chad M. Vanderbilt, Raul Caso, Dig Vijay Kumar Yarlagadda, Gabriele Campanella, Thomas J. Fuchs

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=aqOfnZx4-N">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        'An emerging technology in cancer care and research is the use of histopathology whole slide images (WSI). Leveraging computation methods to aid in WSI assessment poses unique challenges. WSIs, being extremely high resolution giga-pixel images, cannot be directly processed by convolutional neural networks (CNN) due to huge computational cost. For this reason, state-of-the-art methods for WSI analysis adopt a two-stage approach where the training of a tile encoder is decoupled from the tile aggregation. This results in a trade-off between learning diverse and discriminative features. In contrast, we propose end-to-end part learning (EPL) which is able to learn diverse features while ensuring that learned features are discriminative. Each WSI is modeled as consisting of $k$ groups of tiles with similar features, defined as parts. A loss with respect to the slide label is backpropagated through an integrated CNN model to $k$ input tiles that are used to represent each part. Our experiments show that EPL is capable of clinical grade prediction of prostate and basal cell carcinoma. Further, we show that diverse discriminative features produced by EPL succeeds in multi-label classification of lung cancer architectural subtypes. Beyond classification, our method provides rich information of slides for high quality clinical decision support.'
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/O305") }}

---

### Oral presentation
