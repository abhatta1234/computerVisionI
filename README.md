# Genuine and Impostor Distribution with Face Part Blurring

All the code repos required to reproduced this results are put in a google drive link in the section below:

[Google Drive Link For All Repos](https://drive.google.com/drive/folders/1BxMBhLNl82rzaw-xX3-SCCw9ivsHB9hr?usp=sharing)

**Note: Make Sure that all the repos - insightface, face_parsing_BiSeNet and face_matching are at the same directory level.**

# BiSeNet Segmentation

In this project, modified version of BiSeNet Segmentation was used. The orginal implementation of this modified version can be found [here](https://github.com/zllrunning/face-parsing.PyTorch). The most relevant python files are put in folder "face_parsing_BiSeNet" and are:<br>
- create_mask.py
- create_blur_part.py
- multiple_parts.py

### Example Usage

To generate images with blurred parts, following script with proper inputs are shown below. This scripts takes in directory of images, creates a mask for particular part, saves the mask in intermediate directory, and finally, uses this mask to create the image with blurred part. 

~~~bash
python3 ./face_parsing_BiSeNet/multiple_parts.py -s /path_folder_with_images/ -m /intermediate_folder_to_save_mask/ -d /destination_to_save_images
~~~

#### Note:

The original modified implementation of BiSeNet only processes single images. To process the whole directory, the usage was heavily inspired from this [github repo](https://github.com/vitoralbiero/face-parsing.PyTorch).

# Feature Extraction

The feature extractor used in this project is from [ArcFace Paper](https://arxiv.org/abs/1801.07698) and the usage is adapted from repo, which can be found [here](https://github.com/vitoralbiero/face_matching). There are several options for different architecture based feature extractor, but for this project - ArcFace was used and all the pre-trained model required to reproduce the results provided ** Here ** .

### Example Usage

~~~bash
python3 ./face_matching/insightface_feature_extraction.py -s /path_folder_with_images/ -d /destination_to_save_extractions
~~~

The feature returned from above feature extraction returns folders with .npy file. To use the results for further steps, create a list with the absolute path of this directory. This [link](https://unix.stackexchange.com/questions/268474/how-to-list-all-files-in-a-directory-with-absolute-paths) might be helpful. First 5 lines of such list could be something like this :

~~~bash
/usr/Desktop/saved_features/img1.npy
/usr/Desktop/saved_features/img2.npy
/usr/Desktop/saved_features/img3.npy
/usr/Desktop/saved_features/img4.npy
/usr/Desktop/saved_features/img5.npy
~~~

#### Note : 

- This setting assumes, input size of (112,112). Add --image-size argument while running the script, with appropriate value, if a different image size is to be used. 
- Make sure that there is absolutely no additional lines in the list file(.txt).

# Feature Matching

Cosine Similarity is the metrics used to find the similarity between two 512-d representation, which is the ouput from feature extraction used above.

### Example usage:

This usage is in case when the both the probe and gallery list are blurred, meaning that you are matching within the list

~~~bash
python3 ./face_matching/feature_match_efficient.py -p ./file_with_abspath_features.txt -o /destination_to_save_match_results -d dataset_name -gr CM
~~~

- Dataset for this project : MORPH
- Groups: CM, CF, AAM, AAF
- Save Format: For CM (for example) - results will be saved something like CM_authentic.npy, CM_impostor.npy, CM_labels.txt in the destination folder

To cross-match i.e match images with blur parts with original image,  the gallery list can be introduced as follows:

~~~bash
python3 ./face_matching/feature_match_efficient.py -p ./file_with_abspath_probe.txt -g ./file_with_abspath_gallery.txt -o /destination_to_save_match_results -d dataset_name -gr CM
~~~

# Plots

All the functions used for plotting are inside Plots folder of face_matching repo. The authentic and impostor distribution npy file required for this part is the result of matching done above.

### Example Usage

~~~bash
python3 ./face_matching/Plots/plot_relative_freq_histogram_v2.py -a1 ../authentic_dist1.npy -i1 ../impostor_dist1.npy -l1 Label1 -a2 ../authentic_dist2.npy -i2 ../impostor_dist2.npy -l2 Label2 -t 'Tittle' -d ../plot_save_folder -n output
~~~

# Dataset

The dataset used in this project can be found below:

[Curated MORPH Subset](https://drive.google.com/drive/folders/1BxMBhLNl82rzaw-xX3-SCCw9ivsHB9hr?usp=sharing)




