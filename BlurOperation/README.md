This code shows how to generate the blurred version of an image based on human annotations.
There is one example in the "Example" folder for the artificial eye used in Figure 3 in the paper.
The program here recreates the plots from Figure 3.

The program "blur_image_example.py" walks through the process of applying the annotations.

We do not supply the training/inference code as we use the implementation of D-NetPAD found here: https://github.com/iPRoBe-lab/D-NetPAD

The main contribution of this paper is the density based blurring of images which the program supplied outlines.

To run:
python3 blur_image_example.py

Dependencies:
OpenCV, Numpy, Matplotlib, Scipy, Seaborn