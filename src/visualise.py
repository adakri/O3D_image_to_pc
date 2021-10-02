import open3d as o3d
import numpy as np
import copy
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import matplotlib.pyplot as plt 
import time



"""
Visualization functions
Uses the gui module to create a window and represent the different point clouds given
A more detailed and user oriented gui is in the  works 
"""


"""
Draws two point clouds in a automatically opened window
"""
def draw_test(source, target):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    o3d.visualization.draw_geometries([source_temp, target_temp])
    
    
    
"""
Draws multiple point clouds given in a list (also draws any other geometric entities
like bounding boxes, lines....
"""
def draw_tests(source, bounding_box = True):
    #Source is a pc list
    source_temp=[]
    if(len(source)==2):
        draw_test(source[0], source[1])
    else:
        source_temp.append( copy.deepcopy(source[0]))
        source_temp[0].paint_uniform_color([1, 0.706, 0])  
        aabb = source_temp[0].get_axis_aligned_bounding_box()  
        obb = source_temp[0].get_oriented_bounding_box() 
        
        
        for i in range(1,len(source)-1) :
            k=int(i%2==0)
            source_temp.append(copy.deepcopy(source[i]))
            source_temp[i].paint_uniform_color([0.62*k, 0.07*k + 0.4*(1-k), 0.04*k + 0.2*(1-k) ])   
        source_temp.append(copy.deepcopy(source[len(source)-1]))
        source_temp[len(source)-1].paint_uniform_color([0, 0.651, 0.929])
        
        if(bounding_box):
            source_temp.append(aabb)
            source_temp.append(obb)
        o3d.visualization.draw_geometries(source_temp)


        
        



"""
The GUI in works, not used in main py file
"""
        
def create_gui(pc):
    app = gui.Application.instance
    app.initialize()

    w = app.create_window("Open3D - 3D point cloud test", 1024, 768)
    widget3d = gui.SceneWidget()
    widget3d.scene = rendering.Open3DScene(w.renderer)
    mat = rendering.Material()
    mat.shader = "defaultUnlit"
    mat.point_size = 5 * w.scaling
    widget3d.scene.add_geometry("Points", pc, mat)
    for idx in range(0, len(pc.points)):
        widget3d.add_3d_label(pc.points[idx], "{}".format(idx))
    bbox = widget3d.scene.bounding_box
    widget3d.setup_camera(60.0, bbox, bbox.get_center())
    w.add_child(widget3d)

    app.run()
        

