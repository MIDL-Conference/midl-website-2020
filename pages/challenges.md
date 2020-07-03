---
title: "Challenges"
page_class: "events"
---

{% from "_macros.html" import button %}


# Official MIDL 2020 challenges

For the first time, MIDL invites the community to propose challenges involving both medical imaging and machine learning topics.

**Challenges will be held on July 9 2020.**

---

## object-CXR
#### Automatic detection of foreign objects on chest X-rays
#### Thursday July 9 - 9:00-13:00 UTC-4

Analyzing chest X-rays is a common clinical approach for diagnosing pulmonary and heart diseases. However, foreign objects are occasionally presented on chest X-ray images, especially in rural and remote locations where standard filming guidelines are not strictly followed. Foreign objects on chest X-rays may obscure pathological finds, thus increasing false negative diagnosis. They may also confuse junior radiologists from real pathological findings, e.g. buttons are visually similar to nodules on chest X-ray, thus increasing false positive diagnosis. An algorithm based foreign object detection system could automatically promote re-filming, thus significantly reduce the cost and save radiologists time for more diagnosis.

We provide a large dataset of chest X-rays with strong annotations of foreign objects, and the competition for automatic detection of foreign objects. Specifically, 5000 frontal chest X-ray images with foreign objects (all manually annotated) as well as 5000 frontal chest X-ray images without foreign objects are provided.

More info: [Challenge website](https://jfhealthcare.github.io/object-CXR/)

---

## MC-MRRec
#### Multi-channel MR Image Reconstruction Challenge
#### Thursday July 9 - 14:00-17:00 UTC-4

Deep-learning-based Magnetic Resonance (MR) Imaging reconstruction has the potential to greatly speed-up MR exams. Our Multi-channel MR Image Reconstruction Challenge tackles this issue by:

* Comparing different DL-based MR reconstruction models on a large dataset (> 200 GB)
* Assessing reconstruction model generalizability to various datasets acquired with a different number of channels

The challenge has two separate tracks, and teams are free to decide whether to submit to just one track or both; we encourage teams to submit to both tracks. Each track will have a separate ranking.

In these two tracks, we will assess MR reconstruction quality and noticeable loss of high resolution detail, especially at the higher acceleration rates. By having two separate tracks, we hope to determine whether a generic reconstruction model applicable to various multi-channel coils will have a decreased performance (if any) compared to more coil-specific reconstruction models.


More info: [Challenge website](https://sites.google.com/view/calgary-campinas-dataset/home/mr-reconstruction-challenge).

If having troubles accessing the website, please contact: [roberto.medeirosdeso@ucalgary.ca](mailto:roberto.medeirosdeso@ucalgary.ca)


---

## SARAS-ESAD
### SARAS endoscopic vision challenge for surgeon action detection
#### Thursday July 9 - 9:00-13:00 UTC-4

Minimally Invasive Surgery (MIS) is a very sensitive medical procedure, whose success depends on the competence of the human surgeons and the degree of effectiveness of their coordination. The SARAS (Smart Autonomous Robotic Assistant Surgeon) EU consortium, is working towards replacing the assistant surgeon in MIS with two assistive robotic arms. To accomplish that, an artificial intelligence based system is required which not only can understand the complete surgical scene but also detect the actions being performed by the main surgeon.

This challenge has recorded four sessions of complete prostatectomy procedure performed by expert surgeons on real patients with prostate cancer. Later, expert AI and medical professions annotated these complete surgical procedures for the actions. Multiple action instances might be present at any point during the procedure . Hence, each frame is labeled for multiple actions and these actions can have overlapping bounding boxes.

To the best of our knowledge, this challenge presents the first benchmark dataset for action detection in the surgical domain, and paves the way for the introduction, for the first time, of partial/full autonomy in surgical robotics. Within computer vision, other datasets for action detection exist, but are of limited size.

More info:

* [Challenge website](https://saras-esad.grand-challenge.org)
* [SARAS (Smart Autonomous Robotic Assistant Surgeon) EU consortium](https://www.saras-project.eu/)

---

The [call for challenges](call-for-challenges.html) is still available.
