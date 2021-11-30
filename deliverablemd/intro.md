# Computer Vision I

This repository is for all assignment related to Computer Vision class for Fall 2021 at the University of Notre Dame.


Dataset : I will be using MORPH datasets to perform the experiments for the computer vision project. MORPH is a facial age estimation dataset, which contains 55,134 facial images(headshot) of 13,617 subjects ranging from 16 to 77 years old - published by UNC Wilmington. I have the dataset in my CRC home directory and this data set has been previously used by members of Notre Dame CVRL for research. I don't think I would need to create a test/train/validation split because I am not training any deep neural net models from scratch or rather at all. I am using all pre-trained models - ArcFace and BiSeNet for the project. Additionally, the overall goal of this project is to understand what part of the face is causing or adding more weight to difference in accuracy between gender - so I cannot think of a way that I would need such a data split.


Planned Steps for the project:

1) Run the BiSeNet image segmentor and get the targeted areas such as nose, mouth, eyes, ear, forehead, etc. (Have no experience with BiSeNet, so I might have no idea what I am talking about)
2) Blur one of the targeted area at once in all the images ( I am not exactly sure how to do it!)
3) Run an ArcFace to get 512d feature vector representation
4) Perform some similarity metrics, much likely cosine similarity to compare the obtained feature vector
5) Plot genuine and impostor distribution with statistics from blurred image and real image and compare.
6) Repeat the same step with all essential parts
