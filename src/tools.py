#import open3d as o3d
import numpy as np
import open3d as o3d
import math
import argparse
import os



"""
Auxiliary functions module
"""


"""
Parses the command line to get the entry point cloud file 
name and the user parameters file
"""
def parse_cmd_line():
    parser = argparse.ArgumentParser()

    parser.add_argument("--name",help="Name of the image to be converted",required=True)
    
    args = parser.parse_args()
    
    
    print("\n")
    print("You chose to use the image file",args.name)
    
    return args.name



"""
Preprocessing the point cloud and parameters
"""



"""
Load the ply file into an open3D compatible file format
"""
def load_pc(file_name):
    print("______________________________________________________")
    pcd = o3d.io.read_point_cloud(file_name)
    return pcd
    
    
"""
Print point cloud as array
"""    
def display_pc(pc):
    print(np.asarray(pc.points))


"""
Find point cloud size.
"""
def find_size_pc(pc):

    pc_np_array = np.asarray(pc.points)    
    size_pc = int(np.size(pc_np_array) / 3)
    
    return size_pc
    
