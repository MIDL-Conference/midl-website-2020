---
title: "Fusing Structural and Functional MRIs using Graph Convolutional Networks for Autism Classification"
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

# [Fusing Structural and Functional MRIs using Graph Convolutional Networks for Autism Classification](https://chat.midl.io/channel/P183)

##### Devanshu Arya,Richard Olij,Deepak K. Gupta,Ahmed El Gazzar,Guido van Wingen,Marcel Worring,Rajat Mani Thomas
###### Keywords: KEYWORDS

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=EKu4FU5s4">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        Geometric deep learning methods such as graph convolutional networks have recently proven to deliver generalized solutions in disease prediction using medical imaging. In this paper, we focus particularly on their use in autism classification. Most of the recent methods use graphs to leverage phenotypic information about subjects (patients or healthy controls) as additional contextual information. To do so, metadata such as age, gender and acquisition sites are utilized to define intricate relations (edges) between the subjects. We alleviate the use of such non-imaging metadata and propose a fully imaging-based approach where information from structural and functional Magnetic Resonance Imaging (MRI) data are fused to construct the edges and nodes of the graph. To characterize each subject, we employ brain summaries. These are 3D images obtained from the 4D spatiotemporal resting-state fMRI data through summarization of the temporal activity of each voxel using neuroscientifically informed temporal measures such as amplitude low frequency fluctuations and entropy. Further, to extract features from these 3D brain summaries, we propose a 3D CNN model. We perform analysis on the open dataset for autism research (full ABIDE I-II) and show that by using simple brain summary measures and incorporating sMRI information, there is a noticeable increase in the generalizability and performance values of the framework as compared to state-of-the-art graph-based models.
        <span class="actions">
  <br/>
  <a class="toggle_visibility" data-level="2">Hide abstract</a></span>
</span>

<span class="paper_qa">
        Not available for now
        <br/>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
</span>

---

### Spotlight presentation
