# Introduction

In this part of the project, the BiSeNet(Bilateral Segmentation Network) was run on 31,706 caucasian males images to obtain mask for seven key parts of the face. The parts of the face used were : eyes, nose, eye brows, eyes with brows, mouth region(including lips), hair and only skin (excluding key features like nose, eyes,etc). Using the mask obtained for these parts, the blurring was done for the respective part. The core idea behind the blurring is that while extracting features of the face using deep-learning based method, ArcFace in this case of project, these parts will be ignored. So, out of these seven candidate parts, the one that causes highest shift in impostor score distribution will most likely be the most important feature that is important in recognition. 

# Segmentation Network Choice

Out of several face pre-trained face segmentation network available, BiSeNet was selected for reason listed as follows:

1) Face segmentation results(mean IOU) obtained from BiSeNet is very close to SOTA segmentation network
2) The network is publicly available to use 
3) The segmentation is comparatively faster ~ 4-8 iterations/sec

# Blurring Operation

The blurring operation was done using the mask obtained from BiSeNet. It is well known in deep learning community that the sharp gradient can deteriorate the performance of these neural network, most probably because of treating these sharp gradient as an additional feature. In order to avoid, such sharp gradient in the boundaries where blurring mask is applied, gaussian filtering was applied to the mask before applying it to the face. Additionally, to make this blending even more smoother, dilation was performed on the mask obtained from BiSeNet. The rate of dilation applied was inversely propotional to the size of the part. For eg: since, eyes are comparatively smaller than nose - a larger dilation was applied on eyes to obtain smoother gradient blending in the boundary regions. **Some of the sample dilations of the mask using hand-crafted kernel and blurring of the part can be seen here.**

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

After the images with blurred parts were obtained for the caucasian male dataset, the face-feature vector representation were obtained using ArcFace. The cosine similarity scores between genuine and impostor pairs were calculated 

| Blurred Eye | Blurred Brows | Blurred Eye w/ Brows |
| --- | --- | --- |
| <img src="/Plots/results/blurredeyes.png" width="400"/> | <img src="/Plots/results/blurredbrows.png" width="400"/> | <img src="/Plots/results/blurredeyeswbrows.png" width="400"/> |

| Blurred Mouth w/ Lips | Blurred Nose | Blurred Hair |
| --- | --- | --- |
| <img src="/Plots/results/blurredlips.png" width="400"/>| <img src="/Plots/results/blurrednose.png" width="400"/>| <img src="/Plots/results/blurredhair.png" width="400"/> |

| Blurred Skin | 
| --- |
| <img src="/Plots/results/blurredskin.png" width="300"/>| 
