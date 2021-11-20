
# Importing modules

import os
import cv2
import matplotlib.pyplot as plt
from numpy.lib.npyio import save
import scipy.ndimage
import numpy as np
from skimage.filters import gaussian
import sys
from tqdm import tqdm
import argparse
# Some useful functions:

def get_kernel(part):
    if part == "eyes":
        ksize = 5
        iterations = 4
    elif part == "nose":
        ksize = 5
        iterations=3
    elif part == "eyeswbrows":
        ksize = 5
        iterations=4
    elif part == "hair":
        ksize = 5
        iterations = 4
    elif part == "mouthwlips":
        ksize = 5
        iterations = 4
    elif part == "skin":
        ksize = 0
        iterations = 0
    elif part == "brows":
        ksize = 5
        iterations = 2

    return ksize,iterations

def blur_image(imgPath,maskPath,savePath,part,save_img=False):
    
    if not os.path.exists(savePath):
        os.makedirs(savePath)
        
    for filename in tqdm(os.listdir(imgPath)):

        face_img = cv2.imread(os.path.join(imgPath,filename),cv2.IMREAD_COLOR)
        face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

        mask_name = filename.split(".")[0] + "_annotation.png"

        org_mask = cv2.imread(os.path.join(maskPath,mask_name))
        org_mask = cv2.resize(org_mask, (224,224), interpolation = cv2.INTER_AREA)
        
        ksize,iterations = get_kernel(part)
        
        kernel = np.ones((ksize,ksize), np.uint8)

        dilated_mask = cv2.dilate(org_mask, kernel, iterations=iterations)


        blurred_mask = scipy.ndimage.gaussian_filter(dilated_mask,5)
        blurred_mask = blurred_mask/255


        blurred_face = cv2.blur(face_img, (15, 15))


        final_image = (blurred_mask * blurred_face + (1.0 - blurred_mask)* face_img)
        final_image = final_image.astype("uint8")
        
        if save_img:
            # imwrite by default used bgr so change it rgb before saving 
            cv2.imwrite(savePath + filename , cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a face with blurred mask region")

    parser.add_argument("--source","-s", help = "Path to folder with images")
    parser.add_argument("--mask","-m", help = "Path to folder with annotated masks")
    parser.add_argument("--dest","-d", help = "Path to folder to save the images with blurred part")
    parser.add_argument("--part","-p", help = "Part to blur, needed to know mask dilation")

    args = parser.parse_args()

    blur_image(imgPath=args.source, maskPath=args.mask, savePath=args.dest, part = args.part,save_img=True)
