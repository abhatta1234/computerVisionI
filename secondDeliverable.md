# Introduction

Facial recognition accuracy differs across racial groups. The main goal of this project is to figure out if any particular part of the face is driving the accuracy difference and if, so what part ? To perform the experiments, the MORPH dataset published by UNC-Wilimington is used. There is no preprocessing specific to the dataset itself, because the dataset includes mugshot images in the controlled environment. But, a substantial pre-processing steps is required when it comes to the project itself. 
 
The experimental pipeline for this project is:
 - Get a image(pre-processed)
 - Obtain a feature vector vector representation of the image
 - Compare all feature vector representations obtained using a similarity metrics
 - Plot Genuine and Impostor Distribution 


# Image pre-processing

The major pre-processing required here is to blur the specific part of the image and repeat the experimental steps mentioned above repeatedly for each different parts. To blur the specific part, the presented needs to parsed into different parts. To perform semantic segmentation, BiSeNet was used and the paper can be accessed using this [link](https://arxiv.org/abs/1808.00897). The following image is used for the illustration of the segmentation:

![423383_01F31](https://user-images.githubusercontent.com/40056517/137397604-00c45876-fe4e-4f1f-9c31-a0231284014e.JPG) <br ><br >
The result of semantic segmentation on the above image using BiSeNet is shown below:
![BiseNet Result](https://user-images.githubusercontent.com/40056517/137433274-70e43f2d-c2d5-4851-af88-785c75a6a219.png)


![checkAnno](https://user-images.githubusercontent.com/40056517/137429036-c6542d93-8010-4b4e-9281-769397a56ace.png) 




![423383_01F31_color_mask](https://user-images.githubusercontent.com/40056517/137429053-5d781713-d363-4d84-8ba3-1d7bac5f23e5.png)


<img width="566" alt="Screen Shot 2021-10-14 at 10 28 56 PM" src="https://user-images.githubusercontent.com/40056517/137429071-bcb5c40a-162e-4edf-ad84-24bd3f0d635d.png">
