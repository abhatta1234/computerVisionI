# %% 

import numpy as np

x = np.array([1,2,3])
print(x)


# %%
import cv2
import os

upperBinDirectory = "/afs/crc.nd.edu/user/a/abhatta/genImpPlot/upperBin"

print("before Changing")
print(os.getcwd())


print("after changing")
os.chdir(upperBinDirectory)
print(os.getcwd())


imgOne = os.listdir()[0]

print(imgOne)

image = cv2.imread(imgOne)
#cv2.imshow("image",image)
#cv2.waitKey(0)

# %%
