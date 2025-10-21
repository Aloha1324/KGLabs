import numpy as np
from PIL import Image, ImageOps
import math
from math import cos, sin, pi
from random import randint


def draw_polygons(img, x0, y0, x1, y1, x2, y2):
    
    
    xmin = min(x0, x1, x2)
    xmax = max(x0, x1, x2)
    ymin = min(y0, y1, y2)
    ymax = max(y0, y1, y2)
    if xmin < 0: xmin = 0
    if ymin < 0: ymin = 0

    color =(randint(0,255), randint(0,255), randint(0, 255))#[100, 255, 200]
    
    for y in range(int(ymin), int(ymax) + 1):
        for x in range(int(xmin), int(xmax) + 1):

            lambda0, lambda1, lambda2 = barycentric_coordinates(x, y, x0, y0, x1, y1, x2, y2)
            if lambda0 >= 0.0 and lambda1 >= 0.0 and lambda2 >= 0.0:
                img[y][x] = color
              


def barycentric_coordinates(x, y, x0, y0, x1, y1, x2, y2):
    lambda0 = (((x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2)))
    lambda1 = (((x0 - x2) * (y - y2) - (x - x2) * (y0 - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2)))

    lambda2 = 1.0 - lambda0 - lambda1
    return lambda0, lambda1, lambda2


img_mat = np.zeros((2000, 2000, 3), dtype=np.uint8)
file_in = open('model_1.obj')
v = []
f = []


for s in file_in:
    sp = s.split()
    if sp[0] == 'v':
        v.append([float(sp[1]), float(sp[2]), float(sp[3])])
    elif sp[0] == 'f':
        f.append([sp[1].split('/')[0], sp[2].split('/')[0], sp[3].split('/')[0]])

 
for i in range(0,len(f)):
  
    x0 = (5000 * v[int(f[i][0]) - 1][0] + 500)
    y0 = (5000 * v[int(f[i][0]) - 1][1] + 500)

    x1 = (5000 * v[int(f[i][1]) - 1][0] + 500)
    y1 = (5000 * v[int(f[i][1]) - 1][1] + 500)
    
    x2 = (5000 * v[int(f[i][2]) - 1][0] + 500)
    y2 = (5000 * v[int(f[i][2]) - 1][1] + 500)
   
    
    color = (100, 255, 250)
    draw_polygons(img_mat, x0, y0, x1, y1, x2, y2,)


img = Image.fromarray(img_mat, mode='RGB')
img = ImageOps.flip(img)
img.save('krolik2.0.0.png')
img.show()
