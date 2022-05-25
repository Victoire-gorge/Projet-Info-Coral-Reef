from ast import parse
from hashlib import new
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import shutil, os
from tqdm import tqdm


train = pd.read_csv('train.csv')
train = train.loc[train['annotations'] != '[]']

def create_new_dataset():
    sub_train = train.loc[:,['video_id','video_frame']]
    video_pos = []
    for i in sub_train.values:
        video_pos.append('import/train_images/video_' + str(i[0]) + '/' + str(i[1]) + '.jpg')
    for i in tqdm(range(len(video_pos))):
        shutil.copy(video_pos[i],'data_set/' + str(i) + '.jpg')

def parse_annotation(input_annotation):
    input_annotation = input_annotation.split(',')
    output = []
    for i in input_annotation:
        current_value = ''.join(c for c in i if c.isdigit())
        if(len(list(current_value)) > 0):
            output.append(int(current_value))
    return output

def create_annotation_files():
    for i in tqdm(range(train.shape[0])):
        current_row = train.iloc[i].values[-1][2:-1].split('{')
        current_file = open('annotations/' + str(i) + '.txt','w')

        for j in current_row:
            current_row_annotation = parse_annotation(j)

            new_x = np.interp(current_row_annotation[0],[0,1280],[0,1])
            new_y = np.interp(current_row_annotation[1],[0,720],[0,1])
            new_width = np.interp(current_row_annotation[2],[0,1280],[0,1])
            new_height = np.interp(current_row_annotation[3],[0,720],[0,1])

            new_x += new_width/2
            new_y += new_height/2

            current_file.write('starfish ' + str(new_x) + ' ' + str(new_y) + ' ' + str(new_width) + ' ' + str(new_height) + '\n')
        
        current_file.close()

create_annotation_files()

"""
current_row_annotation = parse_annotation(train.iloc[i].values[-1])
current_file = open('annotations/' + str(i) + '.txt','w')
new_x = np.interp(current_row_annotation[0],[0,1280],[0,1])
new_y = np.interp(current_row_annotation[1],[0,720],[0,1])
new_width = np.interp(current_row_annotation[2],[0,1280],[0,1])
new_height = np.interp(current_row_annotation[3],[0,720],[0,1])

new_x += new_width/2
new_y += new_height/2

current_file.write('starfish ' + str(new_x) + ' ' + str(new_y) + ' ' + str(new_width) + ' ' + str(new_height))
current_file.close()
"""
