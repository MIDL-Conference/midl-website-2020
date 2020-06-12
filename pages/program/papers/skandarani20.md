---
title: "On the effectiveness of GAN generated cardiac MRIs for segmentation"
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

# [On the effectiveness of GAN generated cardiac MRIs for segmentation](https://chat.midl.io/channel/S118)

##### Youssef Skandarani,Nathan Painchaud,Pierre-Marc Jodoin,Alain Lalande
###### Keywords: KEYWORDS

<!-- ### Abstract -->
<center><a class="toggle_visibility" data-selector=".paper_abstract" data-level="3">Abstract</a>
        - <a href="https://openreview.net/forum?id=f9Pl3Qj3_Q">Reviews</a>
        - <a class="toggle_visibility" data-selector=".paper_qa" data-level="3">Schedule</a>

<span class="paper_abstract">
        In this work, we propose a Variational Autoencoder (VAE) - Generative Adversarial Networks (GAN) model that can produce highly realistic MRI together with its pixel accurate groundtruth for the application of cine-MR image cardiac segmentation.  On one side of our model is a Variational Autoencoder (VAE) trained to learn the latent representations of cardiac shapes.  On the other side is a GAN that uses  ”SPatially-Adaptive (DE)Normalization” (SPADE) modules to generate realistic MR images tailored to a given anatomical map.  At test time, the sampling of the VAE latent space allows to generate an arbitrary large number of cardiac shapes, which are fed to the GAN that subsequently generates MR images whose cardiac structure fits that of the cardiac shapes.  In other words, our system can generate a large volume of realistic yet labeled cardiac MR images.  We show that segmentation with CNNs trained with our synthetic annotated images gets competitive results compared to traditional techniques.
      We also show that combining data augmentation with our GAN-generated images lead to an improvement in the Dice score of up to 12 percent while allowing for better generalization capabilities on  other datasets.
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

### Short paper
