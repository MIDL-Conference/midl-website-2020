---
title: "Prostate Cancer Semantic Segmentation by Gleason Score Group in mp-MRI with Self Attention Model on the Peripheral Zone"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P238 - Prostate Cancer Semantic Segmentation by Gleason Score Group in mp-MRI with Self Attention Model on the Peripheral Zone

#### Audrey Duran, Pierre-Marc Jodoin, Carole Lartizien

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=Ih04Ji3rtN">Paper</a>
- <a href="https://openreview.net/forum?id=Ih04Ji3rtN">Reviews</a>
{{ teaser('Jrj2SAtkPLY') }}

<p>
    <span class="abstract">
        Multiparametric magnetic resonance imaging (mp-MRI) has shown promising results in the detection of prostate cancer (PCa). However, discriminating clinically significant (CS) from benign lesions is time demanding and challenging, even for experienced readers, especially when individual MR sequences yield conflicting findings. Computer aided detection (CADe) or diagnostic (CADx) systems based on standard or deep supervised machine learning have achieved high performance in assisting radiologists for this diagnostic binary detection task.      We aim to go one step further in the diagnostic refinement by characterizing the aggressiveness of PCa lesions, assessed by the Gleason score (GS) group grading. This challenging problem has been very recently addressed from the deep learning perspective by a few groups.      In this work, we propose a novel end-to-end multiclass deep network to jointly perform the segmentation of the peripheral prostate zone (PZ) as well as the detection and GS Group grading of PZ lesions. Our U-Net inspired  architecture is constituted from a standard encoding part that first extracts the latent information from multichannel T2 weighted (T2w) and  apparent diffusion coefficient (ADC) input images. This latent representation is then connected to two separate decoding branches : 1) the first one performs a binary PZ segmentation 2) the second branch uses this zonal prior as an attention gate for the detection and grading of PZ lesions.      Performance of this model was evaluated on a dataset of 98 mp-MRI exams including 57 exams acquired on a 1.5 Tesla scanner (Symphony; Siemens, Erlangen, Germany) and 41 exams acquired on a 3 Tesla scanner (Discovery; General Electric, Milwaukee, USA). All patients underwent a prostatectomy after the MR exams. The prostatectomy specimens were analyzed a posteriori by an anatomopathologist thus providing the histological ground.  A total of 132 lesions were delineated on the images, including 37, 47, 23, 16 and 9 lesions of GS 6, 3+4, 4+3, 8 and ≥ 9, respectively. All lesions with a GS > 6 were considered as clinically significant.      The deep model was trained and validated with a 5-fold cross-validation. Performance of our model was compared to a U-Net baseline model to assess the impact of the self attention module on PCa detection.      A free-response receiver operating (FROC) analysis was conducted to evaluate the performance in detecting CS lesions and to discriminate lesions of the different GS groups.      Regarding the detection of CS lesions, our model achieves 75.78% sensitivity at 2.5 false positive per patient. Regarding the automatic GS group grading, the Cohen quadratic weighted kappa coefficient is 0.35, which is considered as a fair agreement and an improvement with regards to the baseline model. Our model reaches 78% and 18% sensitivity for GS ≥ 9 and GS 6 at 1 false positive per patient, respectively.      Our method achieves good performance without requiring any prior manual region delineation in clinical practice. We show that the addition of the proposed self attention mechanism improves the CAD performance in comparison to the baseline model.      
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

{{ button("Access paper channel", "https://chat.midl.io/channel/p238") }}
[% / %]

---


### Spotlight presentation

---

{{ presentation('Au8FCQBka9o', '/slides/duran20.pdf', 720, 450) }}