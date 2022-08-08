#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:04:58 2022

@author: Ahmad Darkhalil
"""
from vis import *
import os

json_files_path = '/home/ru20956/Downloads/visor_release_v3_train_val_test/sample_json'
output_directory ='/home/ru20956/Downloads/out_pngs/sample_masks'
input_resolution = (1920,1080)
output_resolution= (192,108)
is_overlay=True
images_root_directory = '/home/ru20956/Downloads/DATA/Images_fixed_train_val_test'


folder_of_jsons_to_masks_new(json_files_path, output_directory,is_overlay=is_overlay,images_root_directory=images_root_directory,input_resolution=input_resolution,output_resolution=output_resolution)
generate_video_from_images(os.path.join(output_directory+'/P28_103'), 3)
