# Demonstration of how much blurring changes the genuine plots

This section is intended to verify if the feature extractor that is being used in the project is a good one or not. In this project, feature extractor used in ResNet based model, trained with Additive Angular Margin Loss, as proposed by ArcFace[]. This proposed approach not only maximizes inter-class distance, but also minimizes intra-class distance. So, in the context of this experiment, if comparison is made between image of a subject with one of the face part blurred with the original image of a subject, it will have a lower similarity score, because the representation will get spread out more as compared to the instance where both were originals. But, if comparison is made between image of a subject with one of the face part blurred with original face of another subject, there should be more or less the same difference as compared to if both originals were used, because ideally the interclass distance doesn't vary by that much - if we think about representation in 512-d space. This pattern holds in the following plots and thus, it can be said that the feature extractor is doing a great job.


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
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Brows</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_brows.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_brows.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_brows.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_brows.png" width="600"/></td></tr>
</table>
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Eyeswbrows</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_eyeswbrows.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_eyeswbrows.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_eyeswbrows.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_eyeswbrows.png" width="600"/></td></tr>
</table>
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Nose</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_nose.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_nose.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_nose.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_nose.png" width="600"/></td></tr>
</table>
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Mouth Region</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_lips.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_mouthwlips.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_mouthwlips.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_mouthwlips.png" width="600"/></td></tr>
</table>
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Hair</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_hair.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_hair.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_hair.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_hair.png" width="600"/></td></tr>
</table>
<br><br>

<table>
    <tr><th colspan=2>Genuine and Impostor Distribution for Blurred Skin</th></tr>
  <tr><td align="center">Caucasian Male</td><td align="center">African-American Male</td></tr>
    <tr><td><img src="/blurPlots/CM/distributionplots/blurred_skin.png" width="600"/></td><td><img src="/blurPlots/AAM/distributionplots/blurred_skin.png" width="600"/></tr>
  <tr><td align="center">Caucasian Female</td><td align="center">African-American Female</td></tr>
  <tr><td><img src="/blurPlots/CF/distributionplots/blurred_skin.png" width="600"/></td><td><img src="/blurPlots/AAF/distributionplots/blurred_skin.png" width="600"/></td></tr>
</table>
<br><br>

# Results and Discussion

One of the major finding of this project is that the importance of a specific part is more or less ethnicity agnostic. For eg: nose is more or less equally important for all ethnic categories considered. In other words, nose is not more important of a facial feature for AAM and less for CM and so on. This is a conclusion from the general pattern seen in the plot. For future work, results from a more rigid statistical measure can be reported to prove this. 
<br><br>
The second major finding from this work is that, the importance of facial parts is not directly propotional to number of pixels. From the above plots, it can be seen that impostor distribution shifts to a higher score(more similar), more or less the same when blurring is done for nose, eyeswbrows and whole skin(all face except nose, eyebrows, ear, mouth and hair). This simply indicates that more pixels(associated with face) doesn't neccessarily mean more information. From this experiment, it can be concluded that - Eye Socket Region(Eyes with Brows) and Nose are the most salient region for face recognition system. 

# Future Work

- Repeat this work with ResNet based model with a different loss function
- Repeat this work with a different dataset





