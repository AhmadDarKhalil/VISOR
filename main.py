#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:04:58 2022

@author: ru20956
"""
from vis import *
json_files_path = '/home/ru20956/Downloads/visor_release_v3_train_val_test/sample_json'
output_directory ='/home/ru20956/Downloads/out_pngs/sample_masks'
input_resolution = (1920,1080)
output_resolution= (1920,1080)


folder_of_jsons_to_masks_new(json_files_path, output_directory,input_resolution,output_resolution)
