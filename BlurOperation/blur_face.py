
# Original Author : Aidan Boyd
# Modified for purpose : Aman Bhatta

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import scipy.ndimage
import seaborn as sns
from copy import deepcopy

## This is used to calculate the blur amount based on a polynomial
def get_curve(max_blur,val,order=4):
    val = (1/(max_blur**(order-1)))*(val**order) # (1/max^3)x^4
    return val


def blur_image(im,stacked_img,max_blur,curved):

    blurred_im = deepcopy(im) # to hold final image
    stacked_img = scipy.ndimage.gaussian_filter(stacked_img, 5) # Blur this image so no hard boundaries between different levels
    scaled_img = stacked_img/(stacked_img.max()/max_blur) # Scale image back to range 0 to sigma max so we get correct blur level

    scaled_img = np.around(scaled_img,decimals=1) # Round to one decimal place
    uniq_vals = np.unique(scaled_img)
    for scaled_val in uniq_vals: # for all possible blur levels
        blur_amount = round(max_blur - scaled_val, 1)
        if curved: # based on polynomial instead of linear
            blur_amount  = get_curve(max_blur,blur_amount,order=4)
        
        if blur_amount != 0: # if blurring required
            indices = np.where(scaled_img == scaled_val) # where this level of blur should be applied
            qwerty = scipy.ndimage.gaussian_filter(im, blur_amount)
            blurred_im[indices] = qwerty[indices] # apply that blur level to the specified pixels
    return blurred_im


if __name__ == "__main__":

    sigma_max = 15 # You can set this to any value
    curved = True # Use a non-linear function to calculate blur

    #mask folder
    example_annotations = "./Example/Annotations/checkAnno.png"

    #original image
    example_image = cv2.imread('./Example/Images/check.JPG',cv2.IMREAD_GRAYSCALE)

    # Resize the original image to match the size of the annotation
    example_image = cv2.resize(example_image,(512,512),interpolation=cv2.INTER_NEAREST)
    stacked_img = cv2.imread(example_annotations,cv2.IMREAD_GRAYSCALE)
    
    # Generate blurred image
    blurred_image = blur_image(example_image,stacked_img,sigma_max,curved) 

    # For display purposes
    color_example_image = cv2.cvtColor(example_image,cv2.COLOR_GRAY2RGB)
    mask_annotation = cv2.cvtColor(stacked_img,cv2.COLOR_GRAY2RGB)
    color_blurred_image = cv2.cvtColor(blurred_image,cv2.COLOR_GRAY2RGB)
    combined_image = np.concatenate((color_example_image,mask_annotation,color_blurred_image),axis=1)
    plt.cla()
    plt.imshow(combined_image)
    plt.title("Original image | Annotation | Blurred Image")
    plt.show()