#!/usr/bin/env python

"""Tests for `create_distance_maps_adjacency_matrix` package."""

import os
import numpy as np
from scipy.spatial import distance
import unittest

class TestCreate(unittest.TestCase):
    """Tests for `create_distance_maps_adjacency_matrix` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_create_distance_ok(self):
        """
        Test calculation of distance matrix
        """
        test_array = np.array([[3, 2, 4],
                               [3, 0, 1],
                               [5, 3, 2]])
        test_distance_array = np.array([[0, np.sqrt((3-3)**2 + (2-0)**2 + (4-1)**2), np.sqrt((3-5)**2 + (2-3)**2 + (4-2)**2)],
                                        [np.sqrt((3-3)**2 + (0-2)**2 + (1-4)**2), 0, np.sqrt((3-5)**2 + (0-3)**2 + (1-2)**2)],
                                        [np.sqrt((5-3)**2 + (3-2)**2 + (2-4)**2), np.sqrt((5-3)**2 + (3-0)**2 + (2-1)**2), 0]])

        calculate_distances = distance.pdist(test_array, 'euclidean')
        make_square = distance.squareform(calculate_distances)

        test_distance_list = []
        for i in range(test_distance_array.shape[0]):
            for j in range(test_distance_array.shape[1]):
                test_distance_list.append(test_distance_array[i,j])

        test_makesquare_list = []
        for m in range(make_square.shape[0]):
            for n in range(make_square.shape[1]):
                test_makesquare_list.append(make_square[m,n])

        for i in range(0, len(test_distance_list)):
            assert test_distance_list[i] == test_makesquare_list[i]

        for i in range(0, len(test_makesquare_list)):
            assert test_makesquare_list[i] == test_distance_list[i]

        test_1 = np.array([[1, 2, 3],
                           [4, 5, 6]])
        test_2 = np.array([[1, 2, 3],
                           [4, 5, 6]])

        test_1_list = []
        for i in range(test_1.shape[0]):
            for j in range(test_1.shape[1]):
                test_1_list.append(test_1[i,j])

        test_2_list = []
        for m in range(test_2.shape[0]):
            for n in range(test_2.shape[1]):
                test_2_list.append(test_2[m,n])

        for i in range(0, len(test_1_list)):
            assert test_1_list[i] == test_2_list[i]

    def test_002_coordinate_calculation(self):
        """
        Test calculation of coordinates from distance matrix
        """
        test_array = np.random.randint(10, size=(100, 3))

        calculate_distances = distance.pdist(test_array, 'euclidean')
        distance_map = distance.squareform(calculate_distances)

        print(distance_map)

        structure = np.zeros(distance_map.shape)
        for i in range(0,distance_map.shape[0]):
            for j in range(0,distance_map.shape[1]):
                structure[i,j] = 1/2 * (distance_map[i,0]**2 + distance_map[0,j]**2 - distance_map[i,j]**2)


        w, v = np.linalg.eigh(structure)
        nb_components = 3 # 3D
        ZZ = np.matmul(v[:,-nb_components:], np.diag(np.sqrt(w[-nb_components:])))

        ZZ_distances = distance.pdist(ZZ, 'euclidean')
        ZZ_distance_map = distance.squareform(ZZ_distances)

        print('\n')
        print(ZZ_distance_map)
        print(type(ZZ_distance_map))

        self.assertTrue(np.allclose(distance_map, ZZ_distance_map))
