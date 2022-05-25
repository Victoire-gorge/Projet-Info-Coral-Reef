import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

input_json = open('metrics.json','r')

lines = input_json.readlines()

def parse_line(input_line):
    input_line = input_line[1:-2].split(',')
    output_array = []
    for i in input_line:
        current_value = i.split(':')[-1]
        output_array.append(float(current_value))
    return output_array

def parse_json():
    buffer_array = []
    for i in lines:
        if 'bbox' in i:
            continue
        current_array = parse_line(i)
        buffer_array.append(current_array)
    
    output_array = [[] for i in buffer_array[0]]

    for i in buffer_array:
        count = 0
        for j in i:
            output_array[count].append(j)
            count += 1
    
    return output_array

metrics_array = parse_json()

fig,axs = plt.subplots(2,5)
axs[0,0].plot(metrics_array[1],metrics_array[2][::-1])
axs[0,0].set_title('cls accuracy')
axs[1,0].plot(metrics_array[1],metrics_array[3][::-1])
axs[1,0].set_title('false negative')
axs[0,1].plot(metrics_array[1],metrics_array[4][::-1])
axs[0,1].set_title('fg cls accuracy')
axs[1,1].plot(metrics_array[1],metrics_array[6][::-1])
axs[1,1].set_title('loss box reg')
axs[0,2].plot(metrics_array[1],metrics_array[7][::-1])
axs[0,2].set_title('loss cls')
axs[1,2].plot(metrics_array[1],metrics_array[8][::-1])
axs[1,2].set_title('loss rpn cls')
axs[0,3].plot(metrics_array[1],metrics_array[9][::-1])
axs[0,3].set_title('loss rpn loc')
axs[1,3].plot(metrics_array[1],metrics_array[10][::-1])
axs[1,3].set_title('lr')
axs[0,4].plot(metrics_array[1],metrics_array[16][::-1])
axs[0,4].set_title('total loss')

plt.show()