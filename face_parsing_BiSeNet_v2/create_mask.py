#!/usr/bin/python
# -*- encoding: utf-8 -*-

from logger import setup_logger
from model import BiSeNet
import sys

import torch

import os
from os import path, listdir, makedirs
import os.path as osp
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import cv2
from tqdm import tqdm
import argparse



def vis_parsing_maps(im, parsing_anno, stride, save_im=False, save_path='vis_results/parsing_map_on_im.jpg', part = 'part'):

    im = np.array(im)
    vis_im = im.copy().astype(np.uint8)
    vis_parsing_anno = parsing_anno.copy().astype(np.uint8)
    vis_parsing_anno = cv2.resize(vis_parsing_anno, None, fx=stride,
                                  fy=stride, interpolation=cv2.INTER_NEAREST)

    
    #creating a mask that acts as an annotation
    mask = np.zeros_like(vis_parsing_anno)
    
    vis_parsing_anno_color = np.zeros((vis_parsing_anno.shape[0], vis_parsing_anno.shape[1], 3)) + 255
    num_of_class = np.max(vis_parsing_anno)
    


    # For individual parts 
    # changed this part for the logical or operation
    
    if part == 'eyes':
        index = np.where(np.logical_or(vis_parsing_anno == 4,vis_parsing_anno == 5))
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]
    
    elif part == 'eyeswbrows':
        index = np.where(np.logical_or.reduce((vis_parsing_anno == 2, vis_parsing_anno == 3, vis_parsing_anno == 4,vis_parsing_anno == 5,vis_parsing_anno ==6)))
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]
    
    elif part == 'brows':
        index = np.where(np.logical_or(vis_parsing_anno == 2, vis_parsing_anno == 3))
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]
    
    elif part == 'nose':
        index = np.where(vis_parsing_anno == 10)
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]
    
    elif part == 'mouthwlips':
        index = np.where(np.logical_or.reduce((vis_parsing_anno == 11,vis_parsing_anno == 12,vis_parsing_anno == 13)))
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]

    elif part == 'hair':
        index = np.where(vis_parsing_anno == 17)
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]
    
    elif part == 'skin':
        index = np.where(vis_parsing_anno == 1)
        mask[index[0],index[1]]=255
        vis_parsing_anno_color[index[0], index[1], :] = [255,0,0]

    vis_parsing_anno_color = vis_parsing_anno_color.astype(np.uint8)
    vis_im = cv2.addWeighted(cv2.cvtColor(vis_im, cv2.COLOR_RGB2BGR), 0.4, vis_parsing_anno_color, 0.6, 0)

    # Save result or not
    if save_im:
        #cv2.imwrite(save_path[:-4] + '_mask.png', vis_parsing_anno)
        #cv2.imwrite(save_path[:-4] +'_color_mask.png', vis_im, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        cv2.imwrite(save_path[:-4] + '_annotation.png', mask)


def evaluate(source='./data', dest='./res/test_res', cp='evaluate.pth',part = "part"):
    n_classes = 19
    net = BiSeNet(n_classes=n_classes)
    net.cuda()
    save_pth = osp.join('res/cp', cp)
    net.load_state_dict(torch.load(save_pth))
    net.eval()

    to_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])

   
    dspth = listdir(source)

    if not path.exists(dest):
        makedirs(dest)
    

    with torch.no_grad():
        for image_name in tqdm(dspth):
            
            image_path = path.join(source, image_name)
            img = Image.open(image_path)

            save_path = osp.join(dest, image_name)

            if os.path.isfile(save_path[:-4] + '_mask.png'):
                print('Skipping...')
                continue

            image = img.resize((512, 512), Image.BILINEAR)
            img = to_tensor(image)
            img = torch.unsqueeze(img, 0)
            img = img.cuda()
            out = net(img)[0]
            parsing = out.squeeze(0).cpu().numpy().argmax(0)
           

            vis_parsing_maps(image, parsing, stride=1, save_im=True, save_path=save_path,part=part)


# if __name__ == "__main__":
#     # parser = argparse.ArgumentParser(description="Create mask for the given part")

#     # parser.add_argument("--source","-s", help = "Path to folder with images")
#     # parser.add_argument("--dest","-d", help = "Path to folder to save the mask")
#     # parser.add_argument("--part","-p", help = "Part to create the mask for")

#     # args = parser.parse_args()

#     evaluate(source, dest, cp='79999_iter.pth',part)
