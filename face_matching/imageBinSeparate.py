# This code is to separate the files to 2 bins based on the threshold
# Amazon Parser Code : originally by Vitor Albiero , modified by : Aman Bhatta

 # %% 

 # Importing modules

import json
import numpy as np
from tqdm import tqdm
import os
import matplotlib.pyplot as plt
import shutil # package to move files using python


# %%

# Changing the directory to access the files

original_directory = os.getcwd()
json_directory = "/afs/crc.nd.edu/user/a/abhatta/json_files"
os.chdir(json_directory)


# %%

# Code to parse the confidence values from the amazon file

predictions = []
female_list = []
misClassfiedCount = 0

json_list = os.listdir()

# Seems like 98 can be used as the experimental value for the threshold division

threshold_value = 98
lowerBin = 0
upperBin = 0

for json_name in tqdm(json_list):

    file = open(json_name, 'r')
    response = json.load(file)

    if len(response['FaceDetails']) > 0:
        gender = response['FaceDetails'][0]['Gender']['Value']
        confd_val = response['FaceDetails'][0]['Gender']['Confidence']

        if gender.lower() == "male":
            predictions.append([json_name, gender,confd_val])

        if gender.lower() == "female":
            misClassfiedCount += 1
            confd_val = -1 * confd_val
            predictions.append([json_name, gender,confd_val])
        

        if confd_val < threshold_value:
            lowerBin += 1

        else:
            upperBin += 1


    else:
        gender = "None"
        confd_val = 0


print("The number of males classified as female are: ", misClassfiedCount)

# %%



# %%

# Code for the histogram plot to see general confidence score distribution

x = [indList[2] for indList in predictions]  
plt.hist(x, bins = 5000)
plt.show()


# %%


# Directories where to move files

imgDirectory = "/afs/crc.nd.edu/user/a/abhatta/genImpPlot/01"
upperBinDirectory = "/afs/crc.nd.edu/user/a/abhatta/genImpPlot/upperBin"
lowerBinDirectory = "/afs/crc.nd.edu/user/a/abhatta/genImpPlot/lowerBin"


# Code to move files to their respective Bins
count1 = 0
count2 = 0

for output in predictions:

    if output[2] < threshold_value:
        
        toExtract = output[0]
        intermediate = toExtract.split(".")
        finalString = intermediate[0] + ".JPG"
        imagePath = os.path.join(imgDirectory,finalString)

        # This step is to copy the images from one folder to other
        # Comment it after one run
        
        #shutil.move(imagePath,lowerBinDirectory)
        

    else:

        toExtract = output[0]
        intermediate = toExtract.split(".")
        finalString = intermediate[0] + ".JPG"
        imagePath = os.path.join(imgDirectory,finalString)

        # This step is to copy the images from one folder to other
        # Comment it after one run

        #shutil.move(imagePath,upperBinDirectory)
        





