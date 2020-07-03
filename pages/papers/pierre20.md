---
title: "Priority Unet: Detection of Punctuate White Matter Lesions in Preterm Neonate in 3D Cranial Ultrasonography"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# P228 - Priority Unet: Detection of Punctuate White Matter Lesions in Preterm Neonate in 3D Cranial Ultrasonography

### ERBACHER Pierre, LARTIZIEN Carole, MARTIN Matthieu, FOLLETO PIMENTA Pedro, QUETIN Philippe, DELACHARTRE Philippe

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=BpXY-yIs6f">Paper</a>
- <a href="https://openreview.net/forum?id=BpXY-yIs6f">Reviews</a>
{{ teaser('') }}

<p>
    <span class="abstract">
        Brain damage, particularly of cerebral white matter (WM), observed in premature infants in the neonatal period is responsible for frequent neurodevelopmental sequelae in early childhood and [V Pierrat et al. EPIPAGE-2 cohort study. BMJ. 2017]. Punctuate white matter lesions (PWML) are most frequent WM abnormalities, occurring in 18–35% of all preterm infants [AL Nguyen et al. Int Journal of Developmental Neuroscience, 2019] [N. Tusor et al, Scientific Reports, 2017].      Accurately assessing the volume and localisation of these lesions at the early postnatal phase can help paediatricians adapting the therapeutic strategy and potentially reduce severe sequelae. MRI is the gold standard neuroimaging tool to assess minimal to severe WM lesions, but it is only rarely performed for cost and accessibility reasons. Cranial ultrasonography (cUS) is a routinely used tool, however, the visual detection of PWM lesions  is challenging and time consuming because these lesions are small with variable contrast and no specific pattern. There are also weak anatomical landmarks in neonate brains as the brain structures are moving and not fully developed.      Research on automatic detection of PWML on MRI based on standard image analysis was initiated by Mukherjee [Mukherjee, S. et al. MBEC 57(1), 71-87, 2019]. One other team has recently tackled this issue based on deep architectures [Y Liu et al. MICCAI 2019]. Despite the high contrast and low noise of MR images, this algorithm struggles with low accuracy over the PWML detection task. As far as we know, there is currently no known research team working on automatic segmentation of PWML on US data. This task is highly challenging because of the speckle noise, low contrast and the high acquisition variability.      In this paper, we introduce a novel architecture based on the U-Net backbone to perform the detection and segmentation of PWML in cUS images. This model combines a soft attention model focusing on the PWML localisation and the self balancing focal loss (SBFL) introduced by Lin [Liu et al, arxiv, 2019]. The soft attention mask is a 3D probabilistic map derived from spatial prior knowledge of PWML localisation computed from our dataset.      Performance of this model is evaluated on a dataset of cUS exams including 21 patients acquired with a Acuson Siemens 4-9 MHZ probe. For each exam, a 3D volume of dimension 360x400x380 was reconstructed with an isotropic spatial resolution of 0.15 mm.  A total of 547 lesions were delineated on the images by an expert pediatrician. For this study, we considered 131 lesions with a volume bigger than 1.7 $mm^3$. Volumes of PWM lesions range from 1.75 $mm^3$ to 61.09 $mm^3$ with a median size of 4 $mm^3$.      The deep model was trained and validated with a 10-fold cross-validation based on approximately 3000 coronal slices extracted from the 3D volumes .  We also performed an ablation study to evaluate the impact of the attention gate and the focal loss. Detection performance was assessed at the lesion level, thus meaning that we performed a cluster analysis on the label maps outputted by the network using a 3D connectivity rule to identify the connected components.      Compared to the U-Net, the priority U-Net with SBFL increases the recall and the precision in the detection task from 0.4404      to 0.5370 and from 0.3217 to 0.5043, respectively. The Dice metric is also increased from 0.3040 to 0.3839 in the segmentation task.      In this study, we proposed the first use case of automated detection of PWML in cUS exams of preterms neonates as well as a novel deep architecture inspired from the attention gated U-Net combined with the self-balancing focal loss. Our results are shown to outperform the standard U-Net for this challenging detection task.
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

<!-- {{ button("Access paper channel", "https://chat.midl.io/channel/p228") }} -->
[% / %]

---

### Spotlight presentation

---

