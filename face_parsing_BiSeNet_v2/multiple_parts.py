from create_blur_part import *
from create_mask import *
from tqdm import tqdm
import argparse
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a face with blurred mask region")
    parser.add_argument("--source","-s", help = "Path to folder with images")
    parser.add_argument("--maskdest","-m", help = "Path to folder to save the images with blurred part")
    parser.add_argument("--finaldest","-d", help = "Path to folder to save the images with blurred part")
    args = parser.parse_args()

    parts = ['eyes','eyeswbrows','brows','nose','mouthwlips','hair','skin']

    for part in tqdm(parts):
        print(part)
        evaluate(args.source, args.maskdest + "mask_{}".format(part) , cp='79999_iter.pth',part = part)
    
    for part in tqdm(parts):
        print(part)
        blur_image(imgPath=args.source, maskPath=args.maskdest + "mask_{}".format(part), savePath=args.finaldest +"blurred_{}/".format(part), part = part,save_img=True)
