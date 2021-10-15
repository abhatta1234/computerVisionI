# Introduction

Facial recognition accuracy differs across racial groups. The main goal of this project is to figure out if any particular part of the face is driving the accuracy difference and if, so what part ? To perform the experiments, the MORPH dataset published by UNC-Wilimington is used. There is no preprocessing specific to the dataset itself, because the dataset includes mugshot images in the controlled environment. But, a substantial pre-processing steps is required when it comes to the project itself. 
 
The experimental pipeline for this project is:
 - Get a image(pre-processed)
 - Obtain a feature vector vector representation of the image
 - Compare all feature vector representations obtained using a similarity metrics
 - Plot Genuine and Impostor Distribution 


# Image pre-processing and Segmentation

The major pre-processing required here is to blur the specific part of the image and repeat the experimental steps mentioned above repeatedly for each different parts. To blur the specific part, the presented needs to parsed into different parts. To perform semantic segmentation, BiSeNet was used and the paper can be accessed using this [link](https://arxiv.org/abs/1808.00897). The following image is used for the illustration of the segmentation:

<img width="506" alt="Screen Shot 2021-10-15 at 4 03 06 PM" src="https://user-images.githubusercontent.com/40056517/137547027-76901ff1-d575-45a3-8331-186a23b60c0c.png"> <br > <br >

Bilateral Segmentation network, a deep-learning based framework, ingeniously uses a context path and spatial path to parse/annotate different parts of the face. Some of the parts of the face that are parsed are left & right eyes, left & right ears, nose, skin, hair, hat and so on. All the parts that are parsed are displayed using different colors. One of the sample results is shown below:

![BiseNet Result](https://user-images.githubusercontent.com/40056517/137433274-70e43f2d-c2d5-4851-af88-785c75a6a219.png) <br ><br >

Now, for the purpose of illustration - the pixel associated with just nose using the BiSeNet network is shown below:

![423383_01F31_color_mask](https://user-images.githubusercontent.com/40056517/137429053-5d781713-d363-4d84-8ba3-1d7bac5f23e5.png) <br ><br >

Now, the mask needs to be created from this segmentation. To do all, all pixel values labeled as nose are given the value of 255 and all remaining pixels are given the value of 0. The mask created using such operation is shown as follows:

![checkAnno](https://user-images.githubusercontent.com/40056517/137429036-c6542d93-8010-4b4e-9281-769397a56ace.png) <br ><br >

Using the mask above, the blurring operation was applied on the face to obtain just the image of the nose with everything else blurred. The original image, annotation and the blurred image is shown below:

<img width="566" alt="Screen Shot 2021-10-14 at 10 28 56 PM" src="https://user-images.githubusercontent.com/40056517/137429071-bcb5c40a-162e-4edf-ad84-24bd3f0d635d.png">

# Future Steps

For the remaining part of the project, the following steps needs to be taken
- Blur one specific part (eyes, nose, ears, skin, hair, etc) for all images in the dataset
- Use ArcFace model to get the feature vector representation
- Compare the feature vector representation
- Plot genuine and impostor distribution to observe any patter
- Repeat the experiment for another major part
