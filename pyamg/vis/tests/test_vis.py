""" Try creating a point and primal aggregate view for a C/F splitting and
simple aggregation, respectively."""

from pyamg.testing import *

import tempfile
import os

from scipy.sparse import csr_matrix
from numpy import array, ones, uint32

from pyamg.vis import coarse_grid_vis, write_vtu

class TestVis(TestCase):
    def setUp(self):
        self.file_name = tempfile.mktemp()

    def tearDown(self):
        os.remove(self.file_name)

    def test_tri_points(self):
        Vert = array([[0.0,0.0],
                      [1.0,0.0],
                      [2.0,0.0],
                      [0.0,1.0],
                      [1.0,1.0],
                      [2.0,1.0],
                      [0.0,2.0],
                      [1.0,2.0],
                      [2.0,2.0],
                      [0.0,3.0],
                      [1.0,3.0],
                      [2.0,3.0]])

        E2V = array([[0,4,3],
                     [0,1,4],
                     [1,5,4],
                     [1,2,5],
                     [3,7,6],
                     [3,4,7],
                     [4,8,7],
                     [4,5,8],
                     [6,10,9],
                     [6,7,10],
                     [7,11,10],
                     [7,8,11]],dtype=uint32)

        row  = array([0,1,2,3,4,5,6,7,8,9,10,11])
        col  = array([1,0,1,1,0,1,0,1,0,1, 0, 1])
        data = ones((1,12),dtype=uint32).ravel()

        Agg = csr_matrix((data,(row,col)),shape=(12,2))

        coarse_grid_vis(self.file_name, 
                        Vert=Vert, E2V=E2V, Agg=Agg,
                        mesh_type='tri', A=None, plot_type='points')

    def test_tri_primal(self):
        Vert = array([[0.0,0.0],
                      [1.0,0.0],
                      [2.0,0.0],
                      [0.0,1.0],
                      [1.0,1.0],
                      [2.0,1.0],
                      [3.0,1.0],
                      [0.0,2.0],
                      [1.0,2.0],
                      [2.0,2.0],
                      [3.0,2.0],
                      [4.0,2.0],
                      [0.0,3.0],
                      [1.0,3.0],
                      [2.0,3.0],
                      [3.0,3.0],
                      [4.0,3.0],
                      [5.0,3.0]])

        E2V = array([[0,4,3],
                     [0,1,4],
                     [1,5,4],
                     [1,2,5],
                     [2,6,5],
                     [3,8,7],
                     [3,4,8],
                     [4,9,8],
                     [4,5,9],
                     [5,10,9],
                     [5,6,10],
                     [6,11,10],
                     [7,13,12],
                     [7,8,13],
                     [8,14,13],
                     [8,9,14],
                     [9,15,14],
                     [9,10,15],
                     [10,16,15],
                     [10,11,16],
                     [11,17,16]],dtype=uint32)

        row  = array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        col  = array([0,1,3,0,1,1,3,0,0,1, 3, 4, 0, 0, 0, 2, 4, 4])
        data = ones((1,18),dtype=uint32).ravel()

        Agg = csr_matrix((data,(row,col)),shape=(18,5))

        coarse_grid_vis(self.file_name, 
                        Vert=Vert, E2V=E2V, Agg=Agg,
                        mesh_type='tri', A=None, plot_type='primal')

