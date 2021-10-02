# -*- coding: utf-8 -*-
import open3d as o3d
import numpy as np
import visualise as vis


import sys
import os
import copy
import random


import tools as helper
from PIL import Image


#change the path absoluteness and the use of links


def convert_to_bw(img_path):
    img = Image.open(img_path)
    thresh = 100
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    r.save('/home/abdel_dakri/work/Python/Open3D tool/img/temp_converted.png')



def image_tag_to_point_cloud_bw(img_path):
    """
    Convert image of apriltag to point cloud.
    """
    
    img = o3d.io.read_image(img_path)

    o3d.visualization.draw_geometries([img],
    width = 480, height = 640)

    """
    convert_to_bw(img_path)

    img = o3d.io.read_image("/home/abdel_dakri/work/Python/Open3D tool/img/temp_converted.png")
    
    o3d.visualization.draw_geometries([img],
    width = 480, height = 640)
    """
    np_img = np.array(img)
    print(img)
    print(np_img.shape)
    
    x,y,z = np_img.shape
    
    randomlist1 = random.sample(range(0, x), x)
    randomlist2 = random.sample(range(0, y), y)
    
    img_points = []
    img_colours = []
    
    

    #sys.exit()


    for i in range(x):
        for j in range(y):
            sum = int(np_img[i][j][0]) + int(np_img[i][j][1]) + int(np_img[i][j][2])
            #sum = np_img[i][j][0]
            #print(sum)
            img_points.append([i/x,j/y,0.])
            if(sum == 0):
                #print(sum)
                img_colours.append([0.,0.,0.])
            else:
                #print(sum)
                img_colours.append([1.,1.,1.])
                
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(img_points)
    pcd.colors = o3d.utility.Vector3dVector(img_colours)
    
    
    o3d.visualization.draw_geometries([pcd],width = 480, height = 720)
    
    return pcd


def main():
    image_path = helper.parse_cmd_line()
    image_tag_to_point_cloud_bw(image_path)
    return 0


if __name__ == "__main__": 
    main()



