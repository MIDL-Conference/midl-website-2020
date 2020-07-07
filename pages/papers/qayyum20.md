---
title: "Segmentation of the Myocardium on Late-Gadolinium Enhanced MRI based on 2.5 D Residual Squeeze and Excitation Deep Learning Model"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# S135 - Segmentation of the Myocardium on Late-Gadolinium Enhanced MRI based on 2.5 D Residual Squeeze and Excitation Deep Learning Model

### Abdul Qayyum, Alain Lalande, Thomas Decourselle, Thibaut Pommier, Alexandre Cochet, Fabrice Meriaudeau

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=4v2lR3Zvsw">Paper</a>
- <a href="https://openreview.net/forum?id=4v2lR3Zvsw">Reviews</a>
{{ teaser('Gl1ioiS7IEE') }}

<p>
    <span class="abstract">
        Cardiac left ventricular (LV) segmentation from short-axis MRI acquired 10 minutes after the injection of a contrast agent (LGE-MRI) is a necessary step in the processing allowing the identification and diagnosis of cardiac diseases such as myocardial infarction. However, this segmentation is challenging due to high variability across subjects and the potential lack of contrast between structures. Then, the main objective of this work is to develop an accurate automatic segmentation method based on deep learning models for the myocardial borders on LGE-MRI. To this end, 2.5 D residual neural network integrated with a squeeze and excitation blocks in encoder side with specialized convolutional has been proposed. Late fusion has been used to merge the output of the best trained proposed models from a different set of hyperparameters. A total number of 320 exams (with a mean number of 6 slices per exam) were used for training and 28 exams used for testing. The performance analysis of the proposed ensemble model in the basal and middle slices was similar as compared to intra-observer study and slightly lower at apical slices. The overall Dice score was 82.01% by our proposed method as compared to Dice score of 83.22% obtained from the intra observer study. The proposed model could be used for the automatic segmentation of myocardial border that is a very important step for accurate quantification of no-reflow, myocardial infarction, myocarditis, and hypertrophic cardiomyopathy, among others.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Poster Session #5  - 9:30 - 11:00 UTC-4 (Wednesday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/s135") }}
[% / %]

---


### Short paper

---

{{ presentation('hdNBYfsuJSE', '/slides/qayyum20.pdf', 720, 450) }}