#!/usr/bin/env python2

import sys
import numpy as np
import time
import os
from glob import glob
import random
import multiprocessing
import urllib
import zipfile

import vis

sys.path.append('../../py/')
import pyoctnet


# random.seed(42)
# np.random.seed(42)

vx_res = 512
n_threads = 10


# create oc from voxel grid
dense = np.random.random([vx_res,vx_res,vx_res]).astype("float32")
np.save("densehai",dense)
# dense[:,0,1:vx_res-1] = 1
# dense[:,vx_res-1,1:vx_res-1] = 1
# dense[:,:,1] = 1
# dense[:,:,vx_res-2] = 1
# val_range = np.array([(0.9, 1.1)], dtype=np.float32)
grid = pyoctnet.Octree.create_from_dense(dense[np.newaxis], n_threads=n_threads,threshold=0.000001)
# oc_from_dense2 = pyoctnet.Octree.create_from_dense2(dense, dense[np.newaxis,...].copy(), n_threads=n_threads)
s="lol"
b = bytes(s, 'utf-8')
# vis.write_ply_voxels('dense.ply', dense)
grid.write_bin(b)

# vis.write_ply_voxels('oc_from_dense1.ply', oc_from_dense1.to_cdhw())
# vis.write_ply_voxels('oc_from_dense2.ply', oc_from_dense2.to_cdhw())


# # create from point cloud
# xyz = np.random.normal(0, 1, (100, 3)).astype(np.float32)

# xyz_min, xyz_max = xyz.min(axis=0), xyz.max(axis=0)
# src_width = (xyz_max - xyz_min).max()
# xyz_ctr = (xyz_max + xyz_min) / 2
# xyz_scaled = (xyz - xyz_ctr) / src_width * vx_res + vx_res/2

# features = np.ones_like(xyz)
# oc_from_pcl1 = pyoctnet.Octree.create_from_pc(xyz, features, vx_res,vx_res,vx_res, normalize=True, n_threads=n_threads)

# oc_from_pcl2 = pyoctnet.Octree.create_from_pc(xyz_scaled, features, vx_res,vx_res,vx_res, normalize=False, n_threads=n_threads)

# vis.write_ply_pcl('xyz.ply', xyz)
# vis.write_ply_pcl('xyz_scaled.ply', xyz_scaled)
# vis.write_ply_voxels('oc_from_pcl1.ply', oc_from_pcl1.to_cdhw()[0])
# vis.write_ply_voxels('oc_from_pcl2.ply', oc_from_pcl2.to_cdhw()[0])

