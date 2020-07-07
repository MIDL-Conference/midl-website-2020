---
title: "Awards"
---

{% from "_macros.html" import paper %}
{% from "_macros.html" import youtube %}

# Awards

The MIDL 2020 best paper award recognizes the highest quality full-length paper presented at the conference. The focus lies on novel methodological concepts with great potential of medical impact. All long papers that are presented as orals at MIDL 2020 were eligible. The award was decided by an independent committee composed of members of the program committee that had no conflicts of interest.

## Best paper Award
[% .papers %]
{{ paper('Addressing The False Negative Problem of MRI Reconstruction Networks by Adversarial Attacks and Robust Training',
        'Kaiyang Cheng, Francesco Calivá, Rutwik Shah, Misung Han, Sharmila Majumdar, Valentina Pedoia',
        openreview='https://openreview.net/forum?id=7NF2rZwE-z',
        pdf='https://openreview.net/pdf?id=7NF2rZwE-z',
        id='O028',
        paper='papers/cheng20.html',
        teaser='',
        video='https://youtu.be/7ccE6SXy9t8',
        abstract="Deep learning models have been shown to have success in reconstructing accelerated MRI, over traditional methods. However, it has been observed that these methods tend to miss the small features that are rare, such as meniscal tears, subchondral osteophyte, etc. This is a concerning finding as these small and rare features are the most relevant in clinical diagnostic settings. In this work, we propose a framework to find the worst-case false negatives by adversarially attacking the trained models and improve the models\\' ability to reconstruct the small features by robust training.")
}}
[% / %]

{{ youtube('7ccE6SXy9t8') }}


## Runner-ups for best paper Award

[% .papers %]
{{ paper('MAC-ReconNet: A Multiple Acquisition Context based Convolutional Neural Network for MR Image Reconstruction using Dynamic Weight Prediction',
        'Sriprabha Ramanarayanan, Balamurali Murugesan, Keerthi Ram, Mohanasankar Sivaprakasam',
        openreview='https://openreview.net/forum?id=pMHk_HIZf7',
        pdf='https://openreview.net/pdf?id=pMHk_HIZf7',
        id='O056',
        paper='papers/ramanarayanan20.html',
        teaser='https://youtu.be/_rzsMOcyV3o',
        video='https://youtu.be/HQ1ioGUwhcE',
        abstract='Convolutional Neural network based MR reconstruction methods have shown to provide fast and high quality reconstructions.  A primary drawback with a CNN-based model is that it lacks flexibility and can effectively operate only for a specific acquisition context limiting practical applicability.  By acquisition context, we mean a specific combination of three input settings considered namely, the anatomy under study, undersampling mask pattern and acceleration  factor  for  undersampling.   The  model  could be  trained  jointly  on  images  combining multiple contexts.  However the model does not meet the performance of context specific models nor extensible to contexts unseen at train time.  This necessitates a modification to the existing architecture in generating context specific weights so as to incorporate flexibility to multiple contexts. We propose a multiple acquisition context based network, called MAC-ReconNet for MRI reconstruction, flexible to multiple acquisition contexts and generalizable to unseen contexts for applicability in real scenarios. The proposed network has an MRI reconstruction module and a dynamic weight prediction (DWP) module.  The DWP module takes the corresponding acquisition context information  as  input  and  learns  the context-specific weights  of  the  reconstruction module which changes dynamically with context at run time.  We show that the proposed approach can handle multiple contexts  based on Cardiac and Brain datasets, Gaussian and Cartesian undersampling patterns and five acceleration factors. The proposed network outperforms the naive  jointly  trained model  and  gives  competitive results  with  the  context-specific  models both quantitatively and qualitatively.  We also demonstrate the generalizability of our model by testing on contexts unseen at train time.')
}}
{{ paper('Extending Unsupervised Neural Image Compression With Supervised Multitask Learning',
        'David Tellez, Diederik Hoppener, Cornelis Verhoef, Dirk Grunhagen, Pieter Nierop, Michal Drozdzal, Jeroen van der Laak, Francesco Ciompi',
        openreview='https://openreview.net/forum?id=oepOBj_A7E',
        pdf='https://openreview.net/pdf?id=oepOBj_A7E',
        id='O096',
        paper='papers/tellez20.html',
        teaser='https://youtu.be/GhW1qVGVit8',
        video='https://youtu.be/w48yYvYixCk',
        abstract='We focus on the problem of training convolutional neural networks on gigapixel histopathology images to predict image-level targets. For this purpose, we extend Neural Image Compression (NIC), an image compression framework that reduces the dimensionality of these images using an encoder network trained unsupervisedly. We propose to train this encoder using supervised multitask learning (MTL) instead. We applied the proposed MTL NIC to two histopathology datasets and three tasks. First, we obtained state-of-the-art results in the Tumor Proliferation Assessment Challenge of 2016 (TUPAC16). Second, we successfully classified histopathological growth patterns in images with colorectal liver metastasis (CLM). Third, we predicted patient risk of death by learning directly from overall survival in the same CLM data. Our experimental results suggest that the representations learned by the MTL objective are: (1) highly specific, due to the supervised training signal, and (2) transferable, since the same features perform well across different tasks. Additionally, we trained multiple encoders with different training objectives, e.g. unsupervised and variants of MTL, and observed a positive correlation between the number of tasks in MTL and the system performance on the TUPAC16 dataset.')
}}
{{ paper('Tensor Networks for Medical Image Classification',
        'Raghavendra Selvan, Erik B Dam',
        openreview='https://openreview.net/forum?id=jjk6bxk07G',
        pdf='https://openreview.net/pdf?id=jjk6bxk07G',
        id='O095',
        paper='papers/selvan20.html',
        teaser='https://youtu.be/w0YgIa2SxWk',
        video='https://youtu.be/CpBJVULSGiY',
        abstract='With the increasing adoption of machine learning tools like neural networks across several domains, interesting connections and comparisons to concepts from other domains are coming to light. In this work, we focus on the class of Tensor Networks, which has been a work horse for physicists in the last two decades to analyse quantum many-body systems. Building on the recent interest in tensor networks for machine learning, we extend the Matrix Product State tensor networks (which can be interpreted as linear classifiers operating in exponentially high dimensional spaces) to be useful in medical image analysis tasks. We focus on classification problems as a first step where we motivate the use of tensor networks and propose adaptions for 2D images using classical image domain concepts such as local orderlessness of images. With the proposed locally orderless tensor network model (LoTeNet), we show that tensor networks are capable of attaining performance that is comparable to state-of-the-art deep learning methods. We evaluate the model on two publicly available medical imaging datasets and show performance improvements with fewer model hyperparameters and lesser computational resources compared to relevant baseline methods.')
}}
[% / %]


---

## Outstanding reviewer Award

* Murat Ayhan
* Fausto Milletari
* Tanja Lossau
* Hoel Kervadec
* Saypraseuth Mounsaveng