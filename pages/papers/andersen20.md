---
title: "Comparing Objective Functions for Segmentation and Detection of Tiny Lesions in Retinal Images"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P174 - Comparing Objective Functions for Segmentation and Detection of Tiny Lesions in Retinal Images

### Jakob Kristian Holm Andersen, Thiusius Rajeeth Savarimuthu, Jakob Grauslund

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=TC_eOaPKBB">Paper</a>
- <a href="https://openreview.net/forum?id=TC_eOaPKBB">Reviews</a>
{{ teaser('w8zGGamA3Ao') }}

<p>
    <span class="abstract">
        Retinal microaneurysms (MAs) are the earliest signs of diabetic retinopathy (DR) which is  the  leading  cause  of  blindness  in  the  western  world.   MAs  independently  predict  the risk of sight threatening DR and early detection is important to identify patients at risk. Detection and segmentation of retinal MAs present a particular challenging problem due to  a  large  class  imbalance  with  MA  pixels  accounting  for  less  than  0.5%  of  the  retinal image.  Extreme foreground-background class imbalance can adversely affect the learning process in DNNs by introducing a bias towards the most well represented class.  Recently, a number of objective functions have been proposed as alternatives to the standard Crossentropy loss in efforts to overcome this problem.  In this work we investigate the influence of  the  network  objective  during  optimization  by  comparing  Residual  U-nets  trained  for segmentation of MAs in retinal images using seven different objective functions; weighted and unweighted Crossentropy loss, Dice loss, weighted and unweighted Focal loss, Focal Dice loss and Focal Tversky loss.  Three networks with different seeds are trained for each objective function using optimized hyper-parameter settings on a dataset of 382 images with pixel level annotations for MAs.  The instance level MA detection performance is evaluated as the average free response receiver operator characteristic (FROC) score calculated as the mean sensitivity at seven average false positives (FPAvg) per image thresholds on 80 test images.  The image level MA detection performance is evaluated as the average AUC on the same images as well as a separate test set of 1200 images.  Segmentation performance is  evaluated  as  the  average  pixel  precision  (AP).  The  unweighted  Crossentropy  loss  and Focal loss outperforms all other losses for instance level detection achieving FROC scores of  0.5067(±0.0115)  and  0.5062(±0.0045.   The  Focal  loss  has  the  highest  pixel  precision with an AP of 0.4254(±0.0096).  For image level detection both objective functions in their unweighted form perform significantly better compared to using all other objectives.  AUCs of 0.9450(±0.0080) and 0.8351(±0.0039) on the two test are achieved using the unweighted Crossentropy  loss,  while  AUCs  for  the  unweighted  Focal  loss  was  0.9375(±0.0074)  and 0.8253(±0.0042) respectivly.      Conclusion:      Despite the promise of using training objectives designed to deal with unbalanced data, the standard Crossentropy loss perform at least as well or better than all other objective functions in our experiments for lesion level and image level detection for small  retinal  MAs.   While  a  number  of  newer  objective  functions  have  been  introduced and shown to improve performance for unbalanced datasets compared to the Dice loss in recent years, our results suggest that it is important to also benchmark new losses against the Crossentropy or Focal loss function, as we achieve the best performance in all our test using these objectives.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #1  - 9:30 - 11:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/p174") }}
[% / %]

---


### Poster presentation

---

{{ presentation('X6JSy3XdSmw', '/slides/andersen20.pdf', 720, 450) }}