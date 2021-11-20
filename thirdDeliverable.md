# Introduction

In this part of the project, the BiSeNet(Bilateral Segmentation Network) was run on 31,706 caucasian males images to obtain mask for seven key parts of the face. The parts of the face used were : eyes, nose, eye brows, eyes with brows, mouth region(including lips), hair and only skin (excluding key features like nose, eyes,etc). Using the mask obtained for these parts, the blurring was done for the respective part. The core idea behind the blurring is that while extracting features of the face using deep-learning based method, ArcFace in this case of project, these parts will be ignored. So, out of these seven candidate parts, the one that causes highest shift in impostor score distribution will most likely be the most important feature that is important in recognition. 

# Segmentation Network Choice

Out of several face pre-trained face segmentation network available, BiSeNet was selected for reason listed as follows:

1) Face segmentation results(mean IOU) obtained from BiSeNet is very close to SOTA segmentation network
2) The network is publicly available to use 
3) The segmentation is comparatively faster ~ 4-8 iterations/sec

# Feature Extractor Choice

Out of several face pre-trained face segmentation network available, ArcFace was selected for reason listed as follows:

1) ArcFace is considered to be SOTA the task of feature extraction, for several benchmark datasets
2) ArcFace directly optimises the geodesic distance margin by virtue of the exact correspondence between the angle and arc in the normalised hypersphere. This causes increase it inter-class distance to increase and intra-class distance to decrease, eventually increasing the accuracy of the representation of images in feature space
3) ArcFace is very easy to implement and computationally fast as well.




# Blurring Operation

The blurring operation was done using the mask obtained from BiSeNet. It is well known in deep learning community that the sharp gradient can deteriorate the performance of these neural network, most probably because of treating these sharp gradient as an additional feature. In order to avoid, such sharp gradient in the boundaries where blurring mask is applied, gaussian filtering was applied to the mask before applying it to the face. Additionally, to make this blending even more smoother, dilation was performed on the mask obtained from BiSeNet. The rate of dilation applied was inversely propotional to the size of the part. For eg: since, eyes are comparatively smaller than nose - a larger dilation was applied on eyes to obtain smoother gradient blending in the boundary regions. Some of the sample This [jupyter kernel](/blurring_operation_demo.ipynb), included in this github repo, shows the sample of hand-crafted dilated kernel selection for different parts and demo displays of mask, dilated mask, gaussian blurred dilated mask, and image with blurred part.

# Sample Blurs for Caucasian Male

This section shows sample blurring on one of the male images. Similar such blurring operations were applied on 31,706 images of Caucasian males to report the results presented in this part of the project. 

| Blurred Eye | Blurred Brows | Blurred Eye w/ Brows |
| --- | --- | --- |
| <img src="/Plots/eyes.JPG" width="300"/> | <img src="/Plots/brows.JPG" width="300"/> | <img src="/Plots/eyeswbrows.JPG" width="300"/> |

| Blurred Mouth w/ Lips | Blurred Nose | Blurred Hair |
| --- | --- | --- |
| <img src="/Plots/mouthwlips.JPG" width="300"/>| <img src="/Plots/nose.JPG" width="300"/>| <img src="/Plots/hair.JPG" width="300"/> |

| Blurred Skin | 
| --- |
| <img src="/Plots/skin.JPG" width="300"/>| 

# Results 

After the images with blurred parts were obtained for the caucasian male dataset, the face-feature vector representation were obtained using ArcFace. The cosine similarity scores between genuine and impostor pairs were calculated. The impostor and genuine distribution plots were obtained using these similarity scores for each parts blurred. The results are shown below:

| Blurred Eye | Blurred Brows | Blurred Eye w/ Brows |
| --- | --- | --- |
| <img src="/Plots/results/blurredeyes.png" width="400"/> | <img src="/Plots/results/blurredbrows.png" width="400"/> | <img src="/Plots/results/blurredeyeswbrows.png" width="400"/> |

| Blurred Mouth w/ Lips | Blurred Nose | Blurred Hair |
| --- | --- | --- |
| <img src="/Plots/results/blurredlips.png" width="400"/>| <img src="/Plots/results/blurrednose.png" width="400"/>| <img src="/Plots/results/blurredhair.png" width="400"/> |

| Blurred Skin | 
| --- |
| <img src="/Plots/results/blurredskin.png" width="300"/>| 

# Interpretation

The general interpretation(not part specific) interpretation from the all of the plots shown above is that the blurring operation doesn't affect similarity score between two genuine pairs. It is most likely because the blurring operation is consistent across all genuine pairs and even after blurring they are more or like same. The blurring affects the impostor comparison because blurring essentially takes away additional feature to compare impostor pairs with and this causes increas in false match rate.<br><br>

Since, genuine distribution for images with blurred parts are more or like same to the original images, the new obtained d-prime scores for impostor distribution can be used as a metric to decide what part is most important in face recognition.**Regarding the part specific genuine and impostor comparison, from all the figures shown above - eyes with eyesbrows seems to be the most important region and mouth with lips regions seems to be least important region to distinguish between two impostor pairs.** The detailed analysis and comparison for all the parts across different ethnic groups will be provided in the final report.

# Final Report Task

For the final report, the following listed results will be included in the report:

1) Genuine and Impostor plots for Caucasian Female, African-American Males and African-American Females. The goal here is to see if certain patterns holds. For eg: Is eyes with brows most important region for recognition across all ethnic groups?<br>
2) Detailed analysis and comparison of the d-prime statistics for comparison between several parts and ethnic groups.
