import numpy as np
import struct
from open3d import *
import os
# import pptk

def convert_data(file_path):
    # Convert .bin files to .pcd file
    size_float = 4
    list_pcd = []
    with open(file_path, "rb") as f:
        byte = f.read(size_float*4)
        while byte:
            x,y,z,intensity = struct.unpack("ffff", byte)
            list_pcd.append([x,y,z])
            byte = f.read(size_float*4)
    np_pcd = np.asarray(list_pcd)
    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(np_pcd)
    return pcd

def save_pcd(directory):
    i = 0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".bin"):

            res = convert_data(directory + "/" + filename)
            open3d.io.write_point_cloud("point_cloud_data/" + str(i) + ".pcd", res)
            # print(i)
            i = i + 1


# def visualize():


if __name__ == '__main__':
    directory = "kitti_dataset/data_object_velodyne/training/velodyne"
    # save_pcd(directory)
    # Read the point cloud and display the files
    cloud = []
    for i in range(0,20):
        cloud.append(open3d.io.read_point_cloud("point_cloud_data/" + str(i) + ".pcd"))
    open3d.visualization.draw_geometries([cloud[0]])
    # open3d.visualization.draw_geometries_with_animation_callback(geometry_list = [cloud_0, cloud_1, cloud_2, cloud_3, cloud_4, cloud_5, cloud_6])

