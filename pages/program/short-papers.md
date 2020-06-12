---
title: "Short papers"
---

{% from "_macros.html" import paper %}

# Short papers

[% .papers %]
{{ paper('4D Deep Learning for Multiple-Sclerosis Lesion Activity Segmentation',
        'Nils Gessert, Marcel Bengs, Julia Krüger, Roland Opfer, Ann-Christin Ostwaldt, Praveena Manogaran, Sven Schippling, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=238UzYB1d9',
        id='S092',
        paper='papers/gessert20.html',
        abstract='Multiple sclerosis lesion activity segmentation is the task of detecting new and enlarging lesions that appeared between a baseline and a follow-up brain MRI scan. While deep learning methods for single-scan lesion segmentation are common, deep learning approaches for lesion activity have only been proposed recently. Here, a two-path architecture processes two 3D MRI volumes from two time points. In this work, we investigate whether extending this problem to full 4D deep learning using a history of MRI volumes and thus an extended baseline can improve performance. For this purpose, we design a recurrent multi-encoder-decoder architecture for processing 4D data. We find that adding more temporal information is beneficial and our proposed architecture outperforms previous approaches with a lesion-wise true positive rate of 0.84 at a lesion-wise false positive rate of 0.19.')
}}
{{ paper('A CNN-LSTM Architecture for Detection of Intracranial Hemorrhage on CT scans',
        'Nhan T. Nguyen, Dat Q. Tran, Nghia T. Nguyen, Ha Q. Nguyen',
        openreview='https://openreview.net/forum?id=1IoPbyuPFT',
        id='S041',
        paper='papers/nguyen20.html',
        abstract='We propose a novel method that combines a convolutional neural network (CNN) with a long short-term memory (LSTM) mechanism for accurate prediction of intracranial hemorrhage on computed tomography (CT) scans. The CNN plays the role of a slice-wise feature extractor while the LSTM is responsible for linking the features across slices. The whole architecture is trained end-to-end with input being an RGB-like image formed by stacking 3 different viewing windows of a single slice. We validate the method on the recent RSNA Intracranial Hemorrhage Detection challenge and on the CQ500 dataset. For the RSNA challenge, our best single model achieves a weighted log loss of 0.0529 on the leaderboard, which is comparable to the top 3\\% performances, almost all of which make use of ensemble learning. Importantly, our method generalizes very well: the model trained on the RSNA dataset significantly outperforms the 2D model, which does not take into account the relationship between slices, on CQ500. Our codes and models will be made public.')
}}
{{ paper('A Deep Learning Approach for Motion Forecasting Using 4D OCT Data',
        'Marcel Bengs, Nils Gessert, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=WVd56kgRV',
        id='S156',
        paper='papers/bengs20.html',
        abstract='Forecasting motion of a specific target object is a common problem for surgical interventions, e.g. for localization of a target region, guidance for surgical interventions, or motion compensation. Optical coherence tomography (OCT) is an imaging modality with a high spatial and temporal resolution. Recently, deep learning methods have shown promising performance for OCT-based motion estimation based on two volumetric images. We extend this approach and investigate whether using a time series of volumes enables motion forecasting. We propose 4D spatio-temporal deep learning for end-to-end motion forecasting and estimation using a stream of OCT volumes. We design and evaluate five different 3D and 4D deep learning methods using a tissue data set. Our best performing 4D method  achieves motion forecasting with an overall average correlation coefficient of 97.41%, while also improving motion estimation performance by a factor of 2.5 compared to a previous 3D approach. ')
}}
{{ paper('A Deep Learning based Fast Signed Distance Map Generation',
        'Zihao Wang, Clair Vandersteen, Thomas Demarcy, Dan Gnansia, Charles Raffaelli, Nicolas Guevara, Hervé Delingette',
        openreview='https://openreview.net/forum?id=b2N5ZuEouu',
        id='S033',
        paper='papers/wang20.html',
        abstract='Signed distance map (SDM) is a common representation of surfaces in medical image analysis and machine learning. The computational complexity of SDM for 3D parametric shapes is often a bottleneck in many applications, thus limiting their interest. In this paper, we propose a learning-based SDM generation neural network which is demonstrated on a tridimensional cochlea shape model parameterized by 4 shape parameters.      The proposed SDM Neural Network generates a cochlea signed distance map depending on four input parameters and we show that the deep learning approach leads to a 60 fold improvement in the time of computation compared to more classical SDM generation methods. Therefore, the proposed approach achieves a good trade-off between accuracy and efficiency. ')
}}
{{ paper('A Fully Convolutional Normalization Approach of Head and Neck Cancer Outcome Prediction',
        'William Le, Francisco Perdigón Romero, Samuel Kadoury',
        openreview='https://openreview.net/forum?id=JojEzQ3E5n',
        id='S145',
        paper='papers/le20.html',
        abstract='Medical image classification performance worsens in multi-domain datasets, caused by radiological image differences across institutions, scanner manufacturer, model and operator. Deep learning is well-suited for learning image features with priors encoded as constraints during the training process.  In this work, we apply a ResNeXt classification network augmented with an FCN preprocessor subnetwork to a public TCIA head and neck cancer dataset. The training goal is survival prediction of radiotherapy cases based on pre-treatment FDG-PET/CT scans, acquired across 4 different hospitals.  We show that the preprocessor sub-network acts as a embedding normalizer and improves over state-of-the-art results of 70% AUC to 76%.')
}}
{{ paper('A deep learning-based pipeline for error detection and quality control of brain MRI segmentation results',
        'Irene Brusini, Daniel Ferreira Padilla, José Barroso, Ingmar Skoog, Örjan Smedby, Eric Westman, Chunliang Wang',
        openreview='https://openreview.net/forum?id=sqbpwcNetg',
        id='S198',
        paper='papers/brusini20.html',
        abstract='Brain MRI segmentation results should always undergo a quality control (QC) process, since automatic segmentation tools can be prone to errors. In this work, we propose two deep learning-based architectures for performing QC automatically. First, we used generative adversarial networks for creating error maps that highlight the locations of segmentation errors. Subsequently, a 3D convolutional neural network was implemented to predict segmentation quality. The present pipeline was shown to achieve promising results and, in particular, high sensitivity in both tasks.')
}}
{{ paper('An ENAS Based Approach for Constructing Deep Learning Models for Breast Cancer Recognition from Ultrasound Images',
        'Mohammed Ahmed, Hongbo Du, Alaa AlZoubi',
        openreview='https://openreview.net/forum?id=GxYt8XnZHM',
        id='S211',
        paper='papers/ahmed20.html',
        abstract='Deep Convolutional Neural Networks (CNN) provides an \\"end-to-end\\" solution for image pattern recognition with impressive performance in many areas of application including medical imaging. Most CNN models of high performance use hand-crafted network architectures that require expertise in CNNs to utilise their potentials. In this paper, we applied the Efficient Neural Architecture Search (ENAS) method to find optimal CNN architectures for classifying breast lesions from ultrasound (US) images. Our empirical study with a dataset of 524 US images shows that the optimal models generated by ENAS achieve an average accuracy of 89.3%, surpassing other hand-crafted alternatives. Furthermore, the models are simpler in complexity and more efficient. Our study demonstrates that the ENAS approach to CNN model design is a promising direction for classifying ultrasound images of breast lesions.')
}}
{{ paper('An interpretable automated detection system for FISH-based HER2 oncogene amplification testing in histo-pathological routine images of breast and gastric cancer diagnostics',
        'Sarah Schmell, Falk Zakrzewski, Walter de Back, Martin Weigert, Uwe Schmidt, Torsten Wenke, Silke Zeugner, Robert Mantey, Christian Sperling, Ingo Roeder, Pia Hoenscheid, Daniela Aust, Gustavo Baretton',
        openreview='https://openreview.net/forum?id=qDEYfzeK7k',
        id='S188',
        paper='papers/schmell20.html',
        abstract="Histo-pathological diagnostics are an inherent part of the everyday work but are particularly laborious and often associated with time-consuming manual analysis of image data. In order to cope with the increasing diagnostic case numbers due to the current growth and demographic change of the global population and the progress in personalized medicine, pathologists ask for assistance. Profiting from digital pathology and the use of artificial intelligence, individual solutions can be offered (e.g. to detect labeled cancer tissue sections). The testing of the human epidermal growth factor receptor 2 (HER2) oncogene amplification status via fluorescence in situ hybridization (FISH) is recommended for breast and gastric cancer diagnostics and is regularly performed at clinics. Here, we developed a comprehensible, multi-step deep learning-based pipeline which automates the evaluation of FISH images with respect to HER2 gene amplification testing. It mimics the pathological assessment and relies on the detection and localization of interphase nuclei based on instance segmentation networks. Furthermore, it localizes and classifies fluorescence signals within each nucleus with the help of image classification and object detection convolutional neural networks (CNNs). Finally, the pipeline classifies the whole image regarding its HER2 amplification status. The visualization of pixels on which the networks\\' decision occurs, complements an essential part to enable interpretability by pathologists.")
}}
{{ paper('Anatomical Predictions using Subject-Specific Medical Data',
        'Marianne Rakic, John Guttag, Adrian V. Dalca',
        openreview='https://openreview.net/forum?id=apwZYLKTCo',
        id='S236',
        paper='papers/rakic20.html',
        abstract='Changes in brain anatomy can provide important insight for treatment design or scientific analyses. We present a method that predicts how brain anatomy for an individual will change over time. We model these changes through a diffeomorphic deformation field, and design a predictive function using convolutional neural networks. Given a predicted deformation field, a baseline scan can be warped to give a prediction of the brain scan at a future time. We demonstrate the method using the ADNI cohort, and analyze how performance is affected by model variants and the type of subject-specific information provided. We show that the model provides good predictions and that external clinical data can improve predictions.      ')
}}
{{ paper('Assessing the validity of saliency maps for abnormality localization in medical imaging',
        'Nishanth Thumbavanam Arun, Nathan Gaw, Praveer Singh, Ken Chang, Katharina Viktoria Hoebel, Jay Patel, Mishka Gidwani, Jayashree Kalpathy-Cramer',
        openreview='https://openreview.net/forum?id=02X3kfP6W4',
        id='S107',
        paper='papers/arun20.html',
        abstract='Saliency maps have become a widely used method to assess which areas of the input image are most pertinent to the prediction of a trained neural network.  However, in the context of medical imaging, there is no study to our knowledge that has examined the efficacy of these techniques and quantified them using overlap with ground truth bounding boxes. In this work, we explored the credibility of the various existing saliency map methods on the RSNA  Pneumonia  dataset. We  found  that  GradCAM  was  the  most  sensitive  to  model parameter and label randomization, and was highly agnostic to model architecture.')
}}
{{ paper('Automated MRI based pipeline for glioma segmentation and prediction of grade, IDH mutation and 1p19q co-deletion',
        'Milan Decuyper, Stijn Bonte, Karel Deblaere, Roel Van Holen',
        openreview='https://openreview.net/forum?id=J5iep2t90F',
        id='S116',
        paper='papers/decuyper20.html',
        abstract='In the WHO glioma classification guidelines grade, IDH mutation and 1p19q co-deletion play a central role as they are important markers for prognosis and optimal therapy planning. Therefore, we propose a fully automatic, MRI based, 3D pipeline for glioma segmentation and classification. The designed segmentation network was a 3D U-Net achieving an average whole tumor dice score of 90%. After segmentation, the 3D tumor ROI is extracted and fed into the multi-task classification network. The network was trained and evaluated on a large heterogeneous dataset of 628 patients, collected from The Cancer Imaging Archive and BraTS 2019 databases. Additionally, the network was validated on an independent dataset of 110 patients retrospectively acquired at the Ghent University Hospital (GUH). Classification AUC scores are 0.93, 0.94 and 0.82 on the TCIA test data and 0.94, 0.86 and 0.87 on the GUH data for grade, IDH and 1p19q status respectively. ')
}}
{{ paper('Automatic segmentation of stroke lesions in non-contrast computed tomography with convolutional neural networks',
        'Anup Tuladhar, Serena Schimert, Deepthi Rajashekar, Helge C. Kniep, Jens Fiehler, Nils D. Forkert',
        openreview='https://openreview.net/forum?id=ehpiBRHu07',
        id='S161',
        paper='papers/tuladhar20.html',
        abstract='Manual lesion segmentation for non-contrast computed tomography (NCCT), a common modality for volumetric follow-up assessment of ischemic strokes, is time-consuming and subject to high inter-observer variability. Our approach uses a combination of a 3D convolutional neural network (CNN) combined with post-processing methods. A total of 272 multi-center clinical NCCT datasets were used: 204 for CNN training, 48 for validation and developing post-processing methods, and 20 for testing. The testing datasets were from centers that did not contribute to the training and validation sets, and were segmented by two neuroradiologists. We achieved a median Dice score of 0.63, which was significantly improved to 0.66 with post-processing. The automatically segmented lesion volumes were not significantly different from the lesion volumes determined by the two manual observers. As the model was trained on datasets from multiple centers, it is broadly applicable. ')
}}
{{ paper('Automatic segmentation of the pulmonary lobes with a 3D u-net and optimized loss function',
        'Bianca Lassen-Schmidt, Alessa Hering, Stefan Krass, Hans Meine',
        openreview='https://openreview.net/forum?id=AkziGgmwl',
        id='S014',
        paper='papers/lassen-schmidt20.html',
        abstract='Fully-automatic lung lobe segmentation is challenging due to anatomical variations, pathologies, and incomplete fissures. We trained a 3D u-net for pulmonary lobe segmentation on 49 mainly publically available datasets and introduced a weighted Dice loss function to emphasize the lobar boundaries. To validate the performance of the proposed method we compared the results to two other methods. The new loss function improved the mean distance to 1.46 mm (compared to 2.08 mm for simple loss function without weighting).')
}}
{{ paper('Bayesian Generative Models for Knowledge Transfer in MRI Semantic Segmentation Problems',
        'Anna Kuzina, Evgenii Egorov, Evgeny Burnaev',
        openreview='https://openreview.net/forum?id=3i6X1618wi',
        id='S256',
        paper='papers/kuzina20.html',
        abstract='Automatic segmentation methods based on deep learning have recently demonstrated state-of-the-art performance, outperforming the ordinary methods. Nevertheless, these methods are inapplicable for small datasets, which are very common in medical problems. To this end, we propose a knowledge transfer method between diseases via the Generative Bayesian Prior network. Our approach is compared to a pre-train approach and random initialization and obtains the best results in terms of Dice Similarity Coefficient metric for the small subsets of the Brain Tumor Segmentation 2018 database (BRATS2018).')
}}
{{ paper('Classification of Epithelial Ovarian Carcinoma Whole-Slide Pathology Images Using Deep Transfer Learning',
        'Yiping Wang, David Farnell, Hossein Farahani, Mitchell Nursey, Basile Tessier-Cloutier, Steven J.M. Jones, David G. Huntsman, C. Blake Gilks, Ali Bashashati',
        openreview='https://openreview.net/forum?id=VXdQD8B307',
        id='S104',
        paper='papers/wang20.html',
        abstract="Ovarian cancer is the most lethal cancer of the female reproductive organs. There are $5$ major histological subtypes of epithelial ovarian cancer, each with distinct morphological, genetic, and clinical features. Currently, these histotypes are determined by a pathologist\\'s microscopic examination of tumor whole-slide images (WSI). This process has been hampered by poor inter-observer agreement (Cohen’s kappa $0.54$-$0.67$). We utilized a two-stage deep transfer learning algorithm based on convolutional neural networks (CNN) and progressive resizing for automatic classification of epithelial ovarian carcinoma WSIs. The proposed algorithm achieved a mean accuracy of $87.54\\%$ and Cohen\\'s kappa of $0.8106$ in the slide-level classification of $305$ WSIs; performing better than a standard CNN and pathologists without gynecology-specific training. ")
}}
{{ paper('Data-Driven Prediction of Embryo Implantation Probability Using IVF Time-lapse Imaging',
        'David H. Silver, Martin Feder, Yael Gold-Zamir, Avital L. Polsky, Shahar Rosentraub, Efrat Shachor, Adi Weinberger, Pavlo Mazur, Valery D. Zukin, Alex M. Bronstein',
        openreview='https://openreview.net/forum?id=TujK1uTkTP',
        id='S126',
        paper='papers/silver20.html',
        abstract='The process of fertilizing a human egg outside the body in order to help those suffering from infertility to conceive is known as in vitro fertilization (IVF). Despite being the most effective method of assisted reproductive technology (ART), the average success rate of IVF is a mere 20-40%. One step that is critical to the success of the procedure is selecting which embryo to transfer to the patient, a process typically conducted manually and without any universally accepted and standardized criteria. In this paper we describe a novel data-driven system trained to directly predict embryo implantation probability from embryogenesis time-lapse imaging videos. Using  retrospectively collected videos from 272 embryos, we demonstrate that, when compared to an external panel of embryologists, our algorithm results in a 12% increase of positive predictive value and a 29% increase of negative predictive value. ')
}}
{{ paper('Deblurring for spiral real-time MRI using convolutional neural networks',
        'Yongwan Lim, Shrikanth Narayanan, Krishna Nayak',
        openreview='https://openreview.net/forum?id=zYareJYs8Z',
        id='S047',
        paper='papers/lim20.html',
        abstract='Spiral acquisitions are preferred in real-time MRI because of their time efficiency. A fundamental limitation of spirals is image blurring due to off-resonance, which degrades image quality significantly at air-tissue boundaries. Here, we demonstrate a simple CNN-based deblurring method for spiral real-time MRI of human speech production. We show the CNN-based deblurring is capable of restoring blurred vocal tract tissue boundaries, without a need for exam-specific field maps. Deblurring performance is superior to a current auto-calibrated method, and slightly inferior to ideal reconstruction with perfect knowledge of the field maps. ')
}}
{{ paper('Deep learning approach to describing and classifying fungi microscopic images',
        'Bartosz Zieliński, Agnieszka Sroka-Oleksiak, Dawid Rymarczyk, Adam Piekarczyk, Monika Brzychczy-Włoch',
        openreview='https://openreview.net/forum?id=AEhp_Cqq-h',
        id='S053',
        paper='papers/zieliński20.html',
        abstract='Preliminary diagnosis of fungal infections can rely on microscopic examination. However, in many cases, it does not allow unambiguous identification of the species due to their visual similarity. Therefore, it is usually necessary to use additional biochemical tests. That involves additional costs and extends the identification process up to 10 days. Such a delay in the implementation of targeted therapy may be grave in consequence as the mortality rate for immunosuppressed patients is high. In this paper, we apply a machine learning approach based on deep neural networks and bag-of-words to classify microscopic images of various fungi species. Our approach makes the last stage of biochemical identification redundant, shortening the identification process by 2-3 days, and reducing the cost of the diagnosis.')
}}
{{ paper('DeepRetinotopy: Predicting the Functional Organization of Human Visual Cortex from Structural MRI Data using Geometric Deep Learning',
        'Fernanda L. Ribeiro, Steffen Bollmann, Alexander M. Puckett',
        openreview='https://openreview.net/forum?id=Nw_trRFjPE',
        id='S073',
        paper='papers/ribeiro20.html',
        abstract='Whether it be in a man-made machine or a biological system, form and function are often directly related. In the latter, however, this particular relationship is often unclear due to the intricate nature of biology. Here we developed a geometric deep learning model capable of exploiting the actual structure of the cortex to learn the complex relationship between brain function and anatomy from structural and functional MRI data. Our model was not only able to predict the functional organization of human visual cortex from anatomical properties alone, but it was also able to predict nuanced variations across individuals.')
}}
{{ paper('Enhancing Foreground Boundaries for Medical Image Segmentation',
        'Dong Yang, Holger Roth, Xiaosong Wang, Ziyue Xu, Andriy Myronenko, Daguang Xu',
        openreview='https://openreview.net/forum?id=PAlQnIVKLY',
        id='S278',
        paper='papers/yang20.html',
        abstract='Object segmentation plays an important role in the modern medical image analysis, which benefits clinical study, disease diagnosis, and surgery planning. Given the various modalities of medical images, the automated or semi-automated segmentation approaches have been used to identify and parse organs, bones, tumors, and other regions-of-interest (ROI). However, these contemporary segmentation approaches tend to fail to predict the boundary areas of ROI, because of the fuzzy appearance contrast caused during the imaging procedure. To further improve the segmentation quality of boundary areas, we propose a boundary enhancement loss to enforce additional constraints on optimizing machine learning models. The proposed loss function is light-weighted and easy to implement without any pre- or post-processing. Our experimental results validate that our loss function are better than, or at least comparable to, other state-of-the-art loss functions in terms of segmentation accuracy.')
}}
{{ paper('Functional Space Variational Inference for Uncertainty Estimation in Computer Aided Diagnosis',
        'Pranav Poduval, Hrushikesh Loya, Amit Sethi',
        openreview='https://openreview.net/forum?id=eLL-c_Xc0B',
        id='S310',
        paper='papers/poduval20.html',
        abstract='Deep neural networks have revolutionized medical image analysis and disease diagnosis. Despite their impressive performance, it is diﬃcult to generate well-calibrated probabilistic outputs for such networks, which makes them uninterpretable black boxes. Bayesian neural networks provide a principled approach for modelling uncertainty and increasing patient safety, but they have a large computational overhead and provide limited improvement in calibration. In this work, by taking skin lesion classiﬁcation as an example task, we show that by shifting Bayesian inference to the functional space we can craft meaningful priors that give better-calibrated uncertainty estimates at a much lower computational cost')
}}
{{ paper('Image Translation by Latent Union of Subspaces for Cross-Domain Plaque Segmentation',
        'Yingying Zhu, Daniel C. Elton, Sungwon Lee, Perry J. Pickhardt, Ronald M. Summers',
        openreview='https://openreview.net/forum?id=qJxBTPyVYA',
        id='S266',
        paper='papers/zhu20.html',
        abstract='Calcified plaque in the aorta and pelvic arteries is associated with coronary artery calcification and is a strong predictor of heart attack. Current calcified plaque detection models show poor generalizeability to different domains (ie. pre-contrast vs. post-contrast CT scans). Many recent works have shown how cross domain object detection can be improved using an image translation model which translates between domains using a single shared latent space. However, while current image translation models do a good job preserving global/intermediate level structures they often have trouble preserving tiny structures. In medical imaging applications, preserving small structures is important since these structures can carry information which is highly relevant for disease diagnosis. Recent works on image reconstruction show that complex real-world images are better reconstructed using a union of subspaces approach. Since small image patches are used to train the image translation model, it makes sense to enforce that each patch be represented by a linear combination of subspaces which may correspond to the different parts of the body present in that patch. Motivated by this, we propose an image translation network using a shared union of subspaces constraint and show our approach preserves subtle structures (plaques) better than the conventional method. We further applied our method to a cross domain plaque detection task and show significant improvement compared to the state-of-the art method.')
}}
{{ paper('Improving Mammography Malignancy Segmentation by Designing the Training Process',
        'Mickael Tardy, Diana Mateus',
        openreview='https://openreview.net/forum?id=vVsWe9-s0G',
        id='S137',
        paper='papers/tardy20.html',
        abstract='We work on the breast imaging malignancy segmentation task while focusing on the train- ing process instead of network complexity. We designed a training process based on a modified U-Net, increasing the overall segmentation performances by using both, benign and malignant data for training. Our approach makes use of only a small amount of anno- tated data and relies on transfer learning from a self-supervised reconstruction task, and favors explainability.')
}}
{{ paper('Interpreting Chest X-rays via CNNs that Exploit Hierarchical Disease Dependencies and Uncertainty Labels',
        'Hieu H. Pham, Tung T. Le, Dat T. Ngo, Dat Q. Tran, Ha Q. Nguyen',
        openreview='https://openreview.net/forum?id=4o1GLIIHlh',
        id='S023',
        paper='papers/pham20.html',
        abstract='We present a new approach based on deep convolutional neural networks (CNNs) for predicting the presence of 14 common thoracic diseases and observations. A strong set of CNNs are trained on over 200,000 chest X-ray images provided by CheXpert - a large scale chest X-ray dataset. In particular, dependencies among abnormality labels and uncertain samples are fully exploited during the training and inference stages. Experiments indicate that the proposed method achieves a mean area under the curve (AUC) of 0.940 in predicting 5 selected pathologies. To the best of our knowledge, this is the highest AUC score yet reported on this dataset to date. Additionally, the proposed method is also evaluated on the independent test set of the CheXpert competition and reports a performance level comparable to practicing radiologists. Our obtained result ranks first on the CheXpert leaderboard at the time of writing this paper.')
}}
{{ paper('Joint Liver Lesion Segmentation and Classification via Transfer Learning',
        'Michal Heker, Hayit Greenspan',
        openreview='https://openreview.net/forum?id=8gSjgXg5U',
        id='S322',
        paper='papers/heker20.html',
        abstract="Transfer learning and joint learning approaches are extensively used to improve the performance of Convolutional Neural Networks (CNNs). In medical imaging applications in which the target dataset is typically very small, transfer learning improves feature learning while joint learning has shown effectiveness in improving the network\\'s generalization and robustness. In this work, we study the combination of these two approaches for the problem of liver lesion segmentation and classification.      For this purpose, 332 abdominal CT slices containing lesion segmentation and classification of three lesion types are evaluated. For feature learning, the dataset of MICCAI 2017 Liver Tumor Segmentation (LiTS) Challenge is used.      Joint learning shows improvement in both segmentation and classification results.      We show that a simple joint framework outperforms the commonly used multi-task architecture (Y-Net), achieving an improvement of 10% in classification accuracy, compared to 3% improvement with Y-Net.")
}}
{{ paper('Learning to map between ferns with differentiable binary embedding networks',
        'Max Blendowski, Mattias P. Heinrich',
        openreview='https://openreview.net/forum?id=EiT7GQAj-T',
        id='S133',
        paper='papers/blendowski20.html',
        abstract="Current deep learning methods are based on the repeated, expensive application of convolutions with parameter-intensive weight matrices. In this work, we present a novel concept that enables the application of differentiable random ferns in end-to-end networks. It can then be used as multiplication-free convolutional layer alternative in deep network architectures. Our experiments on the binary classification task of the TUPAC\\'16 challenge demonstrate improved results over the state-of-the-art binary XNOR net and only slightly worse performance than its 2x more parameter intensive floating point CNN counterpart. ")
}}
{{ paper('Low-dose CT Enhancement Network with a Perceptual Loss Function in the Spatial Frequency and Image Domains',
        'Kevin J. Chung, Roberto Souza, Richard Frayne, Ting-Yim Lee',
        openreview='https://openreview.net/forum?id=rw5BswbvMB',
        id='S059',
        paper='papers/chung20.html',
        abstract='We propose a dual-domain cascade of U-nets (i.e. a W-net\\") operating in both the spatial frequency and image domains to enhance low-dose CT (LDCT) images without the need for proprietary x-ray projection data. The central slice theorem motivated the use of the spatial frequency domain in place of the raw sinogram. Data were obtained from the AAPM Low-dose Grand Challenge. A combination of Fourier space (F) and/or image domain (I) U-nets and W-nets were trained with a multi-scale structural similarity and mean absolute error loss function to denoise filtered back projected (FBP) LDCT images while maintaining perceptual features important for diagnostic accuracy. Deep learning enhancements were superior to FBP LDCT images in quantitative and qualitative performance with the dual-domain W-nets outperforming single-domain U-net cascades. Our results suggest that spatial frequency learning in conjunction with image-domain processing can produce superior LDCT enhancement than image-domain-only networks. ')
}}
{{ paper('Medical Image Segmentation via Unsupervised Convolutional Neural Network',
        'Junyu Chen, Eric C. Frey',
        openreview='https://openreview.net/forum?id=XrbnSCv4LU',
        id='S038',
        paper='papers/chen20.html',
        abstract='For the majority of the learning-based segmentation methods, a large quantity of high-quality training data is required. In this paper, we present a novel learning-based segmentation model that could be trained semi- or un- supervised. Specifically, in the unsupervised setting, we parameterize the Active contour without edges (ACWE) framework via a convolutional neural network (ConvNet), and optimize the parameters of the ConvNet using a self-supervised method. In another setting (semi-supervised), the auxiliary segmentation ground truth is used during training. We show that the method provides fast and high-quality bone segmentation in the context of single-photon emission computed tomography (SPECT) image.')
}}
{{ paper('Multiple resolution residual network for automatic thoracic organs-at-risk segmentation from CT',
        'Hyemin Um, Jue Jiang, Maria Thor, Andreas Rimner, Leo Luo, Joseph O. Deasy, Harini Veeraraghavan',
        openreview='https://openreview.net/forum?id=h3Miqa_jqN',
        id='S308',
        paper='papers/um20.html',
        abstract='We implemented and evaluated a multiple resolution residual network (MRRN) for multiple normal organs-at-risk (OAR) segmentation from computed tomography (CT) images for thoracic radiotherapy treatment (RT) planning. Our approach simultaneously combines feature streams computed at multiple image resolutions and feature levels through residual connections. The feature streams at each level are updated as the images are passed through various feature levels. We trained our approach using 206 thoracic CT scans of lung cancer patients with 35 scans held out for validation to segment the left and right lungs, heart, esophagus, and spinal cord. This approach was tested on the 60 CT scans from the open-source AAPM Thoracic Auto-Segmentation Challenge dataset. Performance was measured using the Dice Similarity Coefficient (DSC). Our approach outperformed the best-performing method in the grand challenge for hard-to-segment structures like the esophagus and achieved comparable results for all other structures. Median DSC using our method was 0.97 (interquartile range [IQR]: 0.97-0.98) for the left and right lungs, 0.93 (IQR: 0.93-0.95) for the heart, 0.78 (IQR: 0.76-0.80) for the esophagus, and 0.88 (IQR: 0.86-0.89) for the spinal cord. ')
}}
{{ paper('On the effectiveness of GAN generated cardiac MRIs for segmentation',
        'Youssef Skandarani, Nathan Painchaud, Pierre-Marc Jodoin, Alain Lalande',
        openreview='https://openreview.net/forum?id=f9Pl3Qj3_Q',
        id='S118',
        paper='papers/skandarani20.html',
        abstract='In this work, we propose a Variational Autoencoder (VAE) - Generative Adversarial Networks (GAN) model that can produce highly realistic MRI together with its pixel accurate groundtruth for the application of cine-MR image cardiac segmentation.  On one side of our model is a Variational Autoencoder (VAE) trained to learn the latent representations of cardiac shapes.  On the other side is a GAN that uses  ”SPatially-Adaptive (DE)Normalization” (SPADE) modules to generate realistic MR images tailored to a given anatomical map.  At test time, the sampling of the VAE latent space allows to generate an arbitrary large number of cardiac shapes, which are fed to the GAN that subsequently generates MR images whose cardiac structure fits that of the cardiac shapes.  In other words, our system can generate a large volume of realistic yet labeled cardiac MR images.  We show that segmentation with CNNs trained with our synthetic annotated images gets competitive results compared to traditional techniques.      We also show that combining data augmentation with our GAN-generated images lead to an improvement in the Dice score of up to 12 percent while allowing for better generalization capabilities on  other datasets.')
}}
{{ paper('Overview of Scanner Invariant Representations',
        'Daniel Moyer, Greg ver Steeg, Paul M. Thompson',
        openreview='https://openreview.net/forum?id=yqm9RD_XHT',
        id='S288',
        paper='papers/moyer20.html',
        abstract='Pooled imaging data from multiple sources is subject to bias from each source. Studies that do not correct for these scanner/site biases at best lose statistical power, and at worst leave spurious correlations in their data. Estimation of the bias effects is non-trivial due to the paucity of data with correspondence across sites, so called \\"traveling phantom\\" data, which is expensive to collect. Nevertheless, numerous solutions leveraging direct correspondence have been proposed. In contrast to this, Moyer et al. (2019) proposes an unsupervised solution using invariant representations, one which does not require correspondence and thus does not require paired images. By leveraging the data processing inequality, an invariant representation can then be used to create an image reconstruction that is uninformative of its original source, yet still faithful to the underlying structure. In the present abstract we provide an overview of this method.')
}}
{{ paper('Pulmonary Nodule Malignancy Classification Using its Temporal Evolution with Two-Stream 3D Convolutional Neural Networks',
        'Xavier Rafael-Palou, Anton Aubanell, Ilaria Bonavita, Mario Ceresa, Gemma Piella, Vicent Ribas, Miguel Ángel González Ballester',
        openreview='https://openreview.net/forum?id=D1jTt_FOPY',
        id='S094',
        paper='papers/rafael-palou20.html',
        abstract='Nodule malignancy assessment is a complex, time-consuming and error-prone task.  Current clinical practice requires measuring changes in size and density of the nodule at different time-points.  State of the art solutions rely on 3D convolutional neural networks built on pulmonary nodules obtained from a single CT scan per patient.  In this work, we propose a two-stream 3D convolutional neural network that predicts malignancy by jointly analyzing two pulmonary nodule volumes from the same patient taken at different time-points.  Best results achieve 77% of F1-score in test with an increment of 9% and 12% of F1-score with respect to the same network trained with images from a single time-point.')
}}
{{ paper('Robust Image Segmentation Quality Assessment',
        'Leixin Zhou, Wenxiang Deng, Xiaodong Wu',
        openreview='https://openreview.net/forum?id=nyhZXiaotm',
        id='S093',
        paper='papers/zhou20.html',
        abstract='Deep learning based image segmentation methods have achieved great success, even having human-level accuracy in some applications. However, due to the black box nature of deep learning, the best method may fail in some situations. Thus predicting segmentation quality without ground truth would be very crucial especially in clinical practice. Recently, people proposed to train neural networks to estimate the quality score by regression. Although it can achieve promising prediction accuracy, the network suffers robustness problem, e.g. it is vulnerable to adversarial attacks. In this paper, we propose to alleviate this problem by utilizing the difference between the input image and the reconstructed image, which is conditioned on the segmentation to be assessed, to lower the chance to overfit to the undesired image features  from the original input image, and thus to increase the robustness. Results on ACDC17 dataset demonstrated our method is promising.')
}}
{{ paper('Segmentation of the Myocardium on Late-Gadolinium Enhanced MRI based on 2.5 D Residual Squeeze and Excitation Deep Learning Model',
        'Abdul Qayyum, Alain Lalande, Thomas Decourselle, Thibaut Pommier, Alexandre Cochet, Fabrice Meriaudeau',
        openreview='https://openreview.net/forum?id=4v2lR3Zvsw',
        id='S135',
        paper='papers/qayyum20.html',
        abstract='Cardiac left ventricular (LV) segmentation from short-axis MRI acquired 10 minutes after the injection of a contrast agent (LGE-MRI) is a necessary step in the processing allowing the identification and diagnosis of cardiac diseases such as myocardial infarction. However, this segmentation is challenging due to high variability across subjects and the potential lack of contrast between structures. Then, the main objective of this work is to develop an accurate automatic segmentation method based on deep learning models for the myocardial borders on LGE-MRI. To this end, 2.5 D residual neural network integrated with a squeeze and excitation blocks in encoder side with specialized convolutional has been proposed. Late fusion has been used to merge the output of the best trained proposed models from a different set of hyperparameters. A total number of 320 exams (with a mean number of 6 slices per exam) were used for training and 28 exams used for testing. The performance analysis of the proposed ensemble model in the basal and middle slices was similar as compared to intra-observer study and slightly lower at apical slices. The overall Dice score was 82.01% by our proposed method as compared to Dice score of 83.22% obtained from the intra observer study. The proposed model could be used for the automatic segmentation of myocardial border that is a very important step for accurate quantification of no-reflow, myocardial infarction, myocarditis, and hypertrophic cardiomyopathy, among others.')
}}
{{ paper('Spatiotemporal motion prediction in free-breathing liver scans via a recurrent multi-scale encoder decoder',
        'Liset Vazquez Romaguera, Rosalie Plantefeve, Samuel Kadoury',
        openreview='https://openreview.net/forum?id=901HZmWDHH',
        id='S057',
        paper='papers/romaguera20.html',
        abstract='In this work we propose a multi-scale recurrent encoder-decoder architecture to predict the breathing induced organ deformation in future frames. The model was trained end-to-end from input images to predict a sequence of motion labels. Targets were created by quantizing the motion fields obtained from deformable image registration. We propose a multi-scale feature extraction scheme in the spatial encoder which processes the input at different resolutions. We report results using MRI free-breathing acquisitions from 12 volunteers. Experiments were aimed at investigating the proposed multi-scale design and the effect of increasing the number of predicted frames on the overall accuracy of the model. The proposed model was able to predict vessel positions in the next temporal image with a mean accuracy of 2.03 (2.89) mm showing increased performance in comparison with state-of-the-art approaches.')
}}
{{ paper('Tackling the Problem of Large Deformations in Deep Learning Based Medical Image Registration Using Displacement Embeddings',
        'Lasse Hansen, Mattias P. Heinrich',
        openreview='https://openreview.net/forum?id=kPBUZluVq',
        id='S155',
        paper='papers/hansen20.html',
        abstract='Though, deep learning based medical image registration is currently starting to show promising advances, often, it still fells behind conventional frameworks in terms of reg- istration accuracy. This is especially true for applications where large deformations exist, such as registration of interpatient abdominal MRI or inhale-to-exhale CT lung registra- tion. Most current works use U-Net-like architectures to predict dense displacement fields from the input images in different supervised and unsupervised settings. We believe that the U-Net architecture itself to some level limits the ability to predict large deformations (even when using multilevel strategies) and therefore propose a novel approach, where the input images are mapped into a displacement space and final registrations are reconstructed from this embedding. Experiments on inhale-to-exhale CT lung registration demonstrate the ability of our architecture to predict large deformations in a single forward path through our network (leading to errors below 2 mm).')
}}
{{ paper('Tractometry-based Anomaly Detection for Single-subject White Matter Analysis',
        'Maxime Chamberland, Sila Genc, Erika P. Raven, Greg D. Parker, Adam Cunningham, Joanne Doherty, Marianne van den Bree, Chantal M. W. Tax, Derek K. Jones',
        openreview='https://openreview.net/forum?id=heX-Rk0TE0',
        id='S027',
        paper='papers/chamberland20.html',
        abstract='There is an urgent need for a paradigm shift from group-wise comparisons to individual diagnosis in diffusion MRI (dMRI) to enable the analysis of rare cases and clinically-heterogeneous groups. Deep autoencoders have shown great potential to detect anomalies in neuroimaging data. We present a framework that operates on the manifold of white matter (WM) pathways to learn normative microstructural features, and discriminate those at genetic risk from controls in a paediatric population. ')
}}
{{ paper('Uncertainty Evaluation Metrics for Brain Tumour Segmentation',
        'Raghav Mehta, Angelos Filos, Yarin Gal, Tal Arbel',
        openreview='https://openreview.net/forum?id=H-PvDNIex',
        id='S282',
        paper='papers/mehta20.html',
        abstract='In this paper, we describe and explore the metric that was designed to assess and rank uncertainty measures for the task of brain tumour sub-tissue segmentation in the BraTS 2019 sub-challenge on uncertainty quantification. The metric is designed to (1) reward uncertainty measures where high confidence is assigned to correct assertions, and where incorrect assertions are assigned low confidence and (2) penalize measures that have higher percentages of under-confident correct assertions.  Here, the workings of the metrics explored based on a number of popular uncertainty measures evaluated on the BraTS2019 dataset')
}}
{{ paper('Unsupervised learning of multimodal image registration using domain adaptation with projected Earth Mover’s discrepancies',
        'Mattias P Heinrich, Lasse Hansen',
        openreview='https://openreview.net/forum?id=wbZM-DcJB9',
        id='S131',
        paper='papers/heinrich20.html',
        abstract='Multimodal image registration is a very challenging problem for deep learning approaches. Most current work focuses on either supervised learning that requires labelled training scans and may yield models that bias towards annotated structures or unsupervised approaches that are based on hand-crafted similarity metrics and may therefore not outperform their classical non-trained counterparts. We believe that unsupervised domain adaptation can be beneficial in overcoming the current limitations for multimodal registration, where good metrics are hard to define.      Domain adaptation has so far been mainly limited to classification problems. We propose the first use of unsupervised domain adaptation for discrete multimodal registration. Based on a source domain for which quantised displacement labels are available as supervision, we transfer the output distribution of the network to better resemble the target domain (other modality) using classifier discrepancies. To improve upon the sliced Wasserstein metric for 2D histograms, we present a novel approximation that projects predictions into 1D and computes the L1 distance of their cumulative sums. Our proof-of-concept demonstrates the applicability of domain transfer from mono- to multimodal 2D registration of canine MRI scans and improves the registration accuracy from 33% (using sliced Wasserstein) to 44%.')
}}
{{ paper('Using Generative Models for Pediatric wbMRI',
        'Alex Chang, Vinith M. Suriyakumar, Abhishek Moturu, Nipaporn Tewattanarat, Andrea Doria, Anna Goldenberg',
        openreview='https://openreview.net/forum?id=BXC_fpbLe',
        id='S312',
        paper='papers/chang20.html',
        abstract='Early detection of cancer is key to a good prognosis and requires frequent testing, especially in pediatrics. Whole-body magnetic resonance imaging (wbMRI) is an essential part of several well-established screening protocols with screening starting in early childhood. To date, machine learning (ML) has been used on wbMRI images to stage adult cancer patients. It is not possible to use such tools in pediatrics due to the changing bone signal throughout growth, the difficulty of obtaining these images in young children due to movement and limited compliance, and the rarity of positive cases. We evaluate the quality of wbMRI images generated using generative adversarial networks (GANs) trained on wbMRI data from a pediatric hospital. We use the Fréchet Inception Distance (FID) metric, Domain Fréchet Distance (DFD), and blind tests with a radiology fellow for evaluation. We demonstrate that StyleGAN2 provides the best performance in generating wbMRI images with respect to all three metrics.')
}}
{{ paper('Vispi: Automatic Visual Perception and Interpretation of Chest X-rays',
        'Xin Li, Rui Cao, Dongxiao Zhu',
        openreview='https://openreview.net/forum?id=otswIbmgYA',
        id='S276',
        paper='papers/li20.html',
        abstract='Computer-aided medical image visual perception and interpretation with deep learning remain a challenging task, due to the lack of high-quality annotated image-report pairs and tailor-made generative models for sufficient extraction and exploitation of localized semantic features associated with abnormalities. To tackle these challenges, we present Vispi, an automatic medical image interpretation system, which first annotates an image via classifying and localizing common thoracic diseases with visual support and then followed by report generation from an attentive LSTM model. Analyzing an open IU X-ray dataset, we demonstrate a superior performance of Vispi in disease classification, localization and report generation using automatic performance evaluation metrics ROUGE and CIDEr.')
}}
[% / %]