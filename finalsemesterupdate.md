# Demonstration of how much blurring changes the genuine plots

This section is intended to verify if the feature extractor that is being used in the project is a good one or not. In this project, feature extractor used is ResNet based model, trained with Additive Angular Margin Loss, as proposed by ArcFace[1]. This proposed approach not only maximizes inter-class distance, but also minimizes intra-class distance. So, in the context of this experiment, if comparison is made between image of a subject with one of the face part blurred with the original image of a subject, it will have a lower similarity score, because the representation will get spread out more as compared to the instance where both were originals. But, if comparison is made between image of a subject with one of the face part blurred with original face of another subject, there should be more or less the same difference as compared to if both originals were used, because ideally the interclass distance doesn't vary by that much - if we think about representation in 512-d space. This pattern holds in the following plots and thus, it can be said that the feature extractor is doing a great job.


<table>
    <tr><th colspan=2> Genuine and Impostor Distribution Plots with Original Images, Blurred Images and Cross-matched Images </th></tr>
  <tr><td align="center">Eyes</td><td align="center">Brows</td></tr>
    <tr><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_eyes.png" width="600"/></td><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_brows.png" width="600"/></tr>
  <tr><td align="center">Eyes with Brows</td><td align="center">Nose</td></tr>
  <tr><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_mouthwlips.png" width="600"/></td><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_nose.png" width="600"/></td></tr>
    <tr><td align="center">Mouth Region</td><td align="center">Hair</td></tr>
  <tr><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_skin.png" width="600"/></td><td><img src="/blurPlots/CMcrossmatch/distributionplots/crossmatch_hair.png" width="600"/></td></tr>
</table>
<br><br>


# Final Distribution Plots

This section is intended to show the genuine and impostor distribution plots, with one of the seven major parts blurred. This section summarizes all the plots for 4 ethnic categories (Caucasian Male, Caucasian Female, African-American Male and African-American Female), with seven parts ( Nose, Eyes, Brows, Eyes with brows, Mouth Region, Skin and Hair).

<table>
    <tr><th colspan=2> Genuine and Impostor Distribution for Blurred Eyes </th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_eyes.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_eyes.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_eyes.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_eyes.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring eye makes the shift in impostor roughly same in between ethnicity i.e almost similar for both genders in caucasian group and the same for African-American group. Similarly, genuine distribution is slightly worse for African-American group , whereas almost intact for Caucasian group. <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Brows</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_brows.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_brows.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_brows.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_brows.png" width="600"/></td></tr>
</table>
<br>
The impostor distribution results for brows different in sense that there is slightly greater shift for African-American group as Caucasian. Similarly, genuine distribution is almost intact, except for slight  <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Eyeswbrows</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_eyeswbrows.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_eyeswbrows.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_eyeswbrows.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_eyeswbrows.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring eye-socket region(eyes with brows) makes the shift in impostor roughly same, while leaving genuine distribution almost intact for all ethnic categories i.e Caucasian Male, Caucasina Female, African-American Male and African-American Female. <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Nose</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_nose.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_nose.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_nose.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_nose.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring nose makes the shift in impostor roughly same, while leaving genuine distribution almost intact for all ethnic categories i.e Caucasian Male, Caucasina Female, African-American Male and African-American Female. <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Mouth Region</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_lips.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_mouthwlips.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_mouthwlips.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_mouthwlips.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring mouth region(mouth and lips) makes the shift in impostor roughly same, while leaving genuine distribution almost intact for all ethnic categories i.e Caucasian Male, Caucasina Female, African-American Male and African-American Female. <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Hair</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_hair.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_hair.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_hair.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_hair.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring hair makes the shift in impostor roughly same, while leaving genuine distribution almost intact for all ethnic categories i.e Caucasian Male, Caucasina Female, African-American Male and African-American Female. <br><br><br>
<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Skin</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_skin.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_skin.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_skin.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_skin.png" width="600"/></td></tr>
</table>
<br>
The plot above shows that blurring skin(all face expect nose,mouth,brows and eyes) makes the shift in impostor roughly same, while leaving genuine distribution almost intact for all ethnic categories i.e Caucasian Male, Caucasina Female, African-American Male and African-American Female. <br><br>

# Results and Discussion

One of the major finding of this project is that the importance of a specific part is more or less ethnicity agnostic. For eg: nose is more or less equally important for all ethnic categories considered. In other words, nose is not more important of a facial feature for AAM and less for CM and so on. There was some deviation observed for brows and eyes, but it is not greatly significant. This finding allows to come up with a general conclusion about which part of the face is more important for face recognition, for all ethnic categories namely Caucasian Male, Caucasian Female, African-American Male and African-American Female, that were taken into consideration for this project. 
<br><br>
The second major finding from this work is that, the importance of facial parts is not directly propotional to number of pixels. From the above plots, it can be seen that impostor distribution shifts to a higher score(more similar), more or less the same when blurring is done for nose, eyes with brows and whole skin(all face except nose, eyebrows, ear, mouth and hair). This simply indicates that more pixels(associated with face) doesn't neccessarily mean more information. From this experiment, it can be concluded that - Eye Socket Region(Eyes with Brows) and Nose are the most salient region for face recognition system. 
<br><br>
The main goal of this project was to see if any specific part of the face is driving the difference significantly. It turns out the facial parts are not the main drivers of this difference. Combining the affect of several parts that has been considered for this experiment might show us some significant difference, but individually the parts are not - at least the ones considered for the project. It could also be that, the difference in facial recognition accuracy are due to some gender-specific styles. For eg, the impostor for male might be lower, because there might be more pairs of male faces one with beard and other without. For women, the images might differs in terms of make-up, but the dataset used for this project has a control for that, meaning the images of women are more uniform. This might be the cause of high FMR for women. So, the overall conclusion is that - one of the major parts considered for this project is not the major driver of gender accuracy difference and the cause of that could be some gender specific styles.

# Future Work

- Repeat this work with ResNet based model with a different loss function
- Repeat this work with a different dataset

# References

1) Deng, J., Guo, J., Xue, N., & Zafeiriou, S. (2019). Arcface: Additive angular margin loss for deep face recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4690-4699).



