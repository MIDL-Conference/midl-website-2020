---
title: "MIDL 2020 Tentative Program - Long"
---

{% from "_macros.html" import paper %}

# MIDL 2020 Program - Long

The conference main schedule will run in Montreal time (ET), [UTC-4](https://www.timeanddate.com/time/map/).

A short program overview in the [program at a glance](/dates.html), and you can subscribe to our [online calendar](/midl.ics).


## Monday July 6 - 8:00-15:00


### MON 8:00-8:30 UTC-4 - Openings + Prizes

### MON 8:30-9:30 UTC-4 - Oral Session #1 - Uncertainty

Session Chairs: Bjoern Menze, Qi Dou

[% .papers %]
{{ paper('Uncertainty-Aware Training of Neural Networks for Selective Medical Image Segmentation',
        'Yukun Ding, Jinglan Liu, Xiaowei Xu, Meiping Huang, Jian Zhuang, Jinjun Xiong, Yiyu Shi',
        openreview='https://openreview.net/forum?id=F1MIJCqX2J',
        pdf='https://openreview.net/pdf?id=F1MIJCqX2J',
        id='O102',
        paper='papers/ding20.html',
        teaser='',
        abstract='State-of-the-art deep learning based methods have achieved remarkable performance on medical image segmentation. Their applications in the clinical setting are, however, limited due to the lack of trustworthiness and reliability. Selective image segmentation has been proposed to address this issue by letting a DNN model process instances with high confidence while referring difficult ones with high uncertainty to experienced radiologists. As such, the model performance is only affected by the predictions on the high confidence subset rather than the whole dataset. Existing selective segmentation methods, however, ignore this unique property of selective segmentation and train their DNN models by optimizing accuracy on the entire dataset. Motivated by such a discrepancy, we present a novel method in this paper that considers such uncertainty in the training process to maximize the accuracy on the confident subset rather than the accuracy on the whole dataset. Experimental results using the whole heart and great vessel segmentation and gland segmentation show that such a training scheme can significantly improve the performance of selective segmentation. ')
}}
{{ paper('Uncertainty-based Graph Convolutional Networks for Organ Segmentation Refinement',
        'Roger D. Soberanis-Mukul, Nassir Navab, Shadi Albarqouni',
        openreview='https://openreview.net/forum?id=UUie86nf5B',
        pdf='https://openreview.net/pdf?id=UUie86nf5B',
        id='O146',
        paper='papers/soberanis--mukul20.html',
        teaser='',
        abstract="Organ segmentation in CT volumes is an important pre-processing step in many computer assisted intervention and diagnosis methods. In recent years, convolutional neural networks have dominated the state of the art in this task. However, since this problem presents a challenging environment due to high variability in the organ\\'s shape and similarity between tissues, the generation of false negative and false positive regions in the output segmentation is a common issue. Recent works have shown that the uncertainty analysis of the model can provide us with useful information about potential errors in the segmentation. In this context, we proposed a segmentation refinement method based on uncertainty analysis and graph convolutional networks. We employ the uncertainty levels of the convolutional network in a particular input volume to formulate a semi-supervised graph learning problem that is solved by training a graph convolutional network. To test our method we refine the initial output of a 2D U-Net. We validate our framework with the NIH pancreas dataset and the spleen dataset of the medical segmentation decathlon. We show that our method outperforms the state-of-the art CRF refinement method by improving the dice score by 1% for the pancreas and 2% for spleen, with respect to the original U-Net\\'s prediction. Finally, we discuss the results and current limitations of the model for future work in this research direction. For reproducibility purposes, we make our code publicly available")
}}
{{ paper('Well-Calibrated Regression Uncertainty in Medical Imaging with Deep Learning',
        'Max-Heinrich Laves, Sontje Ihler, Jacob F. Fast, Lüder A. Kahrs, Tobias Ortmaier',
        openreview='https://openreview.net/forum?id=CecZ_0t79q',
        pdf='https://openreview.net/pdf?id=CecZ_0t79q',
        id='O212',
        paper='papers/laves20.html',
        teaser='https://youtu.be/Wo6mZE3dBWI',
        abstract='The consideration of predictive uncertainty in medical imaging with deep learning is of utmost importance.      We apply estimation of predictive uncertainty by variational Bayesian inference with Monte Carlo dropout to regression tasks and show why predictive uncertainty is systematically underestimated.      We suggest to use $ \\sigma $ scaling with a single scalar value; a simple, yet effective calibration method for both aleatoric and epistemic uncertainty.      The performance of our approach is evaluated on a variety of common medical regression data sets using different state-of-the-art convolutional network architectures.      In all experiments, $ \\sigma $ scaling is able to reliably recalibrate predictive uncertainty, surpassing more complex calibration methods.      It is easy to implement and maintains the accuracy.      Well-calibrated uncertainty in regression allows robust rejection of unreliable predictions or detection of out-of-distribution samples.')
}}
[% / %]

---

### MON 9:30-11:00 UTC-4 - Poster Session #1

[% .papers %]
{{ paper('Uncertainty-Aware Training of Neural Networks for Selective Medical Image Segmentation',
        'Yukun Ding, Jinglan Liu, Xiaowei Xu, Meiping Huang, Jian Zhuang, Jinjun Xiong, Yiyu Shi',
        openreview='https://openreview.net/forum?id=F1MIJCqX2J',
        pdf='https://openreview.net/pdf?id=F1MIJCqX2J',
        id='O102',
        paper='papers/ding20.html',
        teaser='',
        abstract='State-of-the-art deep learning based methods have achieved remarkable performance on medical image segmentation. Their applications in the clinical setting are, however, limited due to the lack of trustworthiness and reliability. Selective image segmentation has been proposed to address this issue by letting a DNN model process instances with high confidence while referring difficult ones with high uncertainty to experienced radiologists. As such, the model performance is only affected by the predictions on the high confidence subset rather than the whole dataset. Existing selective segmentation methods, however, ignore this unique property of selective segmentation and train their DNN models by optimizing accuracy on the entire dataset. Motivated by such a discrepancy, we present a novel method in this paper that considers such uncertainty in the training process to maximize the accuracy on the confident subset rather than the accuracy on the whole dataset. Experimental results using the whole heart and great vessel segmentation and gland segmentation show that such a training scheme can significantly improve the performance of selective segmentation. ')
}}
{{ paper('Uncertainty-based Graph Convolutional Networks for Organ Segmentation Refinement',
        'Roger D. Soberanis-Mukul, Nassir Navab, Shadi Albarqouni',
        openreview='https://openreview.net/forum?id=UUie86nf5B',
        pdf='https://openreview.net/pdf?id=UUie86nf5B',
        id='O146',
        paper='papers/soberanis--mukul20.html',
        teaser='',
        abstract="Organ segmentation in CT volumes is an important pre-processing step in many computer assisted intervention and diagnosis methods. In recent years, convolutional neural networks have dominated the state of the art in this task. However, since this problem presents a challenging environment due to high variability in the organ\\'s shape and similarity between tissues, the generation of false negative and false positive regions in the output segmentation is a common issue. Recent works have shown that the uncertainty analysis of the model can provide us with useful information about potential errors in the segmentation. In this context, we proposed a segmentation refinement method based on uncertainty analysis and graph convolutional networks. We employ the uncertainty levels of the convolutional network in a particular input volume to formulate a semi-supervised graph learning problem that is solved by training a graph convolutional network. To test our method we refine the initial output of a 2D U-Net. We validate our framework with the NIH pancreas dataset and the spleen dataset of the medical segmentation decathlon. We show that our method outperforms the state-of-the art CRF refinement method by improving the dice score by 1% for the pancreas and 2% for spleen, with respect to the original U-Net\\'s prediction. Finally, we discuss the results and current limitations of the model for future work in this research direction. For reproducibility purposes, we make our code publicly available")
}}
{{ paper('Well-Calibrated Regression Uncertainty in Medical Imaging with Deep Learning',
        'Max-Heinrich Laves, Sontje Ihler, Jacob F. Fast, Lüder A. Kahrs, Tobias Ortmaier',
        openreview='https://openreview.net/forum?id=CecZ_0t79q',
        pdf='https://openreview.net/pdf?id=CecZ_0t79q',
        id='O212',
        paper='papers/laves20.html',
        teaser='https://youtu.be/Wo6mZE3dBWI',
        abstract='The consideration of predictive uncertainty in medical imaging with deep learning is of utmost importance.      We apply estimation of predictive uncertainty by variational Bayesian inference with Monte Carlo dropout to regression tasks and show why predictive uncertainty is systematically underestimated.      We suggest to use $ \\sigma $ scaling with a single scalar value; a simple, yet effective calibration method for both aleatoric and epistemic uncertainty.      The performance of our approach is evaluated on a variety of common medical regression data sets using different state-of-the-art convolutional network architectures.      In all experiments, $ \\sigma $ scaling is able to reliably recalibrate predictive uncertainty, surpassing more complex calibration methods.      It is easy to implement and maintains the accuracy.      Well-calibrated uncertainty in regression allows robust rejection of unreliable predictions or detection of out-of-distribution samples.')
}}
[% / %]

[% .papers %]
{{ paper('3D-RADNet: Extracting labels from DICOM metadata for training general medical domain deep 3D convolution neural networks',
        'Richard Du, Varut Vardhanabhuti',
        openreview='https://openreview.net/forum?id=CCbuElJreP',
        pdf='https://openreview.net/pdf?id=CCbuElJreP',
        id='P114',
        paper='papers/du20.html',
        teaser='https://youtu.be/6pRjwuIsedk',
        abstract='Training deep convolution neural network requires a large amount of data to obtain good performance and generalisable results. Transfer learning approaches from datasets such as ImageNet had become important in increasing accuracy and lowering training samples required. However, as of now, there has not been a popular dataset for training 3D volumetric medical images. This is mainly due to the time and expert knowledge required to accurately annotate medical images. In this study, we present a method in extracting labels from DICOM metadata that information on the appearance of the scans to train a medical domain 3D convolution neural network. The labels include imaging modalities and sequences, patient orientation and view, presence of contrast agent, scan target and coverage, and slice spacing. We applied our method and extracted labels from a large amount of cancer imaging dataset from TCIA to train a medical domain 3D deep convolution neural network. We evaluated the effectiveness of using our proposed network in transfer learning a liver segmentation task and found that our network achieved superior segmentation performance (DICE=90.0%) compared to training from scratch (DICE=41.8%). Our proposed network shows promising results to be used as a backbone network for transfer learning to another task. Our approach along with the utilising our network, can potentially be used to extract features from large-scale unlabelled DICOM datasets.')
}}
{{ paper('Pathology GAN: Learning deep representations of cancer tissue',
        'Adalberto Claudio Quiros, Roderick Murray-Smith, Ke Yuan',
        openreview='https://openreview.net/forum?id=CwgSEEQkad',
        pdf='https://openreview.net/pdf?id=CwgSEEQkad',
        id='P150',
        paper='papers/quiros20.html',
        teaser='https://youtu.be/wGx78e1mHQQ',
        abstract='We apply Generative Adversarial Networks (GANs) to the domain of digital pathology. Current machine learning research for digital pathology focuses on diagnosis, but we suggest a different approach and advocate that generative models could drive forward the understanding of morphological characteristics of cancer tissue. In this paper, we develop a framework which allows GANs to capture key tissue features and uses these characteristics to give structure to its latent space. To this end, we trained our model on 249K H&E breast cancer tissue images.          We show that our model generates high quality images, with a Frechet Inception Distance (FID) of 16.65. We additionally assess the quality of the images with cancer tissue characteristics (e.g. count of cancer, lymphocytes, or stromal cells), using quantitative information to calculate the FID and showing consistent performance of 9.86. Additionally, the latent space of our model shows an interpretable structure and allows semantic vector operations that translate into tissue feature transformations. Furthermore, ratings from two expert pathologists found no significant difference between our generated tissue images from real ones.')
}}
{{ paper('Accurate Detection of Out of Body Segments in Surgical Video using Semi-Supervised Learning',
        'Maya Zohar, Omri Bar, Daniel Neimark, Gregory D. Hager, Dotan Asselmann',
        openreview='https://openreview.net/forum?id=k-ANsPQJxY',
        pdf='https://openreview.net/pdf?id=k-ANsPQJxY',
        id='P157',
        paper='papers/zohar20.html',
        teaser='https://youtu.be/2-c8hAMEAEo',
        abstract='Large labeled datasets are an important precondition for deep learning models to achieve state-of-the-art results in computer vision tasks. In the medical imaging domain, privacy concerns have limited the rate of adoption of artificial intelligence methodologies into clinical practice. To alleviate such concerns, and increase comfort levels while sharing and storing surgical video data, we propose a high accuracy method for rapid removal and anonymization of out-of-body and non-relevant surgery segments. Training a deep model to detect out-of-body and non-relevant segments in surgical videos requires suitable labeling. Since annotating surgical videos with per-second relevancy labeling is a tedious task, our proposed framework initiates the learning process from a weakly labeled noisy dataset and iteratively applies Semi-Supervised Learning (SSL) to re-annotate the training data samples. Evaluating our model, on an independent test set, shows a mean detection accuracy of above 97% after several training-annotating iterations. Since our final goal is achieving out-of-body segments detection for anonymization, we evaluate our ability to detect these segments at a high demanding recall of 97%, which leads to a precision of 83.5%. We believe this approach can be applied to similar related medical problems, in which only a coarse set of relevancy labels exists, currently limiting the possibility for supervision training.')
}}
{{ paper('Joint Learning of Vessel Segmentation and Artery/Vein Classification with Post-processing',
        'Liangzhi Li, Manisha Verma, Yuta Nakashima, Ryo Kawasaki, Hajime Nagahara',
        openreview='https://openreview.net/forum?id=O9QVJh8eMX',
        pdf='https://openreview.net/pdf?id=O9QVJh8eMX',
        id='P163',
        paper='papers/li20.html',
        teaser='https://youtu.be/-ky4pCXzCUE',
        abstract='Retinal imaging serves as a valuable tool for diagnosis of various diseases. However, reading retinal images is a difficult and time-consuming task even for experienced specialists. The fundamental step towards automated retinal image analysis is vessel segmentation and artery/vein classification, which provide various information on potential disorders. To improve the performance of the existing automated methods for retinal image analysis, we propose a two-step vessel classification. We adopt a UNet-based model, SeqNet, to accurately segment vessels from the background and make prediction on the vessel type. Our model does segmentation and classification sequentially, which alleviates the problem of label distribution bias and facilitates training. To further refine classification results, we post-process them considering the structural information among vessels to propagate highly confident prediction to surrounding vessels. Our experiments show that our method improves AUC to 0.98 for segmentation and the accuracy to 0.92 in classification over DRIVE dataset.')
}}
{{ paper('Comparing Objective Functions for Segmentation and Detection of Tiny Lesions in Retinal Images',
        'Jakob Kristian Holm Andersen, Thiusius Rajeeth Savarimuthu, Jakob Grauslund',
        openreview='https://openreview.net/forum?id=TC_eOaPKBB',
        pdf='https://openreview.net/pdf?id=TC_eOaPKBB',
        id='P174',
        paper='papers/andersen20.html',
        teaser='https://youtu.be/w8zGGamA3Ao',
        abstract='Retinal microaneurysms (MAs) are the earliest signs of diabetic retinopathy (DR) which is  the  leading  cause  of  blindness  in  the  western  world.   MAs  independently  predict  the risk of sight threatening DR and early detection is important to identify patients at risk. Detection and segmentation of retinal MAs present a particular challenging problem due to  a  large  class  imbalance  with  MA  pixels  accounting  for  less  than  0.5%  of  the  retinal image.  Extreme foreground-background class imbalance can adversely affect the learning process in DNNs by introducing a bias towards the most well represented class.  Recently, a number of objective functions have been proposed as alternatives to the standard Crossentropy loss in efforts to overcome this problem.  In this work we investigate the influence of  the  network  objective  during  optimization  by  comparing  Residual  U-nets  trained  for segmentation of MAs in retinal images using seven different objective functions; weighted and unweighted Crossentropy loss, Dice loss, weighted and unweighted Focal loss, Focal Dice loss and Focal Tversky loss.  Three networks with different seeds are trained for each objective function using optimized hyper-parameter settings on a dataset of 382 images with pixel level annotations for MAs.  The instance level MA detection performance is evaluated as the average free response receiver operator characteristic (FROC) score calculated as the mean sensitivity at seven average false positives (FPAvg) per image thresholds on 80 test images.  The image level MA detection performance is evaluated as the average AUC on the same images as well as a separate test set of 1200 images.  Segmentation performance is  evaluated  as  the  average  pixel  precision  (AP).  The  unweighted  Crossentropy  loss  and Focal loss outperforms all other losses for instance level detection achieving FROC scores of  0.5067(±0.0115)  and  0.5062(±0.0045.   The  Focal  loss  has  the  highest  pixel  precision with an AP of 0.4254(±0.0096).  For image level detection both objective functions in their unweighted form perform significantly better compared to using all other objectives.  AUCs of 0.9450(±0.0080) and 0.8351(±0.0039) on the two test are achieved using the unweighted Crossentropy  loss,  while  AUCs  for  the  unweighted  Focal  loss  was  0.9375(±0.0074)  and 0.8253(±0.0042) respectivly.      Conclusion:      Despite the promise of using training objectives designed to deal with unbalanced data, the standard Crossentropy loss perform at least as well or better than all other objective functions in our experiments for lesion level and image level detection for small  retinal  MAs.   While  a  number  of  newer  objective  functions  have  been  introduced and shown to improve performance for unbalanced datasets compared to the Dice loss in recent years, our results suggest that it is important to also benchmark new losses against the Crossentropy or Focal loss function, as we achieve the best performance in all our test using these objectives.')
}}
{{ paper('Deep learning-based parameter mapping for joint relaxation and diffusion tensor MR Fingerprinting',
        'Carolin M. Pirkl, Pedro A. Gómez, Ilona Lipp, Guido Buonincontri, Miguel Molina-Romero, Anjany Sekuboyina, Diana Waldmannstetter, Jonathan Dannenberg, Sebastian Endt, Alberto Merola, Joseph R. Whittaker, Valentina Tomassini, Michela Tosetti, Derek K. Jones, Bjoern H. Menze, Marion I. Menzel',
        openreview='https://openreview.net/forum?id=wthvY6Y9e',
        pdf='https://openreview.net/pdf?id=wthvY6Y9e',
        id='P182',
        paper='papers/pirkl20.html',
        teaser='https://youtu.be/SMIQgihtEWE',
        abstract='Magnetic Resonance Fingerprinting (MRF) enables the simultaneous quantification of multiple properties of biological tissues. It relies on a pseudo-random acquisition and the matching of acquired signal evolutions to a precomputed dictionary. However, the dictionary is not scalable to higher-parametric spaces, limiting MRF to the simultaneous mapping of only a small number of parameters (proton density, T1 and T2 in general). Inspired by diffusion-weighted SSFP imaging, we present a proof-of-concept of a novel MRF sequence with embedded diffusion-encoding gradients along all three axes to efficiently encode orientational diffusion and T1 and T2 relaxation. We take advantage of a convolutional neural network (CNN) to reconstruct multiple quantitative maps from this single, highly undersampled acquisition. We bypass expensive dictionary matching by learning the implicit physical relationships between the spatiotemporal MRF data and the T1, T2 and diffusion tensor parameters. The predicted parameter maps and the derived scalar diffusion metrics agree well with state-of-the-art reference protocols. Orientational diffusion information is captured as seen from the estimated primary diffusion directions. In addition to this, the joint acquisition and reconstruction framework proves capable of preserving tissue abnormalities in multiple sclerosis lesions.')
}}
{{ paper('Fusing Structural and Functional MRIs using Graph Convolutional Networks for Autism Classification',
        'Devanshu Arya, Richard Olij, Deepak K. Gupta, Ahmed El Gazzar, Guido van Wingen, Marcel Worring, Rajat Mani Thomas',
        openreview='https://openreview.net/forum?id=EKu4FU5s4',
        pdf='https://openreview.net/pdf?id=EKu4FU5s4',
        id='P183',
        paper='papers/arya20.html',
        teaser='https://youtu.be/91XLs_yrfbo',
        abstract='Geometric deep learning methods such as graph convolutional networks have recently proven to deliver generalized solutions in disease prediction using medical imaging. In this paper, we focus particularly on their use in autism classification. Most of the recent methods use graphs to leverage phenotypic information about subjects (patients or healthy controls) as additional contextual information. To do so, metadata such as age, gender and acquisition sites are utilized to define intricate relations (edges) between the subjects. We alleviate the use of such non-imaging metadata and propose a fully imaging-based approach where information from structural and functional Magnetic Resonance Imaging (MRI) data are fused to construct the edges and nodes of the graph. To characterize each subject, we employ brain summaries. These are 3D images obtained from the 4D spatiotemporal resting-state fMRI data through summarization of the temporal activity of each voxel using neuroscientifically informed temporal measures such as amplitude low frequency fluctuations and entropy. Further, to extract features from these 3D brain summaries, we propose a 3D CNN model. We perform analysis on the open dataset for autism research (full ABIDE I-II) and show that by using simple brain summary measures and incorporating sMRI information, there is a noticeable increase in the generalizability and performance values of the framework as compared to state-of-the-art graph-based models.')
}}
{{ paper('A Cross-Stitch Architecture for Joint Registration and Segmentation in Adaptive Radiotherapy',
        'Laurens Beljaards, Mohamed S. Elmahdy, Fons Verbeek, Marius Staring',
        openreview='https://openreview.net/forum?id=oFXY64JJQ8',
        pdf='https://openreview.net/pdf?id=oFXY64JJQ8',
        id='P197',
        paper='papers/beljaards20.html',
        teaser='https://youtu.be/N8r5sl3ujWU',
        abstract='Recently, joint registration and segmentation has been formulated in a deep learning setting, by the definition of joint loss functions. In this work, we investigate joining these tasks at the architectural level. We propose a registration network that integrates segmentation propagation between images, and a segmentation network to predict the segmentation directly. These networks are connected into a single joint architecture via so-called cross- stitch units, allowing information to be exchanged between the tasks in a learnable manner. The proposed method is evaluated in the context of adaptive image-guided radiotherapy, using daily prostate CT imaging. Two datasets from different institutes and manufacturers were involved in the study. The first dataset was used for training (12 patients) and validation (6 patients), while the second dataset was used as an independent test set (14 patients). In terms of mean surface distance, our approach achieved 1.06 ± 0.3 mm, 0.91 ± 0.4 mm, 1.27 ± 0.4 mm, and 1.76 ± 0.8 mm on the validation set and 1.82 ± 2.4 mm, 2.45 ± 2.4 mm, 2.45 ± 5.0 mm, and 2.57 ± 2.3 mm on the test set for the prostate, bladder, seminal vesicles, and rectum, respectively. The proposed multi-task network outperformed single-task networks, as well as a network only joined through the loss function, thus demonstrating the capability to leverage the individual strengths of the segmentation and registration tasks. The obtained performance as well as the inference speed make this a promising candidate for daily re-contouring in adaptive radiotherapy, potentially reducing treatment-related side effects and improving quality-of-life after treatment.')
}}
{{ paper('Automatic Segmentation of Head and Neck Tumors and Nodal Metastases in PET-CT scans',
        'Vincent Andrearczyk, Valentin Oreiller, Martin Vallières, Joel Castelli, Hesham Elhalawani, Sarah Boughdad, Mario Jreige, John O. Prior and Adrien Depeursinge',
        openreview='https://openreview.net/forum?id=1Ql71nEERx',
        pdf='https://openreview.net/pdf?id=1Ql71nEERx',
        id='P205',
        paper='papers/andrearczyk20.html',
        teaser='https://youtu.be/t0IWfoGVpoc',
        abstract='Radiomics, the prediction of disease characteristics using quantitative image biomarkers from medical images, relies on expensive manual annotations of Regions of Interest (ROI) to focus the analysis. In this paper, we propose an automatic segmentation of Head and Neck (H&N) tumors and nodal metastases from FDG-PET and CT images. A fully-convolutional network (2D and 3D V-Net) is trained on PET-CT images using ground truth ROIs that were manually delineated by radiation oncologists for 202 patients. The results show the complementarity of the two modalities with a statistically significant improvement from 48.7% and 58.2% Dice Score Coefficients (DSC) with CT- and PET-only segmentation respectively, to 60.6% with a bimodal late fusion approach. We also note that, on this task, a 2D implementation slightly outperforms a similar 3D design (60.6% vs 59.7% for the best results respectively). The data is publicly available and the code will be shared on our GitHub repository.')
}}
{{ paper('Direct estimation of fetal head circumference from ultrasound images based on regression CNN',
        'Jing Zhang, Caroline Petitjean, Pierre Lopez, Samia Ainouz',
        openreview='https://openreview.net/forum?id=RwYqA6AjS',
        pdf='https://openreview.net/pdf?id=RwYqA6AjS',
        id='P222',
        paper='papers/zhang20c.html',
        teaser='https://youtu.be/y-iXek-lMjE',
        abstract='The measurement of fetal head circumference (HC) is performed throughout the pregnancy as a key biometric to monitor fetus growth. This measurement is performed on ultrasound images, via the manual fitting of an ellipse. The operation is operator-dependent and as such prone to intra and inter-variability error. There have been attempts to design automated segmentation algorithms to segment fetal head, especially based on deep encoding-decoding architectures. In this paper, we depart from this idea and propose to leverage the ability of convolutional neural networks (CNN) to directly measure the head circumference, without having to resort to handcrafted features or manually labeled segmented images. The intuition behind this idea is that the CNN will  learn itself to localize and identify the head contour. Our approach is experimented on the public HC18 dataset, that contains images of all trimesters of the pregnancy. We investigate various architectures and three losses suitable for regression. While room for improvement is left, encouraging results show that it might be possible in the future to directly estimate the HC - without the need for a large dataset of manually segmented ultrasound images. This approach might be extended to other applications where segmentation is just an intermediate step to the computation of biomarkers.')
}}
[% / %]

[% .papers %]
{{ paper('A CNN-LSTM Architecture for Detection of Intracranial Hemorrhage on CT scans',
        'Nhan T. Nguyen, Dat Q. Tran, Nghia T. Nguyen, Ha Q. Nguyen',
        openreview='https://openreview.net/forum?id=1IoPbyuPFT',
        pdf='https://openreview.net/pdf?id=1IoPbyuPFT',
        id='S041',
        paper='papers/nguyen20.html',
        teaser='https://youtu.be/rZuYAKt26fo',
        abstract='We propose a novel method that combines a convolutional neural network (CNN) with a long short-term memory (LSTM) mechanism for accurate prediction of intracranial hemorrhage on computed tomography (CT) scans. The CNN plays the role of a slice-wise feature extractor while the LSTM is responsible for linking the features across slices. The whole architecture is trained end-to-end with input being an RGB-like image formed by stacking 3 different viewing windows of a single slice. We validate the method on the recent RSNA Intracranial Hemorrhage Detection challenge and on the CQ500 dataset. For the RSNA challenge, our best single model achieves a weighted log loss of 0.0529 on the leaderboard, which is comparable to the top 3\\% performances, almost all of which make use of ensemble learning. Importantly, our method generalizes very well: the model trained on the RSNA dataset significantly outperforms the 2D model, which does not take into account the relationship between slices, on CQ500. Our codes and models will be made public.')
}}
{{ paper('DeepRetinotopy: Predicting the Functional Organization of Human Visual Cortex from Structural MRI Data using Geometric Deep Learning',
        'Fernanda L. Ribeiro, Steffen Bollmann, Alexander M. Puckett',
        openreview='https://openreview.net/forum?id=Nw_trRFjPE',
        pdf='https://openreview.net/pdf?id=Nw_trRFjPE',
        id='S073',
        paper='papers/ribeiro20.html',
        teaser='https://youtu.be/kwHoPnCDvTk',
        abstract='Whether it be in a man-made machine or a biological system, form and function are often directly related. In the latter, however, this particular relationship is often unclear due to the intricate nature of biology. Here we developed a geometric deep learning model capable of exploiting the actual structure of the cortex to learn the complex relationship between brain function and anatomy from structural and functional MRI data. Our model was not only able to predict the functional organization of human visual cortex from anatomical properties alone, but it was also able to predict nuanced variations across individuals.')
}}
{{ paper('Pulmonary Nodule Malignancy Classification Using its Temporal Evolution with Two-Stream 3D Convolutional Neural Networks',
        'Xavier Rafael-Palou, Anton Aubanell, Ilaria Bonavita, Mario Ceresa, Gemma Piella, Vicent Ribas, Miguel Ángel González Ballester',
        openreview='https://openreview.net/forum?id=D1jTt_FOPY',
        pdf='https://openreview.net/pdf?id=D1jTt_FOPY',
        id='S094',
        paper='papers/rafael-palou20.html',
        teaser='https://youtu.be/ifUQ8CBSUkQ',
        abstract='Nodule malignancy assessment is a complex, time-consuming and error-prone task.  Current clinical practice requires measuring changes in size and density of the nodule at different time-points.  State of the art solutions rely on 3D convolutional neural networks built on pulmonary nodules obtained from a single CT scan per patient.  In this work, we propose a two-stream 3D convolutional neural network that predicts malignancy by jointly analyzing two pulmonary nodule volumes from the same patient taken at different time-points.  Best results achieve 77% of F1-score in test with an increment of 9% and 12% of F1-score with respect to the same network trained with images from a single time-point.')
}}
{{ paper('Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion',
        'Milan Decuyper, Stijn Bonte, Karel Deblaere, Roel Van Holen',
        openreview='https://openreview.net/forum?id=J5iep2t90F',
        pdf='https://openreview.net/pdf?id=J5iep2t90F',
        id='S116',
        paper='papers/decuyper20.html',
        teaser='https://youtu.be/HmU_h8GaUQM',
        abstract='In the WHO glioma classification guidelines grade, IDH mutation and 1p19q co-deletion play a central role as they are important markers for prognosis and optimal therapy planning. Therefore, we propose a fully automatic, MRI based, 3D pipeline for glioma segmentation and classification. The designed segmentation network was a 3D U-Net achieving an average whole tumor dice score of 90%. After segmentation, the 3D tumor ROI is extracted and fed into the multi-task classification network. The network was trained and evaluated on a large heterogeneous dataset of 628 patients, collected from The Cancer Imaging Archive and BraTS 2019 databases. Additionally, the network was validated on an independent dataset of 110 patients retrospectively acquired at the Ghent University Hospital (GUH). Classification AUC scores are 0.93, 0.94 and 0.82 on the TCIA test data and 0.94, 0.86 and 0.87 on the GUH data for grade, IDH and 1p19q status respectively. ')
}}
{{ paper('On the effectiveness of GAN generated cardiac MRIs for segmentation',
        'Youssef Skandarani, Nathan Painchaud, Pierre-Marc Jodoin, Alain Lalande',
        openreview='https://openreview.net/forum?id=f9Pl3Qj3_Q',
        pdf='https://openreview.net/pdf?id=f9Pl3Qj3_Q',
        id='S118',
        paper='papers/skandarani20.html',
        teaser='https://youtu.be/lIVWmPNFG1E',
        abstract='In this work, we propose a Variational Autoencoder (VAE) - Generative Adversarial Networks (GAN) model that can produce highly realistic MRI together with its pixel accurate groundtruth for the application of cine-MR image cardiac segmentation.  On one side of our model is a Variational Autoencoder (VAE) trained to learn the latent representations of cardiac shapes.  On the other side is a GAN that uses  ”SPatially-Adaptive (DE)Normalization” (SPADE) modules to generate realistic MR images tailored to a given anatomical map.  At test time, the sampling of the VAE latent space allows to generate an arbitrary large number of cardiac shapes, which are fed to the GAN that subsequently generates MR images whose cardiac structure fits that of the cardiac shapes.  In other words, our system can generate a large volume of realistic yet labeled cardiac MR images.  We show that segmentation with CNNs trained with our synthetic annotated images gets competitive results compared to traditional techniques.      We also show that combining data augmentation with our GAN-generated images lead to an improvement in the Dice score of up to 12 percent while allowing for better generalization capabilities on  other datasets.')
}}
{{ paper('Data-Driven Prediction of Embryo Implantation Probability Using IVF Time-lapse Imaging',
        'David H. Silver, Martin Feder, Yael Gold-Zamir, Avital L. Polsky, Shahar Rosentraub, Efrat Shachor, Adi Weinberger, Pavlo Mazur, Valery D. Zukin, Alex M. Bronstein',
        openreview='https://openreview.net/forum?id=TujK1uTkTP',
        pdf='https://openreview.net/pdf?id=TujK1uTkTP',
        id='S126',
        paper='papers/silver20.html',
        teaser='https://youtu.be/Jg8Aq4BuXI8',
        abstract='The process of fertilizing a human egg outside the body in order to help those suffering from infertility to conceive is known as in vitro fertilization (IVF). Despite being the most effective method of assisted reproductive technology (ART), the average success rate of IVF is a mere 20-40%. One step that is critical to the success of the procedure is selecting which embryo to transfer to the patient, a process typically conducted manually and without any universally accepted and standardized criteria. In this paper we describe a novel data-driven system trained to directly predict embryo implantation probability from embryogenesis time-lapse imaging videos. Using  retrospectively collected videos from 272 embryos, we demonstrate that, when compared to an external panel of embryologists, our algorithm results in a 12% increase of positive predictive value and a 29% increase of negative predictive value. ')
}}
{{ paper('Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies',
        'Mattias P Heinrich, Lasse Hansen',
        openreview='https://openreview.net/forum?id=wbZM-DcJB9',
        pdf='https://openreview.net/pdf?id=wbZM-DcJB9',
        id='S131',
        paper='papers/heinrich20.html',
        teaser='https://youtu.be/MvcUYnalf4U',
        abstract='Multimodal image registration is a very challenging problem for deep learning approaches. Most current work focuses on either supervised learning that requires labelled training scans and may yield models that bias towards annotated structures or unsupervised approaches that are based on hand-crafted similarity metrics and may therefore not outperform their classical non-trained counterparts. We believe that unsupervised domain adaptation can be beneficial in overcoming the current limitations for multimodal registration, where good metrics are hard to define.      Domain adaptation has so far been mainly limited to classification problems. We propose the first use of unsupervised domain adaptation for discrete multimodal registration. Based on a source domain for which quantised displacement labels are available as supervision, we transfer the output distribution of the network to better resemble the target domain (other modality) using classifier discrepancies. To improve upon the sliced Wasserstein metric for 2D histograms, we present a novel approximation that projects predictions into 1D and computes the L1 distance of their cumulative sums. Our proof-of-concept demonstrates the applicability of domain transfer from mono- to multimodal 2D registration of canine MRI scans and improves the registration accuracy from 33% (using sliced Wasserstein) to 44%.')
}}
{{ paper('Functional Space Variational Inference for Uncertainty Estimation in Computer Aided Diagnosis',
        'Pranav Poduval, Hrushikesh Loya, Amit Sethi',
        openreview='https://openreview.net/forum?id=eLL-c_Xc0B',
        pdf='https://openreview.net/pdf?id=eLL-c_Xc0B',
        id='S310',
        paper='papers/poduval20.html',
        teaser='https://youtu.be/OI3GMnka7Mw',
        abstract='Deep neural networks have revolutionized medical image analysis and disease diagnosis. Despite their impressive performance, it is diﬃcult to generate well-calibrated probabilistic outputs for such networks, which makes them uninterpretable black boxes. Bayesian neural networks provide a principled approach for modelling uncertainty and increasing patient safety, but they have a large computational overhead and provide limited improvement in calibration. In this work, by taking skin lesion classiﬁcation as an example task, we show that by shifting Bayesian inference to the functional space we can craft meaningful priors that give better-calibrated uncertainty estimates at a much lower computational cost')
}}
[% / %]

---

### MON 11:00-12:00 UTC-4 - Keynote #1 - Alan Evans


### MON 12:00-12:30 UTC-4 - Break

---

### MON 12:30-13:30 UTC-4 - Oral Session #2 - Limited Data

Session Chairs: J. Eugenio Iglesias, Caroline Petitjean

[% .papers %]
{{ paper('Bounding boxes for weakly supervised segmentation: Global constraints get close to full supervision',
        'Hoel Kervadec, Jose Dolz, Shanshan Wang, Eric Granger, Ismail Ben Ayed',
        openreview='https://openreview.net/forum?id=m7HZ-yil_-',
        pdf='https://openreview.net/pdf?id=m7HZ-yil_-',
        id='O001',
        paper='papers/kervadec20.html',
        teaser='',
        abstract='We propose a novel weakly supervised learning segmentation based on several global constraints derived from box annotations. Particularly, we leverage a classical tightness prior to a deep learning setting via imposing a set of constraints on the network outputs. Such a powerful topological prior prevents solutions from excessive shrinking by enforcing any horizontal or vertical line within the bounding box to contain, at least, one pixel of the foreground region. Furthermore, we integrate our deep tightness prior with a global background emptiness constraint, guiding training with information outside the bounding box. We demonstrate experimentally that such a global constraint is much more powerful than standard cross-entropy for the background class. Our optimization problem is challenging as it takes the form of a large set of inequality constraints on the outputs of deep networks. We solve it with sequence of unconstrained losses based on a recent powerful extension of the log-barrier method, which is well-known in the context of interior-point methods. This accommodates standard stochastic gradient descent (SGD) for training deep networks, while avoiding computationally expensive and unstable Lagrangian dual steps and projections. Extensive experiments over two different public data sets and applications (prostate and brain lesions) demonstrate that the synergy between our global tightness and emptiness priors yield very competitive performances, approaching full supervision and outperforming significantly DeepCut. Furthermore, our approach removes the need for computationally expensive proposal generation. Our code is shared anonymously.   ')
}}
{{ paper('DIVA: Domain Invariant Variational Autoencoder',
        'Maximilian Ilse, Jakub M. Tomczak, Christos Louizos, Max Welling',
        openreview='https://openreview.net/forum?id=RmNckVums7',
        pdf='https://openreview.net/pdf?id=RmNckVums7',
        id='O043',
        paper='papers/ilse20.html',
        teaser='',
        abstract='We consider the problem of domain generalization, namely, how to learn representations given data from a set of domains that generalize to data from a previously unseen domain. We propose the Domain Invariant Variational Autoencoder (DIVA), a generative model that tackles this problem by learning three independent latent subspaces, one for the domain, one for the class, and one for any residual variations. We highlight that due to the generative nature of our model we can also incorporate unlabeled data from known or previously unseen domains. To the best of our knowledge this has not been done before in a domain generalization setting. This property is highly desirable in fields like medical imaging where labeled data is scarce. We experimentally evaluate our model on the rotated MNIST benchmark and a malaria cell images dataset where we show that (i) the learned subspaces are indeed complementary to each other, (ii) we improve upon recent works on this task and (iii) incorporating unlabelled data can boost the performance even further.')
}}
{{ paper('A learning strategy for contrast-agnostic MRI segmentation',
        'Benjamin Billot, Douglas N. Greve, Koen Van Leemput, Bruce Fischl, Juan Eugenio Iglesias, Adrian V. Dalca',
        openreview='https://openreview.net/forum?id=Qz2DgRQGlP',
        pdf='https://openreview.net/pdf?id=Qz2DgRQGlP',
        id='O072',
        paper='papers/billot20.html',
        teaser='https://youtu.be/ewKD9UqwUDk',
        abstract='We present a deep learning strategy for contrast-agnostic semantic segmentation of unpreprocessed brain MRI scans, without requiring additional training or fine-tuning for new modalities. Classical Bayesian methods address this segmentation problem with unsupervised intensity models, but require significant computational resources. In contrast, learning-based methods can be fast at test time, but are sensitive to the data available at training. Our proposed learning method, SynthSeg, leverages a set of training segmentations (no intensity images required) to generate synthetic scans of widely varying contrasts on the fly during training. These scans are produced using the generative model of the classical Bayesian segmentation framework, with randomly sampled parameters for appearance, deformation, noise, and bias field. Because each mini-batch has a different synthetic contrast, the final network is not biased towards any specific MRI contrast. We comprehensively evaluate our approach on four datasets comprising over 1,000 subjects and four MR contrasts. The results show that our approach successfully segments every contrast in the data, performing slightly better than classical Bayesian segmentation, and three orders of magnitude faster. Moreover, even within the same type of MRI contrast, our strategy generalizes significantly better across datasets, compared to training using real images. Finally, we find that synthesizing a broad range of contrasts, even if unrealistic, increases the generalization of the neural network. Our code and model are open source at https://github.com/BBillot/SynthSeg.')
}}
[% / %]

---

### MON 13:30-15:00 UTC-4 - Poster Session #2

[% .papers %]
{{ paper('Bounding boxes for weakly supervised segmentation: Global constraints get close to full supervision',
        'Hoel Kervadec, Jose Dolz, Shanshan Wang, Eric Granger, Ismail Ben Ayed',
        openreview='https://openreview.net/forum?id=m7HZ-yil_-',
        pdf='https://openreview.net/pdf?id=m7HZ-yil_-',
        id='O001',
        paper='papers/kervadec20.html',
        teaser='',
        abstract='We propose a novel weakly supervised learning segmentation based on several global constraints derived from box annotations. Particularly, we leverage a classical tightness prior to a deep learning setting via imposing a set of constraints on the network outputs. Such a powerful topological prior prevents solutions from excessive shrinking by enforcing any horizontal or vertical line within the bounding box to contain, at least, one pixel of the foreground region. Furthermore, we integrate our deep tightness prior with a global background emptiness constraint, guiding training with information outside the bounding box. We demonstrate experimentally that such a global constraint is much more powerful than standard cross-entropy for the background class. Our optimization problem is challenging as it takes the form of a large set of inequality constraints on the outputs of deep networks. We solve it with sequence of unconstrained losses based on a recent powerful extension of the log-barrier method, which is well-known in the context of interior-point methods. This accommodates standard stochastic gradient descent (SGD) for training deep networks, while avoiding computationally expensive and unstable Lagrangian dual steps and projections. Extensive experiments over two different public data sets and applications (prostate and brain lesions) demonstrate that the synergy between our global tightness and emptiness priors yield very competitive performances, approaching full supervision and outperforming significantly DeepCut. Furthermore, our approach removes the need for computationally expensive proposal generation. Our code is shared anonymously.   ')
}}
{{ paper('DIVA: Domain Invariant Variational Autoencoder',
        'Maximilian Ilse, Jakub M. Tomczak, Christos Louizos, Max Welling',
        openreview='https://openreview.net/forum?id=RmNckVums7',
        pdf='https://openreview.net/pdf?id=RmNckVums7',
        id='O043',
        paper='papers/ilse20.html',
        teaser='',
        abstract='We consider the problem of domain generalization, namely, how to learn representations given data from a set of domains that generalize to data from a previously unseen domain. We propose the Domain Invariant Variational Autoencoder (DIVA), a generative model that tackles this problem by learning three independent latent subspaces, one for the domain, one for the class, and one for any residual variations. We highlight that due to the generative nature of our model we can also incorporate unlabeled data from known or previously unseen domains. To the best of our knowledge this has not been done before in a domain generalization setting. This property is highly desirable in fields like medical imaging where labeled data is scarce. We experimentally evaluate our model on the rotated MNIST benchmark and a malaria cell images dataset where we show that (i) the learned subspaces are indeed complementary to each other, (ii) we improve upon recent works on this task and (iii) incorporating unlabelled data can boost the performance even further.')
}}
{{ paper('A learning strategy for contrast-agnostic MRI segmentation',
        'Benjamin Billot, Douglas N. Greve, Koen Van Leemput, Bruce Fischl, Juan Eugenio Iglesias, Adrian V. Dalca',
        openreview='https://openreview.net/forum?id=Qz2DgRQGlP',
        pdf='https://openreview.net/pdf?id=Qz2DgRQGlP',
        id='O072',
        paper='papers/billot20.html',
        teaser='https://youtu.be/ewKD9UqwUDk',
        abstract='We present a deep learning strategy for contrast-agnostic semantic segmentation of unpreprocessed brain MRI scans, without requiring additional training or fine-tuning for new modalities. Classical Bayesian methods address this segmentation problem with unsupervised intensity models, but require significant computational resources. In contrast, learning-based methods can be fast at test time, but are sensitive to the data available at training. Our proposed learning method, SynthSeg, leverages a set of training segmentations (no intensity images required) to generate synthetic scans of widely varying contrasts on the fly during training. These scans are produced using the generative model of the classical Bayesian segmentation framework, with randomly sampled parameters for appearance, deformation, noise, and bias field. Because each mini-batch has a different synthetic contrast, the final network is not biased towards any specific MRI contrast. We comprehensively evaluate our approach on four datasets comprising over 1,000 subjects and four MR contrasts. The results show that our approach successfully segments every contrast in the data, performing slightly better than classical Bayesian segmentation, and three orders of magnitude faster. Moreover, even within the same type of MRI contrast, our strategy generalizes significantly better across datasets, compared to training using real images. Finally, we find that synthesizing a broad range of contrasts, even if unrealistic, increases the generalization of the neural network. Our code and model are open source at https://github.com/BBillot/SynthSeg.')
}}
[% / %]

[% .papers %]
{{ paper('Quantifying the Value of Lateral Views in Deep Learning for Chest X-rays',
        'Mohammad Hashir, Hadrien Bertrand, Joseph Paul Cohen',
        openreview='https://openreview.net/forum?id=rY3bgRRHnD',
        pdf='https://openreview.net/pdf?id=rY3bgRRHnD',
        id='P035',
        paper='papers/hashir20.html',
        teaser='https://youtu.be/___k6jBuPEo',
        abstract='Most deep learning models in chest X-ray prediction utilize the posteroanterior (PA) view due to the lack of other views available. PadChest is a large-scale chest X-ray dataset that has almost 200 labels and multiple views available. In this work, we use PadChest to explore multiple approaches to merging the PA and lateral views for predicting the radiological labels associated with the X-ray image. We find that different methods of merging the model utilize the lateral view differently. We also find that including the lateral view increases performance for 32 labels in the dataset, while being neutral for the others.      The increase in overall performance is comparable to the one obtained by using only the PA view with twice the amount of patients in the training set.')
}}
{{ paper('On the limits of cross-domain generalization in automated X-ray prediction',
        'Joseph Paul Cohen, Mohammad Hashir, Rupert Brooks, Hadrien Bertrand',
        openreview='https://openreview.net/forum?id=RZ-1WCgOQU',
        pdf='https://openreview.net/pdf?id=RZ-1WCgOQU',
        id='P036',
        paper='papers/cohen20.html',
        teaser='https://youtu.be/LZBFwkAB7f8',
        abstract='This large scale study focuses on quantifying what X-rays diagnostic prediction tasks generalize well across multiple different datasets. We present evidence that the issue of generalization is not due to a shift in the images but instead a shift in the labels. We study the cross-domain performance, agreement between models, and model representations. We find interesting discrepancies between performance and agreement where models which both achieve good performance disagree in their predictions as well as models which agree yet achieve poor performance. We also test for concept similarity by regularizing a network to group tasks across multiple datasets together and observe variation across the tasks.')
}}
{{ paper('Mutual information based deep clustering for semi-supervised segmentation',
        'Jizong Peng, Marco Pedersoli, Christian Desrosiers',
        openreview='https://openreview.net/forum?id=iunvffXgPm',
        pdf='https://openreview.net/pdf?id=iunvffXgPm',
        id='P099',
        paper='papers/peng20a.html',
        teaser='',
        abstract='The scarcity of labeled data often limits the application of deep learning to medical image segmentation. Semi-supervised learning helps overcome this limitation by leveraging unlabeled images to guide the learning process. In this paper, we propose using a clustering loss based on mutual information that explicitly enforces prediction consistency between nearby pixels in unlabeled images, and for random perturbation of these images, while imposing the network to predict the correct labels for annotated images. Since mutual information does not require a strict ordering of clusters in two different cluster assignments, we propose to incorporate another consistency regularization loss which forces the alignment of class probabilities at each pixel of perturbed unlabeled images. We evaluate the method on three challenging publicly-available medical datasets for image segmentation. Experimental results show our method to outperform recently-proposed approaches for semi-supervised and yield a performance comparable to fully-supervised training.')
}}
{{ paper('An Auto-Encoder Strategy for Adaptive Image Segmentation',
        'Evan M. Yu, Juan Eugenio Iglesias, Adrian V. Dalca, Mert R. Sabuncu',
        openreview='https://openreview.net/forum?id=J1-4vNudWo',
        pdf='https://openreview.net/pdf?id=J1-4vNudWo',
        id='P103',
        paper='papers/yu20.html',
        teaser='https://youtu.be/WYpKmCzMuH8',
        abstract='Deep neural networks are powerful tools for biomedical image segmentation. These models are often trained with heavy supervision, relying on pairs of images and corresponding voxel-level labels. However, obtaining segmentations of anatomical regions on a large number of cases can be prohibitively expensive. Thus there is a strong need for deep learning-based segmentation tools that do not require heavy supervision and can continuously adapt. In this paper, we propose a novel perspective of segmentation as a discrete representation learning problem, and present a variational autoencoder segmentation strategy that is flexible and adaptive. Our method, called Segmentation Auto-Encoder (SAE), leverages all available unlabeled scans and merely requires a segmentation prior, which can be a single unpaired segmentation image. In experiments, we apply SAE to brain MRI scans. Our results show that SAE can produce good quality segmentations, particularly when the prior is good. We demonstrate that a Markov Random Field prior can yield significantly better results than a spatially independent prior. Our code is freely available at https://github.com/evanmy/sae. ')
}}
{{ paper('Improving the Ability of Deep Networks to Use Information From Multiple Views in Breast Cancer Screening',
        'Nan Wu, Stanisław Jastrzębski, Jungkyu Park, Linda Moy, Kyunghyun Cho, Krzysztof J. Geras',
        openreview='https://openreview.net/forum?id=aD86B9pZ6u',
        pdf='https://openreview.net/pdf?id=aD86B9pZ6u',
        id='P158',
        paper='papers/wu20.html',
        teaser='https://youtu.be/Ewh3n233xok',
        abstract='In breast cancer screening, radiologists make the diagnosis based on images that are taken from two angles. Inspired by this, we seek to improve the performance of deep neural networks applied to this task by encouraging the model to use information from both views of the breast. First, we take a closer look at the training process and observe an imbalance between learning from the two views. In particular, we observe that parameters of the layers processing one of the views have larger gradient norms and contribute more to the overall loss reduction. Next, we test several methods targeted at utilizing both views more equally in training. We find that using the same weights to process both views, or using a technique called modality dropout, leads to a boost in performance. Looking forward, our results indicate improving learning dynamics as a promising avenue for improving utilization of multiple views in deep neural networks for medical diagnosis.')
}}
{{ paper('4D Semantic Cardiac Magnetic Resonance Image Synthesis on XCAT Anatomical Model',
        'Samaneh Abbasi-Sureshjani, Sina Amirrajab, Cristian Lorenz, Juergen Weese, Josien Pluim, Marcel Breeuwer',
        openreview='https://openreview.net/forum?id=tRdOL-DcPA',
        pdf='https://openreview.net/pdf?id=tRdOL-DcPA',
        id='P200',
        paper='papers/abbasi-sureshjani20.html',
        teaser='https://youtu.be/w5fCCvv-94w',
        abstract='We  propose  a  hybrid  controllable  image  generation  method  to  synthesize  anatomically meaningful 3D+t labeled Cardiac Magnetic Resonance (CMR) images.  Our hybrid method takes the mechanistic 4D eXtended CArdiac Torso (XCAT) heart model as the anatomical  ground  truth  and  synthesizes  CMR  images via a data-driven  Generative  Adversarial Network (GAN). We employ the state-of-the-art SPatially Adaptive De-normalization (SPADE) technique for conditional image synthesis to preserve the semantic spatial information  of  ground  truth  anatomy.  Using  the  parameterized  motion  model  of  the  XCAT heart,  we generate labels for 25 time frames of the heart for one cardiac cycle at 18 locations  for  the  short  axis  view.   Subsequently,  realistic  images  are  generated  from  these labels,  with  modality-specific  features  that  are  learned  from  real  CMR  image  data.   We  demonstrate that style transfer from another cardiac image can be accomplished by using a  style  encoder  network.   Due  to  the  flexibility  of  XCAT  in  creating  new  heart  models, this  approach  can  result  in  a  realistic  virtual  population  to  address  different  challenges the medical image analysis research community is facing such as expensive data collection. Our proposed method has a great potential to synthesize 4D controllable CMR images with annotations and adaptable styles to be used in various supervised multi-site, multi-vendor applications in medical image analysis.')
}}
[% / %]

[% .papers %]
{{ paper('Medical Image Segmentation via Unsupervised Convolutional Neural Network',
        'Junyu Chen, Eric C. Frey',
        openreview='https://openreview.net/forum?id=XrbnSCv4LU',
        pdf='https://openreview.net/pdf?id=XrbnSCv4LU',
        id='S038',
        paper='papers/chen20.html',
        teaser='',
        abstract='For the majority of the learning-based segmentation methods, a large quantity of high-quality training data is required. In this paper, we present a novel learning-based segmentation model that could be trained semi- or un- supervised. Specifically, in the unsupervised setting, we parameterize the Active contour without edges (ACWE) framework via a convolutional neural network (ConvNet), and optimize the parameters of the ConvNet using a self-supervised method. In another setting (semi-supervised), the auxiliary segmentation ground truth is used during training. We show that the method provides fast and high-quality bone segmentation in the context of single-photon emission computed tomography (SPECT) image.')
}}
{{ paper('Spatiotemporal motion prediction in free-breathing liver scans via a recurrent multi-scale encoder decoder',
        'Liset Vazquez Romaguera, Rosalie Plantefeve, Samuel Kadoury',
        openreview='https://openreview.net/forum?id=901HZmWDHH',
        pdf='https://openreview.net/pdf?id=901HZmWDHH',
        id='S057',
        paper='papers/romaguera20.html',
        teaser='https://youtu.be/zjI5M5zf8do',
        abstract='In this work we propose a multi-scale recurrent encoder-decoder architecture to predict the breathing induced organ deformation in future frames. The model was trained end-to-end from input images to predict a sequence of motion labels. Targets were created by quantizing the motion fields obtained from deformable image registration. We propose a multi-scale feature extraction scheme in the spatial encoder which processes the input at different resolutions. We report results using MRI free-breathing acquisitions from 12 volunteers. Experiments were aimed at investigating the proposed multi-scale design and the effect of increasing the number of predicted frames on the overall accuracy of the model. The proposed model was able to predict vessel positions in the next temporal image with a mean accuracy of 2.03 (2.89) mm showing increased performance in comparison with state-of-the-art approaches.')
}}
{{ paper('Low-dose CT Enhancement Network with a Perceptual Loss Function in the Spatial Frequency and Image Domains',
        'Kevin J. Chung, Roberto Souza, Richard Frayne, Ting-Yim Lee',
        openreview='https://openreview.net/forum?id=rw5BswbvMB',
        pdf='https://openreview.net/pdf?id=rw5BswbvMB',
        id='S059',
        paper='papers/chung20.html',
        teaser='',
        abstract='We propose a dual-domain cascade of U-nets (i.e. a W-net\\") operating in both the spatial frequency and image domains to enhance low-dose CT (LDCT) images without the need for proprietary x-ray projection data. The central slice theorem motivated the use of the spatial frequency domain in place of the raw sinogram. Data were obtained from the AAPM Low-dose Grand Challenge. A combination of Fourier space (F) and/or image domain (I) U-nets and W-nets were trained with a multi-scale structural similarity and mean absolute error loss function to denoise filtered back projected (FBP) LDCT images while maintaining perceptual features important for diagnostic accuracy. Deep learning enhancements were superior to FBP LDCT images in quantitative and qualitative performance with the dual-domain W-nets outperforming single-domain U-net cascades. Our results suggest that spatial frequency learning in conjunction with image-domain processing can produce superior LDCT enhancement than image-domain-only networks. ')
}}
{{ paper('Robust Image Segmentation Quality Assessment',
        'Leixin Zhou, Wenxiang Deng, Xiaodong Wu',
        openreview='https://openreview.net/forum?id=nyhZXiaotm',
        pdf='https://openreview.net/pdf?id=nyhZXiaotm',
        id='S093',
        paper='papers/zhou20.html',
        teaser='https://youtu.be/PgTTxpfsQvw',
        abstract='Deep learning based image segmentation methods have achieved great success, even having human-level accuracy in some applications. However, due to the black box nature of deep learning, the best method may fail in some situations. Thus predicting segmentation quality without ground truth would be very crucial especially in clinical practice. Recently, people proposed to train neural networks to estimate the quality score by regression. Although it can achieve promising prediction accuracy, the network suffers robustness problem, e.g. it is vulnerable to adversarial attacks. In this paper, we propose to alleviate this problem by utilizing the difference between the input image and the reconstructed image, which is conditioned on the segmentation to be assessed, to lower the chance to overfit to the undesired image features  from the original input image, and thus to increase the robustness. Results on ACDC17 dataset demonstrated our method is promising.')
}}
{{ paper('Assessing the validity of saliency maps for abnormality localization in medical imaging',
        'Nishanth Thumbavanam Arun, Nathan Gaw, Praveer Singh, Ken Chang, Katharina Viktoria Hoebel, Jay Patel, Mishka Gidwani, Jayashree Kalpathy-Cramer',
        openreview='https://openreview.net/forum?id=02X3kfP6W4',
        pdf='https://openreview.net/pdf?id=02X3kfP6W4',
        id='S107',
        paper='papers/arun20.html',
        teaser='',
        abstract='Saliency maps have become a widely used method to assess which areas of the input image are most pertinent to the prediction of a trained neural network.  However, in the context of medical imaging, there is no study to our knowledge that has examined the efficacy of these techniques and quantified them using overlap with ground truth bounding boxes. In this work, we explored the credibility of the various existing saliency map methods on the RSNA  Pneumonia  dataset. We  found  that  GradCAM  was  the  most  sensitive  to  model parameter and label randomization, and was highly agnostic to model architecture.')
}}
[% / %]


---

## Tuesday July 7 - 8:30-16:00


### TUE 8:30-9:30 UTC-4 - Oral Session #3 - Networks for Histology

Session Chairs: Kevin Zhou, Clarisa Sánchez

[% .papers %]
{{ paper('Tensor Networks for Medical Image Classification',
        'Raghavendra Selvan, Erik B Dam',
        openreview='https://openreview.net/forum?id=jjk6bxk07G',
        pdf='https://openreview.net/pdf?id=jjk6bxk07G',
        id='O095',
        paper='papers/selvan20.html',
        teaser='https://youtu.be/w0YgIa2SxWk',
        abstract='With the increasing adoption of machine learning tools like neural networks across several domains, interesting connections and comparisons to concepts from other domains are coming to light. In this work, we focus on the class of Tensor Networks, which has been a work horse for physicists in the last two decades to analyse quantum many-body systems. Building on the recent interest in tensor networks for machine learning, we extend the Matrix Product State tensor networks (which can be interpreted as linear classifiers operating in exponentially high dimensional spaces) to be useful in medical image analysis tasks. We focus on classification problems as a first step where we motivate the use of tensor networks and propose adaptions for 2D images using classical image domain concepts such as local orderlessness of images. With the proposed locally orderless tensor network model (LoTeNet), we show that tensor networks are capable of attaining performance that is comparable to state-of-the-art deep learning methods. We evaluate the model on two publicly available medical imaging datasets and show performance improvements with fewer model hyperparameters and lesser computational resources compared to relevant baseline methods.')
}}
{{ paper('Extending Unsupervised Neural Image Compression With Supervised Multitask Learning',
        'David Tellez, Diederik Hoppener, Cornelis Verhoef, Dirk Grunhagen, Pieter Nierop, Michal Drozdzal, Jeroen van der Laak, Francesco Ciompi',
        openreview='https://openreview.net/forum?id=oepOBj_A7E',
        pdf='https://openreview.net/pdf?id=oepOBj_A7E',
        id='O096',
        paper='papers/tellez20.html',
        teaser='https://youtu.be/GhW1qVGVit8',
        abstract='We focus on the problem of training convolutional neural networks on gigapixel histopathology images to predict image-level targets. For this purpose, we extend Neural Image Compression (NIC), an image compression framework that reduces the dimensionality of these images using an encoder network trained unsupervisedly. We propose to train this encoder using supervised multitask learning (MTL) instead. We applied the proposed MTL NIC to two histopathology datasets and three tasks. First, we obtained state-of-the-art results in the Tumor Proliferation Assessment Challenge of 2016 (TUPAC16). Second, we successfully classified histopathological growth patterns in images with colorectal liver metastasis (CLM). Third, we predicted patient risk of death by learning directly from overall survival in the same CLM data. Our experimental results suggest that the representations learned by the MTL objective are: (1) highly specific, due to the supervised training signal, and (2) transferable, since the same features perform well across different tasks. Additionally, we trained multiple encoders with different training objectives, e.g. unsupervised and variants of MTL, and observed a positive correlation between the number of tasks in MTL and the system performance on the TUPAC16 dataset.')
}}
{{ paper('Beyond Classfication: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning',
        'Chensu Xie, Hassan Muhammad, Chad M. Vanderbilt, Raul Caso, Dig Vijay Kumar Yarlagadda, Gabriele Campanella, Thomas J. Fuchs',
        openreview='https://openreview.net/forum?id=aqOfnZx4-N',
        pdf='https://openreview.net/pdf?id=aqOfnZx4-N',
        id='O305',
        paper='papers/xie20.html',
        teaser='',
        abstract='An emerging technology in cancer care and research is the use of histopathology whole slide images (WSI). Leveraging computation methods to aid in WSI assessment poses unique challenges. WSIs, being extremely high resolution giga-pixel images, cannot be directly processed by convolutional neural networks (CNN) due to huge computational cost. For this reason, state-of-the-art methods for WSI analysis adopt a two-stage approach where the training of a tile encoder is decoupled from the tile aggregation. This results in a trade-off between learning diverse and discriminative features. In contrast, we propose end-to-end part learning (EPL) which is able to learn diverse features while ensuring that learned features are discriminative. Each WSI is modeled as consisting of $k$ groups of tiles with similar features, defined as parts. A loss with respect to the slide label is backpropagated through an integrated CNN model to $k$ input tiles that are used to represent each part. Our experiments show that EPL is capable of clinical grade prediction of prostate and basal cell carcinoma. Further, we show that diverse discriminative features produced by EPL succeeds in multi-label classification of lung cancer architectural subtypes. Beyond classification, our method provides rich information of slides for high quality clinical decision support.')
}}
[% / %]

---

### TUE 9:30-11:00 UTC-4 - Poster Session #3

[% .papers %]
{{ paper('Tensor Networks for Medical Image Classification',
        'Raghavendra Selvan, Erik B Dam',
        openreview='https://openreview.net/forum?id=jjk6bxk07G',
        pdf='https://openreview.net/pdf?id=jjk6bxk07G',
        id='O095',
        paper='papers/selvan20.html',
        teaser='https://youtu.be/w0YgIa2SxWk',
        abstract='With the increasing adoption of machine learning tools like neural networks across several domains, interesting connections and comparisons to concepts from other domains are coming to light. In this work, we focus on the class of Tensor Networks, which has been a work horse for physicists in the last two decades to analyse quantum many-body systems. Building on the recent interest in tensor networks for machine learning, we extend the Matrix Product State tensor networks (which can be interpreted as linear classifiers operating in exponentially high dimensional spaces) to be useful in medical image analysis tasks. We focus on classification problems as a first step where we motivate the use of tensor networks and propose adaptions for 2D images using classical image domain concepts such as local orderlessness of images. With the proposed locally orderless tensor network model (LoTeNet), we show that tensor networks are capable of attaining performance that is comparable to state-of-the-art deep learning methods. We evaluate the model on two publicly available medical imaging datasets and show performance improvements with fewer model hyperparameters and lesser computational resources compared to relevant baseline methods.')
}}
{{ paper('Extending Unsupervised Neural Image Compression With Supervised Multitask Learning',
        'David Tellez, Diederik Hoppener, Cornelis Verhoef, Dirk Grunhagen, Pieter Nierop, Michal Drozdzal, Jeroen van der Laak, Francesco Ciompi',
        openreview='https://openreview.net/forum?id=oepOBj_A7E',
        pdf='https://openreview.net/pdf?id=oepOBj_A7E',
        id='O096',
        paper='papers/tellez20.html',
        teaser='https://youtu.be/GhW1qVGVit8',
        abstract='We focus on the problem of training convolutional neural networks on gigapixel histopathology images to predict image-level targets. For this purpose, we extend Neural Image Compression (NIC), an image compression framework that reduces the dimensionality of these images using an encoder network trained unsupervisedly. We propose to train this encoder using supervised multitask learning (MTL) instead. We applied the proposed MTL NIC to two histopathology datasets and three tasks. First, we obtained state-of-the-art results in the Tumor Proliferation Assessment Challenge of 2016 (TUPAC16). Second, we successfully classified histopathological growth patterns in images with colorectal liver metastasis (CLM). Third, we predicted patient risk of death by learning directly from overall survival in the same CLM data. Our experimental results suggest that the representations learned by the MTL objective are: (1) highly specific, due to the supervised training signal, and (2) transferable, since the same features perform well across different tasks. Additionally, we trained multiple encoders with different training objectives, e.g. unsupervised and variants of MTL, and observed a positive correlation between the number of tasks in MTL and the system performance on the TUPAC16 dataset.')
}}
{{ paper('Beyond Classfication: Whole Slide Tissue Histopathology Analysis By End-To-End Part Learning',
        'Chensu Xie, Hassan Muhammad, Chad M. Vanderbilt, Raul Caso, Dig Vijay Kumar Yarlagadda, Gabriele Campanella, Thomas J. Fuchs',
        openreview='https://openreview.net/forum?id=aqOfnZx4-N',
        pdf='https://openreview.net/pdf?id=aqOfnZx4-N',
        id='O305',
        paper='papers/xie20.html',
        teaser='',
        abstract='An emerging technology in cancer care and research is the use of histopathology whole slide images (WSI). Leveraging computation methods to aid in WSI assessment poses unique challenges. WSIs, being extremely high resolution giga-pixel images, cannot be directly processed by convolutional neural networks (CNN) due to huge computational cost. For this reason, state-of-the-art methods for WSI analysis adopt a two-stage approach where the training of a tile encoder is decoupled from the tile aggregation. This results in a trade-off between learning diverse and discriminative features. In contrast, we propose end-to-end part learning (EPL) which is able to learn diverse features while ensuring that learned features are discriminative. Each WSI is modeled as consisting of $k$ groups of tiles with similar features, defined as parts. A loss with respect to the slide label is backpropagated through an integrated CNN model to $k$ input tiles that are used to represent each part. Our experiments show that EPL is capable of clinical grade prediction of prostate and basal cell carcinoma. Further, we show that diverse discriminative features produced by EPL succeeds in multi-label classification of lung cancer architectural subtypes. Beyond classification, our method provides rich information of slides for high quality clinical decision support.')
}}
[% / %]

[% .papers %]
{{ paper('How Distance Transform Maps Boost Segmentation CNNs: An Empirical Study',
        'Jun Ma, Zhan Wei, Yiwen Zhang, Yixin Wang, Rongfei Lv, Cheng Zhu, Gaoxiang Chen, Jianan Liu, Chao Peng, Lei Wang, Yunpeng Wang, Jianan Chen',
        openreview='https://openreview.net/forum?id=hM4pNbXWst',
        pdf='https://openreview.net/pdf?id=hM4pNbXWst',
        id='P002',
        paper='papers/ma20a.html',
        teaser='https://youtu.be/G23FofuAOFM',
        abstract='Incorporating distance transform maps of ground truth into segmentation CNNs has been an interesting new trend in the last year. Despite many great works leading to improvements on a variety of segmentation tasks, the comparison among these methods has not been well studied.      In this paper, our \\emph{first contribution} is to summarize the latest developments of these methods in the 3D medical segmentation field.      The \\emph{second contribution} is that we systematically evaluated five benchmark methods on two representative public datasets.      These experiments highlight that all the five benchmark methods can bring performance gains to baseline V-Net. However, the implementation details have a noticeable impact on the performance, and not all the methods hold the benefits in different datasets.      Finally, we suggest the best practices and indicate unsolved problems for incorporating distance transform maps into CNNs, which we hope will be useful for the community. The codes and trained models are publicly available at \\url{https://github.com/JunMa11/SegWithDistMap}.')
}}
{{ paper('KD-MRI: A knowledge distillation framework for image reconstruction and image restoration in MRI workflow',
        'Balamurali Murugesan, Sricharan Vijayarangan, Kaushik Sarveswaran, Keerthi Ram, Mohanasankar Sivaprakasam',
        openreview='https://openreview.net/forum?id=OrBdiT86_O',
        pdf='https://openreview.net/pdf?id=OrBdiT86_O',
        id='P009',
        paper='papers/murugesan20.html',
        teaser='https://youtu.be/ue3XdYiCDz8',
        abstract='Deep learning networks are being developed in every stage of the MRI workflow and have provided state-of-the-art results. However, this has come at the cost of increased computation requirement and storage. Hence, replacing the networks with compact models at various stages in the MRI workflow can significantly reduce the required storage space and provide considerable speedup. In computer vision, knowledge distillation is a commonly used method for model compression. In our work, we propose a knowledge distillation (KD) framework for the image to image problems in the MRI workflow in order to develop compact, low-parameter models without a significant drop in performance. We propose a combination of the attention-based feature distillation method and imitation loss and demonstrate its effectiveness on the popular MRI reconstruction architecture, DC-CNN. We conduct extensive experiments using Cardiac, Brain, and Knee MRI datasets for 4x, 5x and 8x accelerations. We observed that the student network trained with the assistance of the teacher using our proposed KD framework provided significant improvement over the student network trained without assistance across all the datasets and acceleration factors. Specifically, for the Knee dataset, the student network achieves $65\\%$ parameter reduction, 2x faster CPU running time, and 1.5x faster GPU running time compared to the teacher. Furthermore, we compare our attention-based feature distillation method with other feature distillation methods. We also conduct an ablative study to understand the significance of attention-based distillation and imitation loss. We also extend our KD framework for MRI super-resolution and show encouraging results. ')
}}
{{ paper('An Auxiliary Task for Learning Nuclei Segmentation in 3D Microscopy Images',
        'Peter Hirsch, Dagmar Kainmueller',
        openreview='https://openreview.net/forum?id=iJVionbWNX',
        pdf='https://openreview.net/pdf?id=iJVionbWNX',
        id='P017',
        paper='papers/hirsch20.html',
        teaser='https://youtu.be/fLaZoYgUpOo',
        abstract='Segmentation of cell nuclei in microscopy images is a prevalent necessity in cell biology.      Especially for three-dimensional datasets, manual segmentation is prohibitively time-consuming, motivating the need for automated methods. Learning-based methods trained on pixel-wise ground-truth segmentations have been shown to yield state-of-the-art results on 2d benchmark image data of nuclei, yet a respective benchmark is missing for 3d image data. In this work, we perform a comparative evaluation of nuclei segmentation algorithms on a database of manually segmented 3d light microscopy volumes. We propose a novel learning strategy that boosts segmentation accuracy by means of a simple auxiliary task, thereby robustly outperforming each of our baselines. Furthermore, we show that one of our baselines, the popular three-label model, when trained with our proposed auxiliary task, outperforms the recent StarDist-3D.      As an additional, practical contribution, we benchmark nuclei segmentation against nuclei detection, i.e. the task of merely pinpointing individual nuclei without generating respective pixel-accurate segmentations. For learning nuclei detection, large 3d training datasets of manually annotated nuclei center points are available. However, the impact on detection accuracy caused by training on such sparse ground truth as opposed to dense pixel-wise ground truth has not yet been quantified. To this end, we compare nuclei detection accuracy yielded by training on dense vs. sparse ground truth. Our results suggest that training on sparse ground truth yields competitive nuclei detection rates. ')
}}
{{ paper('Continual Learning for Domain Adaptation in Chest X-ray Classification',
        'Matthias Lenga, Heinrich Schulz, Axel Saalbach',
        openreview='https://openreview.net/forum?id=lgE-MUlU1g',
        pdf='https://openreview.net/pdf?id=lgE-MUlU1g',
        id='P037',
        paper='papers/lenga20.html',
        teaser='https://youtu.be/bjuglG8y3q0',
        abstract='Over the last years, Deep Learning has been successfully applied to a broad range of medical applications. Especially in the context of chest X-ray classification, results have been reported which are on par, or even superior to experienced radiologists. Despite this success in controlled experimental environments, it has been noted that the ability of Deep Learning models to generalize to data from a new domain (with potentially different tasks) is often limited. In order to address this challenge, we investigate techniques from the field of Continual Learning (CL) including Joint Training (JT), Elastic Weight Consolidation (EWC) and Learning Without Forgetting (LWF). Using the ChestX-ray14 and the MIMIC-CXR datasets, we demonstrate empirically that these methods provide promising options to improve the performance of Deep Learning models on a target domain and to mitigate effectively catastrophic forgetting for the source domain. To this end, the best overall performance was obtained using JT, while for LWF competitive results could be achieved - even without accessing data from the source domain.')
}}
{{ paper('On Direct Distribution Matching for Adapting Segmentation Networks',
        'Georg Pichler, Jose Dolz, Ismail Ben Ayed, Pablo Piantanida',
        openreview='https://openreview.net/forum?id=-C9f-eGAuV',
        pdf='https://openreview.net/pdf?id=-C9f-eGAuV',
        id='P045',
        paper='papers/pichler20.html',
        teaser='https://youtu.be/6RQxDpWY6OE',
        abstract='Minimization of distribution matching losses is a principled approach to domain adaptation in the context of image classification. However, it is largely overlooked in adapting segmentation networks, which is currently dominated by adversarial models. We propose a class of loss functions, which encourage direct kernel density matching in the network-output space, up to some geometric transformations computed from unlabeled inputs. Rather than using an intermediate domain discriminator, our direct approach unifies distribution matching and segmentation in a single loss. Therefore, it simplifies segmentation adaptation by avoiding extra adversarial steps, while improving quality, stability and efficiency of training. We juxtapose our approach to state-of-the-art segmentation adaptation via adversarial training in the network-output space. In the challenging task of adapting brain segmentation across different magnetic resonance imaging (MRI) modalities, our approach achieves significantly better results both in terms of accuracy and stability.      ')
}}
{{ paper('SAU-Net: Efficient 3D Spine MRI Segmentation Using Inter-Slice Attention',
        'Yichi Zhang, Lin Yuan, Yujia Wang, Jicong Zhang',
        openreview='https://openreview.net/forum?id=wlszIiXbfS',
        pdf='https://openreview.net/pdf?id=wlszIiXbfS',
        id='P054',
        paper='papers/zhang20b.html',
        teaser='https://youtu.be/vqV45k9Wjxc',
        abstract='Accurate segmentation of spine Magnetic Resonance Imaging (MRI) is highly demanded in morphological research, quantitative analysis, and diseases identification, such as spinal canal stenosis, disc herniation and degeneration. However, accurate spine segmentation is challenging because of the irregular shape, artifacts and large variability between slices. To alleviate these problems, spatial information is used for more continuous and accurate segmentation such as by 3D convolutional neural networks (CNN) . However, 3D CNN suffers from higher computational cost, memory cost and risk of over-fitting, especially for medical images where the number of labeled data is limited. To address these problems, we apply the attention mechanism for the utilization of inter-slice information in 3D segmentation tasks based on 2D convolutional networks and propose a spatial attention-based densely connected U-Net (SAU-Net), which consists of Dense U-Net for extraction of intra-slice features and an inter-slice attention module (ISA) to utilize inter-slice information from adjacent slices and refine the segmentation results. Experimental results demonstrate the effectiveness of ISA as well as higher accuracy and efficiency of segmentation results of our method compared with other deep learning methods.')
}}
{{ paper('Red-GAN: Attacking class imbalance via conditioned generation. Yet another medical imaging perspective',
        'Ahmad B Qasim, Ivan Ezhov, Suprosanna Shit, Oliver Schoppe, Johannes Paetzold, Anjany Sekuboyina, Florian Kofler, Jana Lipkova, Hongwei Li, Bjoern Menze',
        openreview='https://openreview.net/forum?id=UHtZuvXHoA',
        pdf='https://openreview.net/pdf?id=UHtZuvXHoA',
        id='P071',
        paper='papers/qasim20.html',
        teaser='https://youtu.be/HCP2X8z44VI',
        abstract="Exploiting learning algorithms under scarce data regimes is a limitation and a reality of the medical imaging field. In an attempt to mitigate the problem, we propose a data augmentation protocol based on generative adversarial networks. The networks are conditioned at a pixel-level (segmentation mask) and at a global-level information (acquisition environment or lesion type). Such conditioning provides immediate access to the image-label pairs while controlling class specific appearance of the synthesized images. To stimulate synthesis of the features relevant for the segmentation task, an additional passive player in a form of segmentor is introduced into the the adversarial game.      We validate the approach on two medical datasets: BraTS, ISIC. By controlling the class distribution through injection of synthetic images into the training set we achieve control over the accuracy levels of the datasets\\' classes.  ")
}}
{{ paper('Siamese Tracking of Cell Behaviour Patterns',
        'Andreas Panteli, Deepak K. Gupta, Nathan de Bruin, Efstratios Gavves',
        openreview='https://openreview.net/forum?id=V3ZrDLgNgu',
        pdf='https://openreview.net/pdf?id=V3ZrDLgNgu',
        id='P109',
        paper='papers/panteli20.html',
        teaser='https://youtu.be/48HXH_WYi6k',
        abstract='Tracking and segmentation of biological cells in video sequences is a challenging problem, especially due to the similarity of the cells and high levels of inherent noise. Most machine learning-based approaches lack robustness and suffer from sensitivity to less prominent events such as mitosis, apoptosis and cell collisions. Due to the large variance in medical image characteristics, most approaches are dataset-specific and do not generalise well on other datasets.      In this paper, we propose a simple end-to-end cascade neural architecture able to model the movement behaviour of biological cells and predict collision and mitosis events. Our approach uses U-Net for an initial segmentation which is then improved through processing by a siamese tracker capable of matching each cell along the temporal axis. By facilitating the re-segmentation of collided and mitotic cells, our method demonstrates its capability to handle volatile trajectories and unpredictable cell locations while being invariant to cell morphology. We demonstrate that our tracking approach achieves state-of-the-art results on  PhC-C2DL-PSC and Fluo-N2DH-SIM+ datasets and ranks second on the DIC-C2DH-HeLa dataset of the cell tracking challenge benchmarks. ')
}}
{{ paper('Knee Injury Detection using MRI with Efficiently-Layered Network (ELNet)',
        'Chen-Han Tsai, Nahum Kiryati, Eli Konen, Iris Eshed, Arnaldo Mayer',
        openreview='https://openreview.net/forum?id=B_NG9y_wqU',
        pdf='https://openreview.net/pdf?id=B_NG9y_wqU',
        id='P117',
        paper='papers/tsai20.html',
        teaser='https://youtu.be/8nO-E_2aNcE',
        abstract="Magnetic Resonance Imaging (MRI) is a widely-accepted imaging technique for knee injury analysis. Its advantage of capturing knee structure in three dimensions makes it the ideal tool for radiologists to locate potential tears in the knee. In order to better confront the ever growing workload of musculoskeletal (MSK) radiologists, automated tools for patients\\' triage are becoming a real need, reducing delays in the reading of pathological cases. In this work, we present the Efficiently-Layered Network (ELNet), a convolutional neural network (CNN) architecture optimized for the task of initial knee MRI diagnosis for triage. Unlike past approaches, we train ELNet from scratch instead of using a transfer-learning approach. The proposed method is validated quantitatively and qualitatively, and compares favorably against state-of-the-art MRNet while using a single imaging stack (axial or coronal) as input. Additionally, we demonstrate our model\\'s capability to locate tears in the knee despite the absence of localization information during training. Lastly, the proposed model is extremely lightweight ($<$ 1MB) and therefore easy to train and deploy in real clinical settings.")
}}
{{ paper('Deep Reinforcement Learning for Organ Localization in CT',
        'Fernando Navarro, Anjany Sekuboyina, Diana Waldmannstetter, Jan C. Peeken, Stephanie E. Combs, Bjoern H. Menze',
        openreview='https://openreview.net/forum?id=0vDeD2UD0S',
        pdf='https://openreview.net/pdf?id=0vDeD2UD0S',
        id='P128',
        paper='papers/navarro20.html',
        teaser='https://youtu.be/Rk6gCh7eYkU',
        abstract='Robust localization of organs in computed tomography scans is a constant pre-processing requirement for organ-specific image retrieval, radiotherapy planning, and interventional image analysis. In contrast to current solutions based on exhaustive search or region proposals, which require large amounts of annotated data, we propose a deep reinforcement learning approach for organ localization in CT. In this work, an artificial agent is actively self-taught to localize organs in CT by learning from its asserts and mistakes. Within the context of reinforcement learning, we propose a novel set of actions tailored for organ localization in CT. Our method can use as a plug-and-play module for localizing any organ of interest. We evaluate the proposed solution on the public VISCERAL dataset containing CT scans with varying fields of view and multiple organs. We achieved an overall intersection over union of 0.63, an absolute median wall distance of 2.25 mm and a median distance between centroids of 3.65 mm.')
}}
{{ paper('A deep learning approach to segmentation of the developing cortex in fetal brain MRI with minimal manual labeling',
        'Ahmed E. Fetit, Amir Alansary, Lucilio Cordero-Grande, John Cupitt, Alice B. Davidson, A. David Edwards, Joseph V. Hajnal, Emer Hughes, Konstantinos Kamnitsas, Vanessa Kyriakopoulou, Antonios Makropoulos, Prachi A. Patkee, Anthony N. Price, Mary A. Rutherford, Daniel Rueckert',
        openreview='https://openreview.net/forum?id=VtVIlHSc0',
        pdf='https://openreview.net/pdf?id=VtVIlHSc0',
        id='P136',
        paper='papers/fetit20.html',
        teaser='https://youtu.be/CJIAB_ryWGs',
        abstract="We developed an automated system based on deep neural networks for fast and sensitive 3D image segmentation of cortical gray matter from fetal brain MRI. The lack of extensive/publicly available annotations presented a key challenge, as large amounts of labeled data are typically required for training sensitive models with deep learning. To address this, we: (i) generated preliminary tissue labels using the Draw-EM algorithm, which uses Expectation-Maximization and was originally designed for tissue segmentation in the neonatal domain; and (ii) employed a human-in-the-loop approach, whereby an expert fetal imaging annotator assessed and refined the performance of the model. By using a hybrid approach that combined automatically generated labels with manual refinements by an expert, we amplified the utility of ground truth annotations while immensely reducing their cost (283 slices). The deep learning system was developed, refined, and validated on 249 3D T2-weighted scans obtained from the Developing Human Connectome Project\\'s fetal cohort, acquired at 3T. Analysis of the system showed that it is invariant to gestational age at scan, as it generalized well to a wide age range (21 – 38 weeks) despite variations in cortical morphology and intensity  across the fetal distribution. It was also found to be invariant to intensities in regions surrounding the brain (amniotic fluid), which often present a major obstacle to the processing of neuroimaging data in the fetal domain.  ")
}}
[% / %]

[% .papers %]
{{ paper('Automatic segmentation of the pulmonary lobes with a 3D u-net and optimized loss function',
        'Bianca Lassen-Schmidt, Alessa Hering, Stefan Krass, Hans Meine',
        openreview='https://openreview.net/forum?id=AkziGgmwl',
        pdf='https://openreview.net/pdf?id=AkziGgmwl',
        id='S014',
        paper='papers/lassen-schmidt20.html',
        teaser='https://youtu.be/IfeHzhAK1yM',
        abstract='Fully-automatic lung lobe segmentation is challenging due to anatomical variations, pathologies, and incomplete fissures. We trained a 3D u-net for pulmonary lobe segmentation on 49 mainly publically available datasets and introduced a weighted Dice loss function to emphasize the lobar boundaries. To validate the performance of the proposed method we compared the results to two other methods. The new loss function improved the mean distance to 1.46 mm (compared to 2.08 mm for simple loss function without weighting).')
}}
{{ paper('Interpreting Chest X-rays via CNNs that Exploit Hierarchical Disease Dependencies and Uncertainty Labels',
        'Hieu H. Pham, Tung T. Le, Dat T. Ngo, Dat Q. Tran, Ha Q. Nguyen',
        openreview='https://openreview.net/forum?id=4o1GLIIHlh',
        pdf='https://openreview.net/pdf?id=4o1GLIIHlh',
        id='S023',
        paper='papers/pham20.html',
        teaser='https://youtu.be/oOBRZmyJW7o',
        abstract='We present a new approach based on deep convolutional neural networks (CNNs) for predicting the presence of 14 common thoracic diseases and observations. A strong set of CNNs are trained on over 200,000 chest X-ray images provided by CheXpert - a large scale chest X-ray dataset. In particular, dependencies among abnormality labels and uncertain samples are fully exploited during the training and inference stages. Experiments indicate that the proposed method achieves a mean area under the curve (AUC) of 0.940 in predicting 5 selected pathologies. To the best of our knowledge, this is the highest AUC score yet reported on this dataset to date. Additionally, the proposed method is also evaluated on the independent test set of the CheXpert competition and reports a performance level comparable to practicing radiologists. Our obtained result ranks first on the CheXpert leaderboard at the time of writing this paper.')
}}
{{ paper('Tractometry-based Anomaly Detection for Single-subject White Matter Analysis',
        'Maxime Chamberland, Sila Genc, Erika P. Raven, Greg D. Parker, Adam Cunningham, Joanne Doherty, Marianne van den Bree, Chantal M. W. Tax, Derek K. Jones',
        openreview='https://openreview.net/forum?id=heX-Rk0TE0',
        pdf='https://openreview.net/pdf?id=heX-Rk0TE0',
        id='S027',
        paper='papers/chamberland20.html',
        teaser='https://youtu.be/j9m9pqqQZHk',
        abstract='There is an urgent need for a paradigm shift from group-wise comparisons to individual diagnosis in diffusion MRI (dMRI) to enable the analysis of rare cases and clinically-heterogeneous groups. Deep autoencoders have shown great potential to detect anomalies in neuroimaging data. We present a framework that operates on the manifold of white matter (WM) pathways to learn normative microstructural features, and discriminate those at genetic risk from controls in a paediatric population. ')
}}
{{ paper('A Deep Learning based Fast Signed Distance Map Generation',
        'Zihao Wang, Clair Vandersteen, Thomas Demarcy, Dan Gnansia, Charles Raffaelli, Nicolas Guevara, Hervé Delingette',
        openreview='https://openreview.net/forum?id=b2N5ZuEouu',
        pdf='https://openreview.net/pdf?id=b2N5ZuEouu',
        id='S033',
        paper='papers/wang20a.html',
        teaser='https://youtu.be/BeWMzeZIjEI',
        abstract='Signed distance map (SDM) is a common representation of surfaces in medical image analysis and machine learning. The computational complexity of SDM for 3D parametric shapes is often a bottleneck in many applications, thus limiting their interest. In this paper, we propose a learning-based SDM generation neural network which is demonstrated on a tridimensional cochlea shape model parameterized by 4 shape parameters.      The proposed SDM Neural Network generates a cochlea signed distance map depending on four input parameters and we show that the deep learning approach leads to a 60 fold improvement in the time of computation compared to more classical SDM generation methods. Therefore, the proposed approach achieves a good trade-off between accuracy and efficiency. ')
}}
{{ paper('Deblurring for spiral real-time MRI using convolutional neural networks',
        'Yongwan Lim, Shrikanth Narayanan, Krishna Nayak',
        openreview='https://openreview.net/forum?id=zYareJYs8Z',
        pdf='https://openreview.net/pdf?id=zYareJYs8Z',
        id='S047',
        paper='papers/lim20.html',
        teaser='',
        abstract='Spiral acquisitions are preferred in real-time MRI because of their time efficiency. A fundamental limitation of spirals is image blurring due to off-resonance, which degrades image quality significantly at air-tissue boundaries. Here, we demonstrate a simple CNN-based deblurring method for spiral real-time MRI of human speech production. We show the CNN-based deblurring is capable of restoring blurred vocal tract tissue boundaries, without a need for exam-specific field maps. Deblurring performance is superior to a current auto-calibrated method, and slightly inferior to ideal reconstruction with perfect knowledge of the field maps. ')
}}
{{ paper('Deep learning approach to describing and classifying fungi microscopic images',
        'Bartosz Zieliński, Agnieszka Sroka-Oleksiak, Dawid Rymarczyk, Adam Piekarczyk, Monika Brzychczy-Włoch',
        openreview='https://openreview.net/forum?id=AEhp_Cqq-h',
        pdf='https://openreview.net/pdf?id=AEhp_Cqq-h',
        id='S053',
        paper='papers/zieliński20.html',
        teaser='https://youtu.be/xCFpZI50cTg',
        abstract='Preliminary diagnosis of fungal infections can rely on microscopic examination. However, in many cases, it does not allow unambiguous identification of the species due to their visual similarity. Therefore, it is usually necessary to use additional biochemical tests. That involves additional costs and extends the identification process up to 10 days. Such a delay in the implementation of targeted therapy may be grave in consequence as the mortality rate for immunosuppressed patients is high. In this paper, we apply a machine learning approach based on deep neural networks and bag-of-words to classify microscopic images of various fungi species. Our approach makes the last stage of biochemical identification redundant, shortening the identification process by 2-3 days, and reducing the cost of the diagnosis.')
}}
{{ paper('4D Deep Learning for Multiple-Sclerosis Lesion Activity Segmentation',
        'Nils Gessert, Marcel Bengs, Julia Krüger, Roland Opfer, Ann-Christin Ostwaldt, Praveena Manogaran, Sven Schippling, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=238UzYB1d9',
        pdf='https://openreview.net/pdf?id=238UzYB1d9',
        id='S092',
        paper='papers/gessert20.html',
        teaser='https://youtu.be/mISTl-A5EK8',
        abstract='Multiple sclerosis lesion activity segmentation is the task of detecting new and enlarging lesions that appeared between a baseline and a follow-up brain MRI scan. While deep learning methods for single-scan lesion segmentation are common, deep learning approaches for lesion activity have only been proposed recently. Here, a two-path architecture processes two 3D MRI volumes from two time points. In this work, we investigate whether extending this problem to full 4D deep learning using a history of MRI volumes and thus an extended baseline can improve performance. For this purpose, we design a recurrent multi-encoder-decoder architecture for processing 4D data. We find that adding more temporal information is beneficial and our proposed architecture outperforms previous approaches with a lesion-wise true positive rate of 0.84 at a lesion-wise false positive rate of 0.19.')
}}
{{ paper('Bayesian Generative Models for Knowledge Transfer in MRI Semantic Segmentation Problems',
        'Anna Kuzina, Evgenii Egorov, Evgeny Burnaev',
        openreview='https://openreview.net/forum?id=3i6X1618wi',
        pdf='https://openreview.net/pdf?id=3i6X1618wi',
        id='S256',
        paper='papers/kuzina20.html',
        teaser='https://youtu.be/aA8dE8mvoic',
        abstract='Automatic segmentation methods based on deep learning have recently demonstrated state-of-the-art performance, outperforming the ordinary methods. Nevertheless, these methods are inapplicable for small datasets, which are very common in medical problems. To this end, we propose a knowledge transfer method between diseases via the Generative Bayesian Prior network. Our approach is compared to a pre-train approach and random initialization and obtains the best results in terms of Dice Similarity Coefficient metric for the small subsets of the Brain Tumor Segmentation 2018 database (BRATS2018).')
}}
[% / %]

---

### TUE 11:00-12:00 UTC-4 - Keynote #2 - Nikos Paragios


### TUE 12:00-12:30 UTC-4 - Break


### TUE 12:30-13:30 UTC-4 - Keynote #3 - Daphne Koller

---

### TUE 13:30-14:30 UTC-4 - Oral #4 - Imaging

Session Chairs: Dana Cobzas, Samuel Kadoury

[% .papers %]
{{ paper('Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping',
        'Jinwei Zhang, Hang Zhang, Mert Sabuncu, Pascal Spincemaille, Thanh Nguyen, Yi Wang',
        openreview='https://openreview.net/forum?id=DuWrLOZ27k',
        pdf='https://openreview.net/pdf?id=DuWrLOZ27k',
        id='O006',
        paper='papers/zhang20a.html',
        teaser='',
        abstract="A learning-based posterior distribution estimation method, Probabilistic Dipole Inversion (PDI), is proposed to solve quantitative susceptibility mapping (QSM) inverse problem in MRI with uncertainty estimation. A deep convolutional neural network (CNN) is used to represent the multivariate Gaussian distribution as the approximated posterior distribution of susceptibility given the input measured field. In PDI, such CNN is firstly trained on healthy subjects\\' data with labels by maximizing the posterior Gaussian distribution loss function as used in Bayesian deep learning. When testing on each patient\\' data without any label, PDI updates the pre-trained CNN\\'s weights in an unsupervised fashion by minimizing the Kullback–Leibler divergence between the approximated posterior distribution represented by CNN and the true posterior distribution given the likelihood distribution from known physical model and pre-defined prior distribution. Based on our experiments, PDI provides additional uncertainty estimation compared to the conventional MAP approach, meanwhile addressing the potential discrepancy issue of CNN when test data deviates from training dataset.")
}}
{{ paper('Addressing The False Negative Problem of MRI Reconstruction Networks by Adversarial Attacks and Robust Training',
        'Kaiyang Cheng, Francesco Calivá, Rutwik Shah, Misung Han, Sharmila Majumdar, Valentina Pedoia',
        openreview='https://openreview.net/forum?id=7NF2rZwE-z',
        pdf='https://openreview.net/pdf?id=7NF2rZwE-z',
        id='O028',
        paper='papers/cheng20.html',
        teaser='',
        abstract="Deep learning models have been shown to have success in reconstructing accelerated MRI, over traditional methods. However, it has been observed that these methods tend to miss the small features that are rare, such as meniscal tears, subchondral osteophyte, etc. This is a concerning finding as these small and rare features are the most relevant in clinical diagnostic settings. In this work, we propose a framework to find the worst-case false negatives by adversarially attacking the trained models and improve the models\\' ability to reconstruct the small features by robust training.")
}}
{{ paper('Correlation via Synthesis: End-to-end Image Generation and Radiogenomic Learning Based on Generative Adversarial Network',
        'Ziyue Xu, Xiaosong Wang, Hoo-Chang Shin, Dong Yang, Holger Roth, Fausto Milletari, Ling Zhang, Daguang Xu',
        openreview='https://openreview.net/forum?id=2wAX1X5X6n',
        pdf='https://openreview.net/pdf?id=2wAX1X5X6n',
        id='O058',
        paper='papers/xu20.html',
        teaser='',
        abstract='Radiogenomic map linking image features and gene expression profiles has great potential for  non-invasively identifying molecular properties of a particular type of disease.  Conventionally, such map is produced in three independent steps: 1) gene-clustering to metagenes, 2) image feature extraction, and 3) statistical correlation between metagenes and image features. Each step is separately performed and relies on arbitrary measurements without considering the correlation among each other. In this work, we investigate the potential of an end-to-end method fusing gene code with image features to generate synthetic pathology image and learn radiogenomic map simultaneously. To achieve this goal, we develop a multi-conditional generative adversarial network (GAN) conditioned on both background images and gene expression code, synthesizing the corresponding image. Image and gene features are fused at different scales to ensure both the separation of pathology part and background, as well as the realism and quality of the synthesized image. We tested our method on non-small cell lung cancer (NSCLC) dataset. Results demonstrate that the proposed method produces realistic synthetic images, and provides a promising way to find gene-image relationship in a holistic end-to-end manner.')
}}
[% / %]

---

### TUE 14:30-16:00 UTC-4 - Poster Session #4

[% .papers %]
{{ paper('Bayesian Learning of Probabilistic Dipole Inversion for Quantitative Susceptibility Mapping',
        'Jinwei Zhang, Hang Zhang, Mert Sabuncu, Pascal Spincemaille, Thanh Nguyen, Yi Wang',
        openreview='https://openreview.net/forum?id=DuWrLOZ27k',
        pdf='https://openreview.net/pdf?id=DuWrLOZ27k',
        id='O006',
        paper='papers/zhang20a.html',
        teaser='',
        abstract="A learning-based posterior distribution estimation method, Probabilistic Dipole Inversion (PDI), is proposed to solve quantitative susceptibility mapping (QSM) inverse problem in MRI with uncertainty estimation. A deep convolutional neural network (CNN) is used to represent the multivariate Gaussian distribution as the approximated posterior distribution of susceptibility given the input measured field. In PDI, such CNN is firstly trained on healthy subjects\\' data with labels by maximizing the posterior Gaussian distribution loss function as used in Bayesian deep learning. When testing on each patient\\' data without any label, PDI updates the pre-trained CNN\\'s weights in an unsupervised fashion by minimizing the Kullback–Leibler divergence between the approximated posterior distribution represented by CNN and the true posterior distribution given the likelihood distribution from known physical model and pre-defined prior distribution. Based on our experiments, PDI provides additional uncertainty estimation compared to the conventional MAP approach, meanwhile addressing the potential discrepancy issue of CNN when test data deviates from training dataset.")
}}
{{ paper('Addressing The False Negative Problem of MRI Reconstruction Networks by Adversarial Attacks and Robust Training',
        'Kaiyang Cheng, Francesco Calivá, Rutwik Shah, Misung Han, Sharmila Majumdar, Valentina Pedoia',
        openreview='https://openreview.net/forum?id=7NF2rZwE-z',
        pdf='https://openreview.net/pdf?id=7NF2rZwE-z',
        id='O028',
        paper='papers/cheng20.html',
        teaser='',
        abstract="Deep learning models have been shown to have success in reconstructing accelerated MRI, over traditional methods. However, it has been observed that these methods tend to miss the small features that are rare, such as meniscal tears, subchondral osteophyte, etc. This is a concerning finding as these small and rare features are the most relevant in clinical diagnostic settings. In this work, we propose a framework to find the worst-case false negatives by adversarially attacking the trained models and improve the models\\' ability to reconstruct the small features by robust training.")
}}
{{ paper('Correlation via Synthesis: End-to-end Image Generation and Radiogenomic Learning Based on Generative Adversarial Network',
        'Ziyue Xu, Xiaosong Wang, Hoo-Chang Shin, Dong Yang, Holger Roth, Fausto Milletari, Ling Zhang, Daguang Xu',
        openreview='https://openreview.net/forum?id=2wAX1X5X6n',
        pdf='https://openreview.net/pdf?id=2wAX1X5X6n',
        id='O058',
        paper='papers/xu20.html',
        teaser='',
        abstract='Radiogenomic map linking image features and gene expression profiles has great potential for  non-invasively identifying molecular properties of a particular type of disease.  Conventionally, such map is produced in three independent steps: 1) gene-clustering to metagenes, 2) image feature extraction, and 3) statistical correlation between metagenes and image features. Each step is separately performed and relies on arbitrary measurements without considering the correlation among each other. In this work, we investigate the potential of an end-to-end method fusing gene code with image features to generate synthetic pathology image and learn radiogenomic map simultaneously. To achieve this goal, we develop a multi-conditional generative adversarial network (GAN) conditioned on both background images and gene expression code, synthesizing the corresponding image. Image and gene features are fused at different scales to ensure both the separation of pathology part and background, as well as the realism and quality of the synthesized image. We tested our method on non-small cell lung cancer (NSCLC) dataset. Results demonstrate that the proposed method produces realistic synthetic images, and provides a promising way to find gene-image relationship in a holistic end-to-end manner.')
}}
[% / %]

[% .papers %]
{{ paper('End-to-end learning of convolutional neural net and dynamic programming for left ventricle segmentation',
        'Nhat M. Nguyen, Nilanjan Ray',
        openreview='https://openreview.net/forum?id=_4_RPMYWN',
        pdf='https://openreview.net/pdf?id=_4_RPMYWN',
        id='P011',
        paper='papers/nguyen20.html',
        teaser='https://youtu.be/X0hBhXi-laY',
        abstract='Differentiable programming is able to combine different functions or modules in a data processing pipeline with the goal of applying gradient descent-based end-to-end learning or optimization. A significant impediment to differentiable programming is the non-differentiable nature of some functions.  We propose to overcome this difficulty by using neural networks to approximate such modules.  An approximating neural network provides synthetic gradients (SG) for backpropagation across a non-differentiable module.  Our design is grounded on a well-known theory that gradient of an approximating neural network can approximate a sub-gradient of a weakly differentiable function.  We apply SG to combine convolutional neural  network  (CNN)  with  dynamic  programming  (DP)  in  end-to-end  learning  for  segmenting left ventricle from short axis view of heart MRI. Our experiments show that end-to-end combination of CNN and DP requires fewer labeled images to achieve a significantly better segmentation accuracy than using only CNN.')
}}
{{ paper('Cascaded Deep Neural Networks for Retinal Layer Segmentation of Optical Coherence Tomography with Fluid Presence',
        'Da Ma, Donghuan Lu, Morgan Heisler, Setareh Dabiri, Sieun Lee, Gavin Weiguan Ding, Marinko V. Sarunic, Mirza Faisal Beg',
        openreview='https://openreview.net/forum?id=dxVMXBzKKQ',
        pdf='https://openreview.net/pdf?id=dxVMXBzKKQ',
        id='P013',
        paper='papers/ma20b.html',
        teaser='https://youtu.be/fRb6s84YSew',
        abstract='Optical coherence tomography (OCT) is a non-invasive imaging technology that can provide micrometer-resolution cross-sectional images of the inner structures of the eye. It is widely used for the diagnosis of ophthalmic diseases with retinal alteration, such as layer deformation and fluid accumulation. In this paper, a novel framework was proposed to segment retinal layers with fluid presence. The main contribution of this study is two folds: 1) we developed a cascaded network framework to incorporate the prior structural knowledge; 2) we proposed a novel deep neural network based on U-Net and fully convolutional network, termed LF-UNet. Cross validation experiments proved that the proposed LF-UNet has superior performance comparing with the state-of-the-art methods, and incorporating the relative distance map structural prior information could further improve the performance regardless of the network.')
}}
{{ paper('DRMIME: Differentiable Mutual Information and Matrix Exponential for Multi-Resolution Image Registration',
        'Abhishek Nan, Matthew Tennant, Uriel Rubin, Nilanjan Ray',
        openreview='https://openreview.net/forum?id=Q0Bm5e6dkW',
        pdf='https://openreview.net/pdf?id=Q0Bm5e6dkW',
        id='P064',
        paper='papers/nan20.html',
        teaser='https://youtu.be/RkWDByLlF5M',
        abstract='In this work, we present a novel unsupervised image registration algorithm. It is differentiable end-to-end and can be used for both multi-modal and mono-modal registration. This is done using mutual information (MI) as a metric. The novelty here is that rather than using traditional ways of approximating MI which are often histogram based, we use a neural estimator called MINE and supplement it with matrix exponential for transformation matrix computation. The introduction of MINE tackles some of the drawbacks of histogram based MI computation and matrix exponential makes the optimization process smoother. We also introduce the idea of a multi-resolution loss, which makes the optimization process faster and more robust. This leads to improved results as compared to the standard algorithms available out-of-the-box in state-of-the-art image registration toolboxes, both in terms of time as well as registration accuracy, which we empirically demonstrate on publicly available datasets.')
}}
{{ paper('Breaking Speed Limits with Simultaneous Ultra-Fast MRI Reconstruction and Tissue Segmentation',
        'Francesco Calivá, Rutwik Shah, Upasana Upadhyay Bharadwaj, Sharmila Majumdar, Peder Larson, Valentina Pedoia',
        openreview='https://openreview.net/forum?id=sXONwA0ex',
        pdf='https://openreview.net/pdf?id=sXONwA0ex',
        id='P239',
        paper='papers/calivá20.html',
        teaser='https://youtu.be/vnACGxIEQwE',
        abstract="Magnetic Resonance Image (MRI) acquisition, reconstruction and tissue segmentation are usually considered separate problems. This can be limiting when it comes to rapidly extracting relevant clinical parameters. In many applications, availability of reconstructed images with high fidelity may not be a priority as long as biomarker extraction is reliable and feasible. Built upon this concept, we demonstrate that it is possible to perform tissue segmentation directly from highly undersampled k-space and obtain quality results comparable to those in fully-sampled scenarios. We propose \\'TB-recon\\', a 3D task-based reconstruction framework. TB-recon simultaneously reconstructs MRIs from raw data and segments tissues of interest. To do so, we devised a network architecture with a shared encoding path and two task-related decoders where features flow among tasks. We deployed TB-recon on a set of (up to $24\\times$) retrospectively undersampled MRIs from the Osteoarthritis Initiative dataset, where we automatically segmented knee cartilage and menisci. An experimental study was conducted showing the superior performance of the proposed method over a combination of a standard MRI reconstruction and segmentation method, as well as alternative deep learning based solutions. In addition, our ablation study highlighted the importance of skip connections among the decoders for the segmentation task. Ultimately, we conducted a reader study, where two musculoskeletal radiologists assessed the proposed model’s reconstruction performance.")
}}
{{ paper('Siamese Content Loss Networks for Highly Imbalanced Medical Image Segmentation',
        'Brandon Mac, Alan R. Moody, April Khademi',
        openreview='https://openreview.net/forum?id=VINrwcDkvA',
        pdf='https://openreview.net/pdf?id=VINrwcDkvA',
        id='P271',
        paper='papers/mac20.html',
        teaser='https://youtu.be/YA4yzdUhu1Y',
        abstract='Automatic segmentation of white matter hyperintensities (WMHs) in magnetic resonance imaging (MRI) remains highly sought after due to the potential to streamline and alleviate clinical workflows. WMHs are small relative to whole acquired volume, which leads to class imbalance issues, and instability during the training process of many deep learning based solutions. To address this, we propose a method which is robust to effects of class imbalance, through incorporating multi-scale information in the training process. Our method consists of training an encoder-decoder neural network utilizing a Siamese network as an auxiliary loss function. These Siamese networks take in pairs of image pairs, input images masked with ground truth labels, and input images masked with predictions, and computes multi-resolution feature vector representations and provides gradient feedback in the form of a L2 norm. We leverage transfer learning in our Siamese network, and present positive results without need to further train. It was found these methods are more robust for training segmentation neural networks and provide greater generalizability. Our method was cross-validated on multi-center data, yielding significant overall agreement with manual annotations. ')
}}
{{ paper('Multitask radiological modality invariant landmark localization using deep reinforcement learning',
        'Vishwa S. Parekh, Alex E. Bocchieri, Michael A. Jacobs',
        openreview='https://openreview.net/forum?id=XvBdNAyPCk',
        pdf='https://openreview.net/pdf?id=XvBdNAyPCk',
        id='P273',
        paper='papers/parekh20.html',
        teaser='https://youtu.be/-EQI-AWNO0c',
        abstract='Deep learning techniques are increasingly being developed for several applications in radiology, for example landmark and organ localization with segmentation. However, these applications to date have been limited in nature, in that, they are restricted to just a single task e.g. localization of tumors or to a specific organ using supervised training by an expert. As a result, to develop a radiological decision support system, it would need to be equipped with potentially hundreds of deep learning models with each model trained for a specific task or organ. This would be both space and computationally expensive. In addition, the true potential of deep learning methods in radiology can only be achieved when the model is adaptable and generalizable to multiple different tasks. To that end, we have developed and implemented a multitask modality invariant deep reinforcement learning framework (MIDRL) for landmark localization and segmentation in radiological applications.  MIDRL was evaluated using a diverse data set containing multiparametric MRIs (mpMRI) acquired from different organs and with different imaging parameters. The MIDRL framework was trained to localize six different anatomical structures throughout the body, including, knee, trochanter, heart, kidney, breast nipple, and prostate across T1 weighted, T2 weighted, Dynamic Contrast Enhanced (DCE), Diffusion Weighted Imaging (DWI), and DIXON MRI sequences obtained from twenty-four breast, eight prostate, and twenty five whole body mpMRIs. The trained MIDRL framework produced excellent accuracy in localizing each of the six anatomical landmarks with an average dice similarity$>$0.77, except for breast nipple localization in DCE. In conclusion, we developed  a multitask deep reinforcement learning framework and demonstrated MIDRL’s potential towards the development of a general AI for a radiological decision support system.')
}}
[% / %]

[% .papers %]
{{ paper('Classification of Epithelial Ovarian Carcinoma Whole-Slide Pathology Images Using Deep Transfer Learning',
        'Yiping Wang, David Farnell, Hossein Farahani, Mitchell Nursey, Basile Tessier-Cloutier, Steven J.M. Jones, David G. Huntsman, C. Blake Gilks, Ali Bashashati',
        openreview='https://openreview.net/forum?id=VXdQD8B307',
        pdf='https://openreview.net/pdf?id=VXdQD8B307',
        id='S104',
        paper='papers/wang20b.html',
        teaser='https://youtu.be/I2JsLBARtmo',
        abstract="Ovarian cancer is the most lethal cancer of the female reproductive organs. There are $5$ major histological subtypes of epithelial ovarian cancer, each with distinct morphological, genetic, and clinical features. Currently, these histotypes are determined by a pathologist\\'s microscopic examination of tumor whole-slide images (WSI). This process has been hampered by poor inter-observer agreement (Cohen’s kappa $0.54$-$0.67$). We utilized a two-stage deep transfer learning algorithm based on convolutional neural networks (CNN) and progressive resizing for automatic classification of epithelial ovarian carcinoma WSIs. The proposed algorithm achieved a mean accuracy of $87.54\\%$ and Cohen\\'s kappa of $0.8106$ in the slide-level classification of $305$ WSIs; performing better than a standard CNN and pathologists without gynecology-specific training. ")
}}
{{ paper('A Fully Convolutional Normalization Approach of Head and Neck Cancer Outcome Prediction',
        'William Le, Francisco Perdigón Romero, Samuel Kadoury',
        openreview='https://openreview.net/forum?id=JojEzQ3E5n',
        pdf='https://openreview.net/pdf?id=JojEzQ3E5n',
        id='S145',
        paper='papers/le20.html',
        teaser='https://youtu.be/OD-lmWkCr4A',
        abstract='Medical image classification performance worsens in multi-domain datasets, caused by radiological image differences across institutions, scanner manufacturer, model and operator. Deep learning is well-suited for learning image features with priors encoded as constraints during the training process.  In this work, we apply a ResNeXt classification network augmented with an FCN preprocessor subnetwork to a public TCIA head and neck cancer dataset. The training goal is survival prediction of radiotherapy cases based on pre-treatment FDG-PET/CT scans, acquired across 4 different hospitals.  We show that the preprocessor sub-network acts as a embedding normalizer and improves over state-of-the-art results of 70% AUC to 76%.')
}}
{{ paper('Automatic segmentation of stroke lesions in non-contrast computed tomography with convolutional neural networks',
        'Anup Tuladhar, Serena Schimert, Deepthi Rajashekar, Helge C. Kniep, Jens Fiehler, Nils D. Forkert',
        openreview='https://openreview.net/forum?id=ehpiBRHu07',
        pdf='https://openreview.net/pdf?id=ehpiBRHu07',
        id='S161',
        paper='papers/tuladhar20.html',
        teaser='',
        abstract='Manual lesion segmentation for non-contrast computed tomography (NCCT), a common modality for volumetric follow-up assessment of ischemic strokes, is time-consuming and subject to high inter-observer variability. Our approach uses a combination of a 3D convolutional neural network (CNN) combined with post-processing methods. A total of 272 multi-center clinical NCCT datasets were used: 204 for CNN training, 48 for validation and developing post-processing methods, and 20 for testing. The testing datasets were from centers that did not contribute to the training and validation sets, and were segmented by two neuroradiologists. We achieved a median Dice score of 0.63, which was significantly improved to 0.66 with post-processing. The automatically segmented lesion volumes were not significantly different from the lesion volumes determined by the two manual observers. As the model was trained on datasets from multiple centers, it is broadly applicable. ')
}}
{{ paper('Anatomical Predictions using Subject-Specific Medical Data',
        'Marianne Rakic, John Guttag, Adrian V. Dalca',
        openreview='https://openreview.net/forum?id=apwZYLKTCo',
        pdf='https://openreview.net/pdf?id=apwZYLKTCo',
        id='S236',
        paper='papers/rakic20.html',
        teaser='https://youtu.be/TPe9p-_sXIE',
        abstract='Changes in brain anatomy can provide important insight for treatment design or scientific analyses. We present a method that predicts how brain anatomy for an individual will change over time. We model these changes through a diffeomorphic deformation field, and design a predictive function using convolutional neural networks. Given a predicted deformation field, a baseline scan can be warped to give a prediction of the brain scan at a future time. We demonstrate the method using the ADNI cohort, and analyze how performance is affected by model variants and the type of subject-specific information provided. We show that the model provides good predictions and that external clinical data can improve predictions.      ')
}}
{{ paper('Enhancing Foreground Boundaries for Medical Image Segmentation',
        'Dong Yang, Holger Roth, Xiaosong Wang, Ziyue Xu, Andriy Myronenko, Daguang Xu',
        openreview='https://openreview.net/forum?id=PAlQnIVKLY',
        pdf='https://openreview.net/pdf?id=PAlQnIVKLY',
        id='S278',
        paper='papers/yang20.html',
        teaser='',
        abstract='Object segmentation plays an important role in the modern medical image analysis, which benefits clinical study, disease diagnosis, and surgery planning. Given the various modalities of medical images, the automated or semi-automated segmentation approaches have been used to identify and parse organs, bones, tumors, and other regions-of-interest (ROI). However, these contemporary segmentation approaches tend to fail to predict the boundary areas of ROI, because of the fuzzy appearance contrast caused during the imaging procedure. To further improve the segmentation quality of boundary areas, we propose a boundary enhancement loss to enforce additional constraints on optimizing machine learning models. The proposed loss function is light-weighted and easy to implement without any pre- or post-processing. Our experimental results validate that our loss function are better than, or at least comparable to, other state-of-the-art loss functions in terms of segmentation accuracy.')
}}
{{ paper('Overview of Scanner Invariant Representations',
        'Daniel Moyer, Greg ver Steeg, Paul M. Thompson',
        openreview='https://openreview.net/forum?id=yqm9RD_XHT',
        pdf='https://openreview.net/pdf?id=yqm9RD_XHT',
        id='S288',
        paper='papers/moyer20.html',
        teaser='https://youtu.be/MXFx0TUC1Qk',
        abstract='Pooled imaging data from multiple sources is subject to bias from each source. Studies that do not correct for these scanner/site biases at best lose statistical power, and at worst leave spurious correlations in their data. Estimation of the bias effects is non-trivial due to the paucity of data with correspondence across sites, so called \\"traveling phantom\\" data, which is expensive to collect. Nevertheless, numerous solutions leveraging direct correspondence have been proposed. In contrast to this, Moyer et al. (2019) proposes an unsupervised solution using invariant representations, one which does not require correspondence and thus does not require paired images. By leveraging the data processing inequality, an invariant representation can then be used to create an image reconstruction that is uninformative of its original source, yet still faithful to the underlying structure. In the present abstract we provide an overview of this method.')
}}
[% / %]


---

## Wednesday July 8 - 8:30-15:00

### WED 8:30-9:30 UTC-4 - Oral Session #5 - Image Generation

Session Chairs: Mattias Heinrich, Carole Sudre

[% .papers %]
{{ paper('Towards multi-sequence MR image recovery from undersampled k-space data',
        'Cheng Peng, Wei-An Lin, Rama Chellappa, S. Kevin Zhou',
        openreview='https://openreview.net/forum?id=Pk7In-gVEd',
        pdf='https://openreview.net/pdf?id=Pk7In-gVEd',
        id='O018',
        paper='papers/peng20b.html',
        teaser='',
        abstract='Undersampled MR image recovery has been widely studied for accelerated MR acquisition. However, it has been mostly studied under a single sequence scenario, despite the fact that multi-sequence MR scan is common in practice. In this paper, we aim to optimize multi-sequence MR image recovery from undersampled k-space data under an overall time constraint while considering the difference in acquisition time for various sequences. We first formulate it as a constrained optimization problem and then show that finding the optimal sampling strategy for all sequences and the best recovery model at the same time is combinatorial and hence computationally prohibitive. To solve this problem, we propose a blind recovery model that simultaneously recovers multiple sequences, and an efficient approach to find proper combination of sampling strategy and recovery model. Our experiments demonstrate that the proposed method outperforms sequence-wise recovery, and sheds light on how to decide the undersampling strategy for sequences within an overall time budget.')
}}
{{ paper('MAC-ReconNet: A Multiple Acquisition Context based Convolutional Neural Network for MR Image Reconstruction using Dynamic Weight Prediction',
        'Sriprabha Ramanarayanan, Balamurali Murugesan, Keerthi Ram, Mohanasankar Sivaprakasam',
        openreview='https://openreview.net/forum?id=pMHk_HIZf7',
        pdf='https://openreview.net/pdf?id=pMHk_HIZf7',
        id='O056',
        paper='papers/ramanarayanan20.html',
        teaser='https://youtu.be/_rzsMOcyV3o',
        abstract='Convolutional Neural network based MR reconstruction methods have shown to provide fast and high quality reconstructions.  A primary drawback with a CNN-based model is that it lacks flexibility and can effectively operate only for a specific acquisition context limiting practical applicability.  By acquisition context, we mean a specific combination of three input settings considered namely, the anatomy under study, undersampling mask pattern and acceleration  factor  for  undersampling.   The  model  could be  trained  jointly  on  images  combining multiple contexts.  However the model does not meet the performance of context specific models nor extensible to contexts unseen at train time.  This necessitates a modification to the existing architecture in generating context specific weights so as to incorporate flexibility to multiple contexts. We propose a multiple acquisition context based network, called MAC-ReconNet for MRI reconstruction, flexible to multiple acquisition contexts and generalizable to unseen contexts for applicability in real scenarios. The proposed network has an MRI reconstruction module and a dynamic weight prediction (DWP) module.  The DWP module takes the corresponding acquisition context information  as  input  and  learns  the context-specific weights  of  the  reconstruction module which changes dynamically with context at run time.  We show that the proposed approach can handle multiple contexts  based on Cardiac and Brain datasets, Gaussian and Cartesian undersampling patterns and five acceleration factors. The proposed network outperforms the naive  jointly  trained model  and  gives  competitive results  with  the  context-specific  models both quantitatively and qualitatively.  We also demonstrate the generalizability of our model by testing on contexts unseen at train time.')
}}
{{ paper('A Heteroscedastic Uncertainty Model for Decoupling Sources of MRI Image Quality',
        'Richard Shaw, Carole H. Sudre, Sebastien Ourselin, M. Jorge Cardoso',
        openreview='https://openreview.net/forum?id=NnKIdnPXCr',
        pdf='https://openreview.net/pdf?id=NnKIdnPXCr',
        id='O171',
        paper='papers/shaw20.html',
        teaser='https://youtu.be/OezqOum9OEY',
        abstract='Quality control (QC) of medical images is essential to ensure that downstream analyses such as segmentation can be performed successfully. Currently, QC is predominantly performed visually at significant time and operator cost. We aim to automate the process by formulating a probabilistic network that estimates uncertainty through a heteroscedastic noise model, hence providing a proxy measure of task-specific image quality that is learnt directly from the data. By augmenting the training data with different types of simulated k-space artefacts, we propose a novel cascading CNN architecture based on a student-teacher framework with a weighted adaptive task loss to decouple sources of uncertainty related to different k-space augmentations in an entirely self-supervised manner. This enables us to predict separate uncertainty quantities for the different types of data degradation. While the uncertainty measures reflect the presence and severity of image artefacts, the network also provides the segmentation predictions given the quality of the data. We show that models trained with simulated artefacts provide more informative measures of uncertainty on real-world images and we validate our uncertainty predictions on problematic images identified by human-raters.')
}}
[% / %]


---


### WED 9:30-11:00 UTC-4 - Poster Session #5

[% .papers %]
{{ paper('Towards multi-sequence MR image recovery from undersampled k-space data',
        'Cheng Peng, Wei-An Lin, Rama Chellappa, S. Kevin Zhou',
        openreview='https://openreview.net/forum?id=Pk7In-gVEd',
        pdf='https://openreview.net/pdf?id=Pk7In-gVEd',
        id='O018',
        paper='papers/peng20b.html',
        teaser='',
        abstract='Undersampled MR image recovery has been widely studied for accelerated MR acquisition. However, it has been mostly studied under a single sequence scenario, despite the fact that multi-sequence MR scan is common in practice. In this paper, we aim to optimize multi-sequence MR image recovery from undersampled k-space data under an overall time constraint while considering the difference in acquisition time for various sequences. We first formulate it as a constrained optimization problem and then show that finding the optimal sampling strategy for all sequences and the best recovery model at the same time is combinatorial and hence computationally prohibitive. To solve this problem, we propose a blind recovery model that simultaneously recovers multiple sequences, and an efficient approach to find proper combination of sampling strategy and recovery model. Our experiments demonstrate that the proposed method outperforms sequence-wise recovery, and sheds light on how to decide the undersampling strategy for sequences within an overall time budget.')
}}
{{ paper('MAC-ReconNet: A Multiple Acquisition Context based Convolutional Neural Network for MR Image Reconstruction using Dynamic Weight Prediction',
        'Sriprabha Ramanarayanan, Balamurali Murugesan, Keerthi Ram, Mohanasankar Sivaprakasam',
        openreview='https://openreview.net/forum?id=pMHk_HIZf7',
        pdf='https://openreview.net/pdf?id=pMHk_HIZf7',
        id='O056',
        paper='papers/ramanarayanan20.html',
        teaser='https://youtu.be/_rzsMOcyV3o',
        abstract='Convolutional Neural network based MR reconstruction methods have shown to provide fast and high quality reconstructions.  A primary drawback with a CNN-based model is that it lacks flexibility and can effectively operate only for a specific acquisition context limiting practical applicability.  By acquisition context, we mean a specific combination of three input settings considered namely, the anatomy under study, undersampling mask pattern and acceleration  factor  for  undersampling.   The  model  could be  trained  jointly  on  images  combining multiple contexts.  However the model does not meet the performance of context specific models nor extensible to contexts unseen at train time.  This necessitates a modification to the existing architecture in generating context specific weights so as to incorporate flexibility to multiple contexts. We propose a multiple acquisition context based network, called MAC-ReconNet for MRI reconstruction, flexible to multiple acquisition contexts and generalizable to unseen contexts for applicability in real scenarios. The proposed network has an MRI reconstruction module and a dynamic weight prediction (DWP) module.  The DWP module takes the corresponding acquisition context information  as  input  and  learns  the context-specific weights  of  the  reconstruction module which changes dynamically with context at run time.  We show that the proposed approach can handle multiple contexts  based on Cardiac and Brain datasets, Gaussian and Cartesian undersampling patterns and five acceleration factors. The proposed network outperforms the naive  jointly  trained model  and  gives  competitive results  with  the  context-specific  models both quantitatively and qualitatively.  We also demonstrate the generalizability of our model by testing on contexts unseen at train time.')
}}
{{ paper('A Heteroscedastic Uncertainty Model for Decoupling Sources of MRI Image Quality',
        'Richard Shaw, Carole H. Sudre, Sebastien Ourselin, M. Jorge Cardoso',
        openreview='https://openreview.net/forum?id=NnKIdnPXCr',
        pdf='https://openreview.net/pdf?id=NnKIdnPXCr',
        id='O171',
        paper='papers/shaw20.html',
        teaser='https://youtu.be/OezqOum9OEY',
        abstract='Quality control (QC) of medical images is essential to ensure that downstream analyses such as segmentation can be performed successfully. Currently, QC is predominantly performed visually at significant time and operator cost. We aim to automate the process by formulating a probabilistic network that estimates uncertainty through a heteroscedastic noise model, hence providing a proxy measure of task-specific image quality that is learnt directly from the data. By augmenting the training data with different types of simulated k-space artefacts, we propose a novel cascading CNN architecture based on a student-teacher framework with a weighted adaptive task loss to decouple sources of uncertainty related to different k-space augmentations in an entirely self-supervised manner. This enables us to predict separate uncertainty quantities for the different types of data degradation. While the uncertainty measures reflect the presence and severity of image artefacts, the network also provides the segmentation predictions given the quality of the data. We show that models trained with simulated artefacts provide more informative measures of uncertainty on real-world images and we validate our uncertainty predictions on problematic images identified by human-raters.')
}}
[% / %]

[% .papers %]
{{ paper('Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks',
        'Jasper Linmans, Jeroen van der Laak, Geert Litjens',
        openreview='https://openreview.net/forum?id=hRwB2BTRNu',
        pdf='https://openreview.net/pdf?id=hRwB2BTRNu',
        id='P140',
        paper='papers/linmans20.html',
        teaser='https://youtu.be/aK8XWnWOKaE',
        abstract='Successful clinical implementation of deep learning in medical imaging depends, in part, on the reliability of the predictions. Specifically, the system should be accurate for classes seen during training while providing calibrated estimates of uncertainty for abnormalities and unseen classes. To efficiently estimate predictive uncertainty, we propose the use of multi-head convolutional neural networks (M-heads). We compare its performance to related and more prevalent approaches, such as deep ensembles, on the task of out-of-distribution (OOD) detection. To this end, we evaluate models, trained to discriminate normal lymph node tissue from breast cancer metastases, on lymph nodes containing lymphoma. We show the ability to discriminate between the in-distribution lymph node tissue and lymphoma by evaluating the AUROC based on the uncertainty signal. Here, the best performing multi-head CNN (91.7) outperforms both Monte Carlo dropout (86.5) and deep ensembles (86.8). Furthermore, we show that the meta-loss function of M-heads improves OOD detection in terms of AUROC from 87.4 to 88.7.')
}}
{{ paper('Skull-RCNN: A CNN-based network for the skull fracture detection',
        'Zhuo Kuang, Xianbo Deng, Li Yu, Hang Zhang, Xian lin, Hui Ma',
        openreview='https://openreview.net/forum?id=BUQyqaRhNH',
        pdf='https://openreview.net/pdf?id=BUQyqaRhNH',
        id='P177',
        paper='papers/kuang20.html',
        teaser='https://youtu.be/LkHM9w7VDFg',
        abstract='Skull fractures, following head trauma, may bring several complications and cause epidural hematomas. Therefore, it is of great significance to locate the fracture in time. However, the manual detection is time-consuming and laborious, and the previous studies for the automatic detection could not achieve the accuracy and robustness for clinical application. In this work, based on the Faster R-CNN, we propose a novel method for more accurate skull fracture detection results, and we name it as the Skull R-CNN. Guiding by the morphological features of the skull, a skeleton-based region proposal method is proposed to make candidate boxes more concentrated in key regions and reduced invalid boxes. With this advantage, the region proposal network in Faster R-CNN is removed for less computation. On the other hand, a novel full resolution feature network is constructed to obtain more precise features to make the model more snesetive to small objects. Experiment results showed that most of skull fractures could be detected correctly by the proposed method in a short time. Compared to the previous works on the skull fracture detecion, Skull R-CNN significantly reduces the less false positives, and keeps a high sensitivity.')
}}
{{ paper('Priority Unet: Detection of Punctuate White Matter Lesions in Preterm Neonate in 3D Cranial Ultrasonography',
        'ERBACHER Pierre, LARTIZIEN Carole, MARTIN Matthieu, FOLLETO PIMENTA Pedro, QUETIN Philippe, DELACHARTRE Philippe',
        openreview='https://openreview.net/forum?id=BpXY-yIs6f',
        pdf='https://openreview.net/pdf?id=BpXY-yIs6f',
        id='P228',
        paper='papers/pierre20.html',
        teaser='',
        abstract='Brain damage, particularly of cerebral white matter (WM), observed in premature infants in the neonatal period is responsible for frequent neurodevelopmental sequelae in early childhood and [V Pierrat et al. EPIPAGE-2 cohort study. BMJ. 2017]. Punctuate white matter lesions (PWML) are most frequent WM abnormalities, occurring in 18–35% of all preterm infants [AL Nguyen et al. Int Journal of Developmental Neuroscience, 2019] [N. Tusor et al, Scientific Reports, 2017].      Accurately assessing the volume and localisation of these lesions at the early postnatal phase can help paediatricians adapting the therapeutic strategy and potentially reduce severe sequelae. MRI is the gold standard neuroimaging tool to assess minimal to severe WM lesions, but it is only rarely performed for cost and accessibility reasons. Cranial ultrasonography (cUS) is a routinely used tool, however, the visual detection of PWM lesions  is challenging and time consuming because these lesions are small with variable contrast and no specific pattern. There are also weak anatomical landmarks in neonate brains as the brain structures are moving and not fully developed.      Research on automatic detection of PWML on MRI based on standard image analysis was initiated by Mukherjee [Mukherjee, S. et al. MBEC 57(1), 71-87, 2019]. One other team has recently tackled this issue based on deep architectures [Y Liu et al. MICCAI 2019]. Despite the high contrast and low noise of MR images, this algorithm struggles with low accuracy over the PWML detection task. As far as we know, there is currently no known research team working on automatic segmentation of PWML on US data. This task is highly challenging because of the speckle noise, low contrast and the high acquisition variability.      In this paper, we introduce a novel architecture based on the U-Net backbone to perform the detection and segmentation of PWML in cUS images. This model combines a soft attention model focusing on the PWML localisation and the self balancing focal loss (SBFL) introduced by Lin [Liu et al, arxiv, 2019]. The soft attention mask is a 3D probabilistic map derived from spatial prior knowledge of PWML localisation computed from our dataset.      Performance of this model is evaluated on a dataset of cUS exams including 21 patients acquired with a Acuson Siemens 4-9 MHZ probe. For each exam, a 3D volume of dimension 360x400x380 was reconstructed with an isotropic spatial resolution of 0.15 mm.  A total of 547 lesions were delineated on the images by an expert pediatrician. For this study, we considered 131 lesions with a volume bigger than 1.7 $mm^3$. Volumes of PWM lesions range from 1.75 $mm^3$ to 61.09 $mm^3$ with a median size of 4 $mm^3$.      The deep model was trained and validated with a 10-fold cross-validation based on approximately 3000 coronal slices extracted from the 3D volumes .  We also performed an ablation study to evaluate the impact of the attention gate and the focal loss. Detection performance was assessed at the lesion level, thus meaning that we performed a cluster analysis on the label maps outputted by the network using a 3D connectivity rule to identify the connected components.      Compared to the U-Net, the priority U-Net with SBFL increases the recall and the precision in the detection task from 0.4404      to 0.5370 and from 0.3217 to 0.5043, respectively. The Dice metric is also increased from 0.3040 to 0.3839 in the segmentation task.      In this study, we proposed the first use case of automated detection of PWML in cUS exams of preterms neonates as well as a novel deep architecture inspired from the attention gated U-Net combined with the self-balancing focal loss. Our results are shown to outperform the standard U-Net for this challenging detection task.')
}}
{{ paper('Training deep segmentation networks on texture-encoded input: application to neuroimaging of the developing neonatal brain',
        'Ahmed E. Fetit, John Cupitt, Turkay Kart, Daniel Rueckert',
        openreview='https://openreview.net/forum?id=vXX5bovYvi',
        pdf='https://openreview.net/pdf?id=vXX5bovYvi',
        id='P230',
        paper='papers/fetit20.html',
        teaser='https://youtu.be/5XPIAJMUHz8',
        abstract='Standard practice for using convolutional neural networks (CNNs) in semantic segmentation tasks assumes that the image intensities are directly used for training and inference. In natural images this is performed using RGB pixel intensities, whereas in medical imaging, e.g. magnetic resonance imaging (MRI), gray level pixel intensities are typically used. In this work, we explore the idea of encoding the image data as local binary textural maps prior to the feeding them to CNNs, and show that accurate segmentation models can be developed using such maps alone, without learning any representations from the images themselves. This questions common consensus that CNNs recognize objects from images by learning increasingly complex representations of shape, and suggests a more important role to image texture, in line with recent findings on natural images. We illustrate this for the first time on neuroimaging data of the developing neonatal brain in a tissue segmentation task, by analyzing large, publicly available T2-weighted MRI scans (n=558, range of postmenstrual ages at scan: 24.3 - 42.2 weeks) obtained retrospectively from the Developing Human Connectome Project cohort. Rapid changes in visual characteristics that take place during early brain development make it important to establish a clear understanding of the role of visual texture when training CNN models on neuroimaging data of the neonatal brain; this yet remains a largely understudied but important area of research. From a deep learning perspective, the results suggest that CNNs could simply be capable of learning representations from structured spatial information, and may not necessarily require conventional images as input. ')
}}
{{ paper('Prostate Cancer Semantic Segmentation by Gleason Score Group in mp-MRI with Self Attention Model on the Peripheral Zone',
        'Audrey Duran, Pierre-Marc Jodoin, Carole Lartizien',
        openreview='https://openreview.net/forum?id=Ih04Ji3rtN',
        pdf='https://openreview.net/pdf?id=Ih04Ji3rtN',
        id='P238',
        paper='papers/duran20.html',
        teaser='https://youtu.be/Jrj2SAtkPLY',
        abstract='Multiparametric magnetic resonance imaging (mp-MRI) has shown promising results in the detection of prostate cancer (PCa). However, discriminating clinically significant (CS) from benign lesions is time demanding and challenging, even for experienced readers, especially when individual MR sequences yield conflicting findings. Computer aided detection (CADe) or diagnostic (CADx) systems based on standard or deep supervised machine learning have achieved high performance in assisting radiologists for this diagnostic binary detection task.      We aim to go one step further in the diagnostic refinement by characterizing the aggressiveness of PCa lesions, assessed by the Gleason score (GS) group grading. This challenging problem has been very recently addressed from the deep learning perspective by a few groups.      In this work, we propose a novel end-to-end multiclass deep network to jointly perform the segmentation of the peripheral prostate zone (PZ) as well as the detection and GS Group grading of PZ lesions. Our U-Net inspired  architecture is constituted from a standard encoding part that first extracts the latent information from multichannel T2 weighted (T2w) and  apparent diffusion coefficient (ADC) input images. This latent representation is then connected to two separate decoding branches : 1) the first one performs a binary PZ segmentation 2) the second branch uses this zonal prior as an attention gate for the detection and grading of PZ lesions.      Performance of this model was evaluated on a dataset of 98 mp-MRI exams including 57 exams acquired on a 1.5 Tesla scanner (Symphony; Siemens, Erlangen, Germany) and 41 exams acquired on a 3 Tesla scanner (Discovery; General Electric, Milwaukee, USA). All patients underwent a prostatectomy after the MR exams. The prostatectomy specimens were analyzed a posteriori by an anatomopathologist thus providing the histological ground.  A total of 132 lesions were delineated on the images, including 37, 47, 23, 16 and 9 lesions of GS 6, 3+4, 4+3, 8 and ≥ 9, respectively. All lesions with a GS > 6 were considered as clinically significant.      The deep model was trained and validated with a 5-fold cross-validation. Performance of our model was compared to a U-Net baseline model to assess the impact of the self attention module on PCa detection.      A free-response receiver operating (FROC) analysis was conducted to evaluate the performance in detecting CS lesions and to discriminate lesions of the different GS groups.      Regarding the detection of CS lesions, our model achieves 75.78% sensitivity at 2.5 false positive per patient. Regarding the automatic GS group grading, the Cohen quadratic weighted kappa coefficient is 0.35, which is considered as a fair agreement and an improvement with regards to the baseline model. Our model reaches 78% and 18% sensitivity for GS ≥ 9 and GS 6 at 1 false positive per patient, respectively.      Our method achieves good performance without requiring any prior manual region delineation in clinical practice. We show that the addition of the proposed self attention mechanism improves the CAD performance in comparison to the baseline model.      ')
}}
{{ paper('Deep learning-based retinal vessel segmentation with cross-modal evaluation',
        'Luisa Sanchez Brea, Danilo Andrade De Jesus, Stefan Klein, Theo van Walsum',
        openreview='https://openreview.net/forum?id=-3UtpvQHNX',
        pdf='https://openreview.net/pdf?id=-3UtpvQHNX',
        id='P249',
        paper='papers/brea20.html',
        teaser='https://youtu.be/3Va3V4-2wl8',
        abstract='This work proposes a general pipeline for retinal vessel segmentation on en-face images. The main goal is to analyse if a model trained in one of two modalities, Fundus Photography (FP) or Scanning Laser Ophthalmoscopy (SLO), is transferable to the other modality accurately. This is motivated by the lack of development and data available in en-face imaging modalities other than FP. FP and SLO images of four and two publicly available datasets, respectively, were used. First, the current approaches were reviewed in order to define a basic pipeline for vessel segmentation. A state-of-art deep learning architecture (U-net) was used, and the effect of varying the patch size and number of patches was studied by training, validating, and testing on each dataset individually. Next, the model was trained in either FP or SLO images, using the available datasets for a given modality combined. Finally, the performance of each network was tested on the other modality. The models trained on each dataset showed a performance comparable to the state-of-the art and to the inter-rater reliability. Overall, the best performance was observed for the largest patch size (256) and the maximum number of overlapped images in each dataset, with a mean sensitivity, specificity, accuracy, and Dice score of 0.89$\\pm$0.05, 0.95$\\pm$0.02, 0.95$\\pm$0.02, and 0.73$\\pm$0.07, respectively. Models trained and tested on the same modality presented a sensitivity, specificity, and accuracy equal or higher than 0.9. The validation on a different modality has shown significantly better sensitivity and Dice on those trained on FP.')
}}
{{ paper('Laplacian pyramid-based complex neural network learning for fast MR imaging',
        'Haoyun Liang, Yu Gong, Hoel Kervadec, Jing Yuan, Hairong Zheng, Shanshan Wang',
        openreview='https://openreview.net/forum?id=0IeI8QS8N6',
        pdf='https://openreview.net/pdf?id=0IeI8QS8N6',
        id='P315',
        paper='papers/liang20.html',
        teaser='',
        abstract='A Laplacian pyramid-based complex neural network, CLP-Net, is proposed to reconstruct high-quality magnetic resonance images from undersampled k-space data. Specifically, three major contributions have been made: 1) A new framework has been proposed to explore the encouraging multi-scale properties of Laplacian pyramid decomposition; 2) A cascaded multi-scale network architecture with complex convolutions has been designed under the proposed framework; 3) Experimental validations on an open source dataset fastMRI demonstrate the encouraging properties of the proposed method in preserving image edges and fine textures.')
}}
{{ paper('Generating Fundus Fluorescence Angiography Images from Structure Fundus Images Using Generative Adversarial Networks',
        'Wanyue Li, Wen Kong, Yiwei Chen, Jing Wang, Yi He, Guohua Shi, Guohua Deng',
        openreview='https://openreview.net/forum?id=qhZM390B4',
        pdf='https://openreview.net/pdf?id=qhZM390B4',
        id='P333',
        paper='papers/li20.html',
        teaser='https://youtu.be/Lk5lHf9fvDw',
        abstract='Fluorescein angiography can provide a map of retinal vascular structure and function, which is commonly used in ophthalmology diagnosis, however, this imaging modality may pose risks of harm to the patients. To help physicians reduce the potential risks of diagnosis, an image translation method is adopted. In this work, we proposed a conditional generative adversarial network (GAN)-based method to directly learn the mapping relationship between structure fundus images and fundus fluorescence angiography (FFA) images. Moreover, local saliency maps, which define each pixel’s importance, are used to define a novel saliency loss in the GAN cost function. This facilitates more accurate learning of small-vessel and fluorescein leakage features. The proposed method was validated on our dataset and the publicly available Isfahan MISP dataset with the metrics of peak signal-to-noise ratio (PSNR) and structural similarity (SSIM). The experimental results indicate that the proposed method can accurately generate both retinal vascular and fluorescein leakage structures, which has great practical significance for clinical diagnosis and analysis.')
}}
{{ paper('Domain adaptation model for retinopathy detection from cross-domain OCT images',
        'Jing Wang, Yiwei Chen, Wanyue Li, Wen Kong, Yi He, Chunhui Jiang, Guohua Shi',
        openreview='https://openreview.net/forum?id=h5z-R09QRm',
        pdf='https://openreview.net/pdf?id=h5z-R09QRm',
        id='P334',
        paper='papers/wang20.html',
        teaser='https://youtu.be/Noi1JIBsITk',
        abstract='A deep neural network (DNN) can assist in retinopathy screening by automatically classifying patients into normal and abnormal categories according to optical coherence tomography (OCT) images. Typically, OCT images captured from different devices show heterogeneous appearances because of different scan settings; thus, the DNN model trained from one domain may fail if applied directly to a new domain. As data labels are difficult to acquire, we proposed a generative adversarial network-based domain adaptation model to address the cross-domain OCT images classification task, which can extract invariant and discriminative characteristics shared by different domains without incurring additional labeling cost. A feature generator, a Wasserstein distance estimator, a domain discriminator, and a classifier were included in the model to enforce the extraction of domain invariant representations. We applied the model to OCT images as well as public digit images. Results show that the model can significantly improve the classification accuracy of cross-domain images.')
}}
[% / %]

[% .papers %]
{{ paper('Learning to map between ferns with differentiable binary embedding networks',
        'Max Blendowski, Mattias P. Heinrich',
        openreview='https://openreview.net/forum?id=EiT7GQAj-T',
        pdf='https://openreview.net/pdf?id=EiT7GQAj-T',
        id='S133',
        paper='papers/blendowski20.html',
        teaser='https://youtu.be/a0266OkLfhw',
        abstract="Current deep learning methods are based on the repeated, expensive application of convolutions with parameter-intensive weight matrices. In this work, we present a novel concept that enables the application of differentiable random ferns in end-to-end networks. It can then be used as multiplication-free convolutional layer alternative in deep network architectures. Our experiments on the binary classification task of the TUPAC\\'16 challenge demonstrate improved results over the state-of-the-art binary XNOR net and only slightly worse performance than its 2x more parameter intensive floating point CNN counterpart. ")
}}
{{ paper('Segmentation of the Myocardium on Late-Gadolinium Enhanced MRI based on 2.5 D Residual Squeeze and Excitation Deep Learning Model',
        'Abdul Qayyum, Alain Lalande, Thomas Decourselle, Thibaut Pommier, Alexandre Cochet, Fabrice Meriaudeau',
        openreview='https://openreview.net/forum?id=4v2lR3Zvsw',
        pdf='https://openreview.net/pdf?id=4v2lR3Zvsw',
        id='S135',
        paper='papers/qayyum20.html',
        teaser='https://youtu.be/Gl1ioiS7IEE',
        abstract='Cardiac left ventricular (LV) segmentation from short-axis MRI acquired 10 minutes after the injection of a contrast agent (LGE-MRI) is a necessary step in the processing allowing the identification and diagnosis of cardiac diseases such as myocardial infarction. However, this segmentation is challenging due to high variability across subjects and the potential lack of contrast between structures. Then, the main objective of this work is to develop an accurate automatic segmentation method based on deep learning models for the myocardial borders on LGE-MRI. To this end, 2.5 D residual neural network integrated with a squeeze and excitation blocks in encoder side with specialized convolutional has been proposed. Late fusion has been used to merge the output of the best trained proposed models from a different set of hyperparameters. A total number of 320 exams (with a mean number of 6 slices per exam) were used for training and 28 exams used for testing. The performance analysis of the proposed ensemble model in the basal and middle slices was similar as compared to intra-observer study and slightly lower at apical slices. The overall Dice score was 82.01% by our proposed method as compared to Dice score of 83.22% obtained from the intra observer study. The proposed model could be used for the automatic segmentation of myocardial border that is a very important step for accurate quantification of no-reflow, myocardial infarction, myocarditis, and hypertrophic cardiomyopathy, among others.')
}}
{{ paper('Improving Mammography Malignancy Segmentation by Designing the Training Process',
        'Mickael Tardy, Diana Mateus',
        openreview='https://openreview.net/forum?id=vVsWe9-s0G',
        pdf='https://openreview.net/pdf?id=vVsWe9-s0G',
        id='S137',
        paper='papers/tardy20.html',
        teaser='https://youtu.be/w8W_NtJ2Rjg',
        abstract='We work on the breast imaging malignancy segmentation task while focusing on the train- ing process instead of network complexity. We designed a training process based on a modified U-Net, increasing the overall segmentation performances by using both, benign and malignant data for training. Our approach makes use of only a small amount of anno- tated data and relies on transfer learning from a self-supervised reconstruction task, and favors explainability.')
}}
{{ paper('Tackling the Problem of Large Deformations in Deep Learning Based Medical Image Registration Using Displacement Embeddings',
        'Lasse Hansen, Mattias P. Heinrich',
        openreview='https://openreview.net/forum?id=kPBUZluVq',
        pdf='https://openreview.net/pdf?id=kPBUZluVq',
        id='S155',
        paper='papers/hansen20.html',
        teaser='https://youtu.be/2uJ_H0G1f-0',
        abstract='Though, deep learning based medical image registration is currently starting to show promising advances, often, it still fells behind conventional frameworks in terms of reg- istration accuracy. This is especially true for applications where large deformations exist, such as registration of interpatient abdominal MRI or inhale-to-exhale CT lung registra- tion. Most current works use U-Net-like architectures to predict dense displacement fields from the input images in different supervised and unsupervised settings. We believe that the U-Net architecture itself to some level limits the ability to predict large deformations (even when using multilevel strategies) and therefore propose a novel approach, where the input images are mapped into a displacement space and final registrations are reconstructed from this embedding. Experiments on inhale-to-exhale CT lung registration demonstrate the ability of our architecture to predict large deformations in a single forward path through our network (leading to errors below 2 mm).')
}}
{{ paper('A Deep Learning Approach for Motion Forecasting Using 4D OCT Data',
        'Marcel Bengs, Nils Gessert, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=WVd56kgRV',
        pdf='https://openreview.net/pdf?id=WVd56kgRV',
        id='S156',
        paper='papers/bengs20.html',
        teaser='https://youtu.be/32BZ5eOHzTk',
        abstract='Forecasting motion of a specific target object is a common problem for surgical interventions, e.g. for localization of a target region, guidance for surgical interventions, or motion compensation. Optical coherence tomography (OCT) is an imaging modality with a high spatial and temporal resolution. Recently, deep learning methods have shown promising performance for OCT-based motion estimation based on two volumetric images. We extend this approach and investigate whether using a time series of volumes enables motion forecasting. We propose 4D spatio-temporal deep learning for end-to-end motion forecasting and estimation using a stream of OCT volumes. We design and evaluate five different 3D and 4D deep learning methods using a tissue data set. Our best performing 4D method  achieves motion forecasting with an overall average correlation coefficient of 97.41%, while also improving motion estimation performance by a factor of 2.5 compared to a previous 3D approach. ')
}}
{{ paper('An interpretable automated detection system for FISH-based HER2 oncogene amplification testing in histo-pathological routine images of breast and gastric cancer diagnostics',
        'Sarah Schmell, Falk Zakrzewski, Walter de Back, Martin Weigert, Uwe Schmidt, Torsten Wenke, Silke Zeugner, Robert Mantey, Christian Sperling, Ingo Roeder, Pia Hoenscheid, Daniela Aust, Gustavo Baretton',
        openreview='https://openreview.net/forum?id=qDEYfzeK7k',
        pdf='https://openreview.net/pdf?id=qDEYfzeK7k',
        id='S188',
        paper='papers/schmell20.html',
        teaser='https://youtu.be/z1OGEOr32og',
        abstract="Histo-pathological diagnostics are an inherent part of the everyday work but are particularly laborious and often associated with time-consuming manual analysis of image data. In order to cope with the increasing diagnostic case numbers due to the current growth and demographic change of the global population and the progress in personalized medicine, pathologists ask for assistance. Profiting from digital pathology and the use of artificial intelligence, individual solutions can be offered (e.g. to detect labeled cancer tissue sections). The testing of the human epidermal growth factor receptor 2 (HER2) oncogene amplification status via fluorescence in situ hybridization (FISH) is recommended for breast and gastric cancer diagnostics and is regularly performed at clinics. Here, we developed a comprehensible, multi-step deep learning-based pipeline which automates the evaluation of FISH images with respect to HER2 gene amplification testing. It mimics the pathological assessment and relies on the detection and localization of interphase nuclei based on instance segmentation networks. Furthermore, it localizes and classifies fluorescence signals within each nucleus with the help of image classification and object detection convolutional neural networks (CNNs). Finally, the pipeline classifies the whole image regarding its HER2 amplification status. The visualization of pixels on which the networks\\' decision occurs, complements an essential part to enable interpretability by pathologists.")
}}
{{ paper('A deep learning-based pipeline for error detection and quality control of brain MRI segmentation results',
        'Irene Brusini, Daniel Ferreira Padilla, José Barroso, Ingmar Skoog, Örjan Smedby, Eric Westman, Chunliang Wang',
        openreview='https://openreview.net/forum?id=sqbpwcNetg',
        pdf='https://openreview.net/pdf?id=sqbpwcNetg',
        id='S198',
        paper='papers/brusini20.html',
        teaser='https://youtu.be/X5DwVtX_noM',
        abstract='Brain MRI segmentation results should always undergo a quality control (QC) process, since automatic segmentation tools can be prone to errors. In this work, we propose two deep learning-based architectures for performing QC automatically. First, we used generative adversarial networks for creating error maps that highlight the locations of segmentation errors. Subsequently, a 3D convolutional neural network was implemented to predict segmentation quality. The present pipeline was shown to achieve promising results and, in particular, high sensitivity in both tasks.')
}}
{{ paper('An ENAS Based Approach for Constructing Deep Learning Models for Breast Cancer Recognition from Ultrasound Images',
        'Mohammed Ahmed, Hongbo Du, Alaa AlZoubi',
        openreview='https://openreview.net/forum?id=GxYt8XnZHM',
        pdf='https://openreview.net/pdf?id=GxYt8XnZHM',
        id='S211',
        paper='papers/ahmed20.html',
        teaser='https://youtu.be/kxrhngN8vRg',
        abstract='Deep Convolutional Neural Networks (CNN) provides an \\"end-to-end\\" solution for image pattern recognition with impressive performance in many areas of application including medical imaging. Most CNN models of high performance use hand-crafted network architectures that require expertise in CNNs to utilise their potentials. In this paper, we applied the Efficient Neural Architecture Search (ENAS) method to find optimal CNN architectures for classifying breast lesions from ultrasound (US) images. Our empirical study with a dataset of 524 US images shows that the optimal models generated by ENAS achieve an average accuracy of 89.3%, surpassing other hand-crafted alternatives. Furthermore, the models are simpler in complexity and more efficient. Our study demonstrates that the ENAS approach to CNN model design is a promising direction for classifying ultrasound images of breast lesions.')
}}
{{ paper('Joint Liver Lesion Segmentation and Classification via Transfer Learning',
        'Michal Heker, Hayit Greenspan',
        openreview='https://openreview.net/forum?id=8gSjgXg5U',
        pdf='https://openreview.net/pdf?id=8gSjgXg5U',
        id='S322',
        paper='papers/heker20.html',
        teaser='https://youtu.be/AFLwTiY2xKU',
        abstract="Transfer learning and joint learning approaches are extensively used to improve the performance of Convolutional Neural Networks (CNNs). In medical imaging applications in which the target dataset is typically very small, transfer learning improves feature learning while joint learning has shown effectiveness in improving the network\\'s generalization and robustness. In this work, we study the combination of these two approaches for the problem of liver lesion segmentation and classification.      For this purpose, 332 abdominal CT slices containing lesion segmentation and classification of three lesion types are evaluated. For feature learning, the dataset of MICCAI 2017 Liver Tumor Segmentation (LiTS) Challenge is used.      Joint learning shows improvement in both segmentation and classification results.      We show that a simple joint framework outperforms the commonly used multi-task architecture (Y-Net), achieving an improvement of 10% in classification accuracy, compared to 3% improvement with Y-Net.")
}}
[% / %]

---

### WED 11:00-12:00 UTC-4 - Keynote #4 - Elsa Angelini


### WED 12:00-12:30 UTC-4 - Break

---

### WED 12:30-13:30 UTC-4 - Oral Session #6 - Attention

Session Chairs: Pierre-Marc Jodoin, April Khademi

[% .papers %]
{{ paper('Automatic Diagnosis of Pulmonary Embolism Using an Attention-guided Framework: A Large-scale Study',
        'Luyao Shi, Deepta Rajan, Shafiq Abedin, David Beymer, Ehsan Dehghan',
        openreview='https://openreview.net/forum?id=hsGCHJDRm2',
        pdf='https://openreview.net/pdf?id=hsGCHJDRm2',
        id='O042',
        paper='papers/shi20.html',
        teaser='https://youtu.be/GSQIJjNgytQ',
        abstract='Pulmonary Embolism (PE) is a life-threatening disorder associated with high mortality and morbidity. Prompt diagnosis and immediate initiation of therapeutic action is important. We explored a deep learning model to detect PE on volumetric contrast-enhanced chest CT scans using a 2-stage training strategy. First, a residual convolutional neural network (ResNet) was trained using annotated 2D images. In addition to the classification loss, an attention loss was added during training to help the network focus attention on PE. Next, a recurrent network was used to scan sequentially through the features provided by the pre-trained ResNet to detect PE. This combination allows the network to be trained using both a limited and sparse set of pixel-level annotated images and a large number of easily obtainable patient-level image-label pairs. We used 1,670 sparsely annotated studies and more than 10,000 labeled studies in our training. On a test set with 2,160 patient studies, the proposed method achieved an area under the ROC curve (AUC) of 0.812. The proposed framework is also able to provide localized attention maps that indicate possible PE lesions, which could potentially help radiologists accelerate the diagnostic process.')
}}
{{ paper('Automated Labelling using an Attention model for Radiology reports of MRI scans (ALARM)',
        'David Wood, Emily Guilhem, Antanas Montvila, Thomas Varsavsky, Martin Kiik, Juveria Siddiqui, Sina Kafiabadi, Naveen Gadapa, Aisha Al Busaidi, Matt Townend, Keena Patel, Gareth Barker, Sebastian Ourselin, Jeremy Lynch, James Cole, Tom Booth',
        openreview='https://openreview.net/forum?id=9exoP7PDD3',
        pdf='https://openreview.net/pdf?id=9exoP7PDD3',
        id='O089',
        paper='papers/wood20.html',
        teaser='',
        abstract='Labelling large datasets for training high-capacity neural networks is a major obstacle to      the development of deep learning-based medical imaging applications. Here we present a      transformer-based network for magnetic resonance imaging (MRI) radiology report classification which automates this task by assigning image labels on the basis of free-text expert      radiology reports. Our model’s performance is comparable to that of an expert radiologist,      and better than that of an expert physician, demonstrating the feasibility of this approach.      We make code available online for researchers to label their own MRI datasets for medical      imaging applications.')
}}
{{ paper('Locating Cephalometric X-Ray Landmarks with Foveated Pyramid Attention',
        'Logan Gilmour, Nilanjan Ray',
        openreview='https://openreview.net/forum?id=6oG9zkHVLa',
        pdf='https://openreview.net/pdf?id=6oG9zkHVLa',
        id='O303',
        paper='papers/gilmour20.html',
        teaser='',
        abstract='CNNs, initially inspired by human vision, differ in a key way: they sample uniformly, rather than with highest density in a focal point. For very large images, this makes training untenable, as the memory and computation required for activation maps scales quadratically with the side length of an image. We propose an image pyramid based approach that extracts narrow glimpses of the of the input image and iteratively refines them to accomplish regression tasks. To assist with high-accuracy regression, we introduce a novel intermediate representation we call ‘spatialized features’. Our approach scales logarithmically with the side length, so it works with very large images. We apply our method to Cephalometric X-ray Landmark Detection and get state-of-the-art results.')
}}
[% / %]

---

### WED 13:30-15:00 UTC-4 - Poster Session #6

[% .papers %]
{{ paper('Automatic Diagnosis of Pulmonary Embolism Using an Attention-guided Framework: A Large-scale Study',
        'Luyao Shi, Deepta Rajan, Shafiq Abedin, David Beymer, Ehsan Dehghan',
        openreview='https://openreview.net/forum?id=hsGCHJDRm2',
        pdf='https://openreview.net/pdf?id=hsGCHJDRm2',
        id='O042',
        paper='papers/shi20.html',
        teaser='https://youtu.be/GSQIJjNgytQ',
        abstract='Pulmonary Embolism (PE) is a life-threatening disorder associated with high mortality and morbidity. Prompt diagnosis and immediate initiation of therapeutic action is important. We explored a deep learning model to detect PE on volumetric contrast-enhanced chest CT scans using a 2-stage training strategy. First, a residual convolutional neural network (ResNet) was trained using annotated 2D images. In addition to the classification loss, an attention loss was added during training to help the network focus attention on PE. Next, a recurrent network was used to scan sequentially through the features provided by the pre-trained ResNet to detect PE. This combination allows the network to be trained using both a limited and sparse set of pixel-level annotated images and a large number of easily obtainable patient-level image-label pairs. We used 1,670 sparsely annotated studies and more than 10,000 labeled studies in our training. On a test set with 2,160 patient studies, the proposed method achieved an area under the ROC curve (AUC) of 0.812. The proposed framework is also able to provide localized attention maps that indicate possible PE lesions, which could potentially help radiologists accelerate the diagnostic process.')
}}
{{ paper('Automated Labelling using an Attention model for Radiology reports of MRI scans (ALARM)',
        'David Wood, Emily Guilhem, Antanas Montvila, Thomas Varsavsky, Martin Kiik, Juveria Siddiqui, Sina Kafiabadi, Naveen Gadapa, Aisha Al Busaidi, Matt Townend, Keena Patel, Gareth Barker, Sebastian Ourselin, Jeremy Lynch, James Cole, Tom Booth',
        openreview='https://openreview.net/forum?id=9exoP7PDD3',
        pdf='https://openreview.net/pdf?id=9exoP7PDD3',
        id='O089',
        paper='papers/wood20.html',
        teaser='',
        abstract='Labelling large datasets for training high-capacity neural networks is a major obstacle to      the development of deep learning-based medical imaging applications. Here we present a      transformer-based network for magnetic resonance imaging (MRI) radiology report classification which automates this task by assigning image labels on the basis of free-text expert      radiology reports. Our model’s performance is comparable to that of an expert radiologist,      and better than that of an expert physician, demonstrating the feasibility of this approach.      We make code available online for researchers to label their own MRI datasets for medical      imaging applications.')
}}
{{ paper('Locating Cephalometric X-Ray Landmarks with Foveated Pyramid Attention',
        'Logan Gilmour, Nilanjan Ray',
        openreview='https://openreview.net/forum?id=6oG9zkHVLa',
        pdf='https://openreview.net/pdf?id=6oG9zkHVLa',
        id='O303',
        paper='papers/gilmour20.html',
        teaser='',
        abstract='CNNs, initially inspired by human vision, differ in a key way: they sample uniformly, rather than with highest density in a focal point. For very large images, this makes training untenable, as the memory and computation required for activation maps scales quadratically with the side length of an image. We propose an image pyramid based approach that extracts narrow glimpses of the of the input image and iteratively refines them to accomplish regression tasks. To assist with high-accuracy regression, we introduce a novel intermediate representation we call ‘spatialized features’. Our approach scales logarithmically with the side length, so it works with very large images. We apply our method to Cephalometric X-ray Landmark Detection and get state-of-the-art results.')
}}
[% / %]

[% .papers %]
{{ paper('Brain Metastasis Segmentation Network Trained with Robustness to Annotations with Multiple False Negatives',
        'Darvin Yi, Endre Grøvik, Michael Iv, Elizabeth Tong, Greg Zaharchuk, Daniel Rubin',
        openreview='https://openreview.net/forum?id=55VoQFvQM',
        pdf='https://openreview.net/pdf?id=55VoQFvQM',
        id='P048',
        paper='papers/yi20.html',
        teaser='',
        abstract='Deep learning has proven to be an essential tool for medical image analysis.  However, the need for accurately labeled input data, often requiring time- and labor-intensive annotation by experts, is a major limitation to the use of deep learning.  One solution to this challenge is to allow for use of coarse or noisy labels, which could permit more efficient and scalable labeling of images.  In this work, we develop a lopsided loss function based on entropy regularization that assumes the existence of a nontrivial false negative rate in the target annotations.  Starting with a carefully annotated brain metastasis lesion dataset, we simulate data with false negatives by (1) randomly censoring the annotated lesions and (2) systematically censoring the smallest lesions.  The latter better models true physician error because smaller lesions are harder to notice than the larger ones.  Even with a simulated false negative rate as high as 50%, applying our loss function to randomly censored data preserves maximum sensitivity at 97% of the baseline with uncensored training data, compared to just 10% for a standard loss function.  For the size-based censorship, performance is restored from 17% with the current standard to 88% with our lopsided bootstrap loss.  Our work will enable more efficient scaling of the image labeling process, in parallel with other approaches on creating more efficient user interfaces and tools for annotation.')
}}
{{ paper('Feature Disentanglement to Aid Imaging Biomarker Characterization for Genetic Mutations',
        'Padmaja Jonnalagedda, Brent Weinberg, Jason Allen, Bir Bhanu',
        openreview='https://openreview.net/forum?id=QIK9UQ_omc',
        pdf='https://openreview.net/pdf?id=QIK9UQ_omc',
        id='P250',
        paper='papers/jonnalagedda20.html',
        teaser='https://youtu.be/gKkd8WLYqYQ',
        abstract='Various mutations have been shown to correlate with prognosis of High-Grade Glioma (Glioblastoma). Overall prognostic assessment requires analysis of multiple modalities: imaging, molecular and clinical. To optimize this assessment pipeline, this paper develops the first deep learning-based system that uses MRI data to predict 19/20 co-gain, a mutation that indicates median survival. The paper addresses two key challenges when dealing with deep learning algorithms and medical data: lack of data and high data imbalance. We propose an unified approach that consists of a Feature Disentanglement (FeaD-GAN) technique for generating synthetic images to address these challenges, that projects features and re-samples from a pseudo-larger data distribution to generate synthetic images from very limited data. A thorough analysis is performed to (a) characterize aspects of visual manifestation of 19/20 co-gain that demonstrates the effectiveness of FeaD-GAN and (b) demonstrate that not only do the imaging biomarkers of 19/20 co-gain exist, but they are reproducible as well.')
}}
{{ paper('Understanding Alzheimer disease’s structural connectivity through explainable AI',
        'Achraf Essemlali, Etienne St-Onge, Jean Christophe Houde, Pierre Marc Jodoin, Maxime Descoteaux',
        openreview='https://openreview.net/forum?id=K75ya1BJMK',
        pdf='https://openreview.net/pdf?id=K75ya1BJMK',
        id='P304',
        paper='papers/essemlali20.html',
        teaser='https://youtu.be/SyBlSUyR10E',
        abstract='In the following work, we use a modified version of deep BrainNet convolutional neural network (CNN) trained on the diffusion weighted MRI (DW-MRI) tractography connectomes of patients with Alzheimer’s Disease (AD) and Mild Cognitive Impairment (MCI) to better understand the structural connectomics of that disease. We show that with a relatively simple connectomic BrainNetCNN used to classify brain images and explainable AI techniques, one can underline brain regions and their connectivity involved in AD. Results reveal that the connected regions with high structural differences between groups are those also reported in previous AD literature. Our findings support that deep learning over structural connectomes is a powerful tool to leverage the complex structure within connectomes derived from diffusion MRI tractography. To our knowledge, our contribution is the first explainable AI work applied to structural analysis of a degenerative disease.')
}}
{{ paper('Fast Mitochondria Detection for Connectomics',
        'Vincent Casser, Kai Kang, Hanspeter Pfister, Daniel Haehn',
        openreview='https://openreview.net/forum?id=dGd1Z9CHAg',
        pdf='https://openreview.net/pdf?id=dGd1Z9CHAg',
        id='P327',
        paper='papers/casser20.html',
        teaser='https://youtu.be/QKUjkkbjMxg',
        abstract='High-resolution connectomics data allows for the identification of dysfunctional mitochondria which are linked to a variety of diseases such as autism or bipolar. However, manual analysis is not feasible since datasets can be petabytes in size. We present a fully automatic mitochondria detector based on a modified U-Net architecture that yields high accuracy and fast processing times. We evaluate our method on multiple real-world connectomics datasets, including an improved version of the EPFL mitochondria benchmark. Our results show a Jaccard index of up to 0.90 with inference times lower than 16ms for a 512x512px image tile. This speed is faster than the acquisition speed of modern electron microscopes, enabling mitochondria detection in real-time. Compared to previous work, our detector ranks first for real-time detection and can be used for image alignment. Our data, results, and code are freely available. ')
}}
{{ paper('Adversarial Domain Adaptation for Cell Segmentation',
        'Mohammad Minhazul Haq, Junzhou Huang',
        openreview='https://openreview.net/forum?id=mgvieZlHlv',
        pdf='https://openreview.net/pdf?id=mgvieZlHlv',
        id='P336',
        paper='papers/haq20.html',
        teaser='https://youtu.be/pZe6N4pro4E',
        abstract='To successfully train a cell segmentation network in fully-supervised manner for a particular type of organ or cancer, we need the dataset with ground-truth annotations. However, high unavailability of such annotated dataset and tedious labeling process enforce us to discover a way for training with unlabeled dataset. In this paper, we propose a network named CellSegUDA for cell segmentation on the unlabeled dataset (target domain). It is achieved by applying unsupervised domain adaptation (UDA) technique with the help of another labeled dataset (source domain) that may come from other organs or sources. We validate our proposed CellSegUDA on two public cell segmentation datasets and obtain significant improvement as compared with the baseline methods. Finally, considering the scenario when we have a small number of annotations available from the target domain, we extend our work to CellSegSSDA, a semi-supervised domain adaptation (SSDA) based approach. Our SSDA model also gives excellent results which are quite close to the fully-supervised upper bound in target domain.')
}}
[% / %]

[% .papers %]
{{ paper('Image Translation by Latent Union of Subspaces for Cross-Domain Plaque Segmentation',
        'Yingying Zhu, Daniel C. Elton, Sungwon Lee, Perry J. Pickhardt, Ronald M. Summers',
        openreview='https://openreview.net/forum?id=qJxBTPyVYA',
        pdf='https://openreview.net/pdf?id=qJxBTPyVYA',
        id='S266',
        paper='papers/zhu20.html',
        teaser='https://youtu.be/ZD1pL8D2oIE',
        abstract='Calcified plaque in the aorta and pelvic arteries is associated with coronary artery calcification and is a strong predictor of heart attack. Current calcified plaque detection models show poor generalizeability to different domains (ie. pre-contrast vs. post-contrast CT scans). Many recent works have shown how cross domain object detection can be improved using an image translation model which translates between domains using a single shared latent space. However, while current image translation models do a good job preserving global/intermediate level structures they often have trouble preserving tiny structures. In medical imaging applications, preserving small structures is important since these structures can carry information which is highly relevant for disease diagnosis. Recent works on image reconstruction show that complex real-world images are better reconstructed using a union of subspaces approach. Since small image patches are used to train the image translation model, it makes sense to enforce that each patch be represented by a linear combination of subspaces which may correspond to the different parts of the body present in that patch. Motivated by this, we propose an image translation network using a shared union of subspaces constraint and show our approach preserves subtle structures (plaques) better than the conventional method. We further applied our method to a cross domain plaque detection task and show significant improvement compared to the state-of-the art method.')
}}
{{ paper('Vispi: Automatic Visual Perception and Interpretation of Chest X-rays',
        'Xin Li, Rui Cao, Dongxiao Zhu',
        openreview='https://openreview.net/forum?id=otswIbmgYA',
        pdf='https://openreview.net/pdf?id=otswIbmgYA',
        id='S276',
        paper='papers/li20.html',
        teaser='https://youtu.be/-un_xVu-hu0',
        abstract='Computer-aided medical image visual perception and interpretation with deep learning remain a challenging task, due to the lack of high-quality annotated image-report pairs and tailor-made generative models for sufficient extraction and exploitation of localized semantic features associated with abnormalities. To tackle these challenges, we present Vispi, an automatic medical image interpretation system, which first annotates an image via classifying and localizing common thoracic diseases with visual support and then followed by report generation from an attentive LSTM model. Analyzing an open IU X-ray dataset, we demonstrate a superior performance of Vispi in disease classification, localization and report generation using automatic performance evaluation metrics ROUGE and CIDEr.')
}}
{{ paper('Uncertainty Evaluation Metrics for Brain Tumour Segmentation',
        'Raghav Mehta, Angelos Filos, Yarin Gal, Tal Arbel',
        openreview='https://openreview.net/forum?id=H-PvDNIex',
        pdf='https://openreview.net/pdf?id=H-PvDNIex',
        id='S282',
        paper='papers/mehta20.html',
        teaser='https://youtu.be/1jVyfnhw1xM',
        abstract='In this paper, we describe and explore the metric that was designed to assess and rank uncertainty measures for the task of brain tumour sub-tissue segmentation in the BraTS 2019 sub-challenge on uncertainty quantification. The metric is designed to (1) reward uncertainty measures where high confidence is assigned to correct assertions, and where incorrect assertions are assigned low confidence and (2) penalize measures that have higher percentages of under-confident correct assertions.  Here, the workings of the metrics explored based on a number of popular uncertainty measures evaluated on the BraTS2019 dataset')
}}
{{ paper('Multiple resolution residual network for automatic thoracic organs-at-risk segmentation from CT',
        'Hyemin Um, Jue Jiang, Maria Thor, Andreas Rimner, Leo Luo, Joseph O. Deasy, Harini Veeraraghavan',
        openreview='https://openreview.net/forum?id=h3Miqa_jqN',
        pdf='https://openreview.net/pdf?id=h3Miqa_jqN',
        id='S308',
        paper='papers/um20.html',
        teaser='https://youtu.be/wmUgVsE_w38',
        abstract='We implemented and evaluated a multiple resolution residual network (MRRN) for multiple normal organs-at-risk (OAR) segmentation from computed tomography (CT) images for thoracic radiotherapy treatment (RT) planning. Our approach simultaneously combines feature streams computed at multiple image resolutions and feature levels through residual connections. The feature streams at each level are updated as the images are passed through various feature levels. We trained our approach using 206 thoracic CT scans of lung cancer patients with 35 scans held out for validation to segment the left and right lungs, heart, esophagus, and spinal cord. This approach was tested on the 60 CT scans from the open-source AAPM Thoracic Auto-Segmentation Challenge dataset. Performance was measured using the Dice Similarity Coefficient (DSC). Our approach outperformed the best-performing method in the grand challenge for hard-to-segment structures like the esophagus and achieved comparable results for all other structures. Median DSC using our method was 0.97 (interquartile range [IQR]: 0.97-0.98) for the left and right lungs, 0.93 (IQR: 0.93-0.95) for the heart, 0.78 (IQR: 0.76-0.80) for the esophagus, and 0.88 (IQR: 0.86-0.89) for the spinal cord. ')
}}
{{ paper('Using Generative Models for Pediatric wbMRI',
        'Alex Chang, Vinith M. Suriyakumar, Abhishek Moturu, Nipaporn Tewattanarat, Andrea Doria, Anna Goldenberg',
        openreview='https://openreview.net/forum?id=BXC_fpbLe',
        pdf='https://openreview.net/pdf?id=BXC_fpbLe',
        id='S312',
        paper='papers/chang20.html',
        teaser='',
        abstract='Early detection of cancer is key to a good prognosis and requires frequent testing, especially in pediatrics. Whole-body magnetic resonance imaging (wbMRI) is an essential part of several well-established screening protocols with screening starting in early childhood. To date, machine learning (ML) has been used on wbMRI images to stage adult cancer patients. It is not possible to use such tools in pediatrics due to the changing bone signal throughout growth, the difficulty of obtaining these images in young children due to movement and limited compliance, and the rarity of positive cases. We evaluate the quality of wbMRI images generated using generative adversarial networks (GANs) trained on wbMRI data from a pediatric hospital. We use the Fréchet Inception Distance (FID) metric, Domain Fréchet Distance (DFD), and blind tests with a radiology fellow for evaluation. We demonstrate that StyleGAN2 provides the best performance in generating wbMRI images with respect to all three metrics.')
}}
[% / %]

---

### WED 15:00-15:30 UTC-4 - Closings


---

## Thursday July 9 - 9:00-17:00 UTC-4 - [Challenges](/challenges.html)

* 14:00-17:00 UTC-4 - [MC-MRRec](https://sites.google.com/view/calgary-campinas-dataset/home/mr-reconstruction-challenge):
 Multi-channel MR Image Reconstruction Challenge
* 9:00-13:00 UTC-4 - [SARAS](https://saras-esad.grand-challenge.org):
 SARAS endoscopic vision challenge for surgeon action detection
* 9:00-13:00 UTC-4 - [object-CXR](https://jfhealthcare.github.io/object-CXR/):
 Automatic detection of foreign objects on chest X-rays