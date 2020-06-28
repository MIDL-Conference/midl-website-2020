---
title: "A CNN-LSTM Architecture for Detection of Intracranial Hemorrhage on CT scans"
page_class: "paper-page"
---

{% from "_macros.html" import button %}

# S041 - A CNN-LSTM Architecture for Detection of Intracranial Hemorrhage on CT scans


### Nhan T. Nguyen, Dat Q. Tran, Nghia T. Nguyen, Ha Q. Nguyen

<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Show abstract</a>
        - <a href="https://openreview.net/forum?id=1IoPbyuPFT">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Show schedule</a>

<span class="paper_abstract">
        We propose a novel method that combines a convolutional neural network (CNN) with a long short-term memory (LSTM) mechanism for accurate prediction of intracranial hemorrhage on computed tomography (CT) scans. The CNN plays the role of a slice-wise feature extractor while the LSTM is responsible for linking the features across slices. The whole architecture is trained end-to-end with input being an RGB-like image formed by stacking 3 different viewing windows of a single slice. We validate the method on the recent RSNA Intracranial Hemorrhage Detection challenge and on the CQ500 dataset. For the RSNA challenge, our best single model achieves a weighted log loss of 0.0529 on the leaderboard, which is comparable to the top 3\% performances, almost all of which make use of ensemble learning. Importantly, our method generalizes very well: the model trained on the RSNA dataset significantly outperforms the 2D model, which does not take into account the relationship between slices, on CQ500. Our codes and models will be made public.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        MON 9:30-11:00 ET - Poster Session #1
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

{{ button("Access paper channel", "https://chat.midl.io/channel/S041") }}

---

### Short paper
