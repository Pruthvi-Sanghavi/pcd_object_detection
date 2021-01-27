import numpy as np
import struct
from open3d import *
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

def save_pcd(pcd):
    open3d.io.write_point_cloud("pointcloud_1.pcd", pcd)

# def visualize():

if __name__ == '__main__':
    file_path = "kitti_dataset/data_object_velodyne/training/velodyne/000000.bin"
    res = convert_data(file_path)
    # Read the point cloud and display the files
    cloud = open3d.io.read_point_cloud("pointcloud_1.pcd")
    open3d.visualization.draw_geometries([cloud])


    # open3d.io.write_point_cloud("pointcloud_1.pcd", res)