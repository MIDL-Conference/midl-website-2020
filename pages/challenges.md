---
title: "Challenges"
page_class: "events"
---

{% from "_macros.html" import button %}


# Official MIDL 2020 challenges

For the first time, MIDL invites the community to propose challenges involving **both medical imaging and machine learning** topics.

---

## object-CXR
### Automatic detection of foreign objects on chest X-rays

Analyzing chest X-rays is a common clinical approach for diagnosing pulmonary and heart diseases. However, foreign objects are occasionally presented on chest X-ray images, especially in rural and remote locations where standard filming guidances are not strictly followed. Foreign objects on chest X-rays may obscure pathological finds, thus increasing false negative diagnosis. They may also confuse junior radiologists from real pathological findings, e.g. buttons are visually similar to nodules on chest X-ray, thus increasing false positive diagnosis. An algorithm based foreign object detection system could automatically promote re-filming, thus significantly reduce the cost and save radiologists time for more diagnosis, which has been noticed before (L Hogeweg, 2013, Medical Physics).

We provide a large dataset of chest X-rays with strong annotations of foreign objects, and the competition for automatic detection of foreign objects. Specifically, 5000 frontal chest X-ray images with foreign objects presented and 5000 frontal chest X-ray images without foreign objects are provided.
Detecting foreign objects is particularly challenging for deep learning (DL) based systems, as specific types of objects presented in the test set may be rarely or never seen in the training set, thus posing a few-shot/zero-shot learning problem. We hope this open dataset and challenge could both help the development of automatic foreign objects detection system, and promote the general research of object detection on chest X-rays, as large scale chest X-ray datasets with strong annotations are limited to the best of our knowledge.

More info: [Challenge website](https://jfhealthcare.github.io/object-CXR/)

---

More challenges to come.

The [call for challenges](call-for-challenges.html) is still available.
