---
title: "Boundary loss for highly unbalanced segmentation"
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

{% from "_macros.html" import youtube %}

# Boundary loss for highly unbalanced segmentation

<center>[Hoel Kervadec](mailto:@hoel:synapse.kervadec.bzh), Jihene Bouchtiba, Christian Desrosiers, Éric Granger, Jose Dolz, [Ismail Ben Ayed](mailto:@ismail:synapse.kervadec.bzh)</center>

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
		- <a href="http://proceedings.mlr.press/v102/kervadec19a.html">Paper</a>
		- <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Q/A</a>

<span class="paper_abstract">
	Widely used loss functions for convolutional neural network (CNN) segmentation, e.g., Dice or cross-entropy, are based on integrals (summations) over the segmentation regions. Unfortunately, forhighly unbalanced segmentations, such regional losses have values that differ considerably -- typically of several orders of magnitude -- across segmentation classes, which may affect training performance and stability. We propose a {\em boundary} loss, which takes the form of a distance metric on the space of contours (or shapes), not regions. This can mitigate the difficulties of regional losses in the context of highly unbalanced segmentation problems because it uses integrals over the boundary (interface) between regions instead of unbalanced integrals over regions. Furthermore, a boundary loss provides information that is complimentary to regional losses. Unfortunately, it is not straightforward to represent the boundary points corresponding to the regional softmax outputs of a CNN. Our boundary loss is inspired by discrete (graph-based) optimization techniques for computing gradient flows of curve evolution. Following an integral approach for computing boundary variations, we express a non-symmetric $L_2$ distance on the space of shapes as a regional integral, which avoids completely local differential computations involving contour points. This yields a boundary loss expressed with the regional softmax probability outputs of the network, which can be easily combined with standard regional losses and implemented with any existing deep network architecture for N-D segmentation.  We report comprehensive evaluations on two benchmark datasets corresponding to difficult, highly unbalanced problems: the ischemic stroke lesion (ISLES) and white matter hyperintensities (WMH). Used in conjunction with the region-based generalized Dice loss (GDL), our boundary loss improves performance significantly compared to GDL alone, reaching up to $8\%$ improvement in Dice score and $10\%$  improvement in Hausdorff score. It also yielded a more stable learning process. Our code is publicly available at [https://github.com/LIVIAETS/surface-loss](https://github.com/LIVIAETS/surface-loss).
	<span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
	QA times:
	<br/>
	- May 30 2020, 16:00 UTC - Live QA
	<br/>
	- May 31 2020, 22:00 UTC - Poster session
	<br/>
	[Videocall room](https://meet.kervadec.science/O001)
	<br/>
	<span class="actions"><a class="toggle_visibility" data-level="2">Hide QA</a></span>
</span>

---

{{ youtube('_z6gmFlD_qE') }}


---

<iframe src="/slides/kervadec19.pdf" width="720" height="500"></iframe>