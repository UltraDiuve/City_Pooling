"""
Unit tests for the geography module
"""

from src.geography import geography
import numpy as np


class TestGeography(object):

    def test_dist(self):
        assert geography.dist([0, 0], [3, 4]) == 5

    def test_permute_array(self):
        assert np.all(
                geography.permute_array(np.array([[1, 2], [3, 4]]), [1, 0]) ==
                np.array([[4, 3], [2, 1]]))

    def test_geography_constructor(self):
        geography.Geography(16)
        geography.Geography(
                3, cities_coordinates=np.array([[0, 1, 2], [0, 0, 0]]))
        geography.Geography(2, cities_names=np.array(['A', 'B', 'C']))

    def test_geography_dist_matrix_init(self):
        geo = geography.Geography(
                3, cities_coordinates=np.array([[0, 1, 2], [0, 0, 0]]))
        assert np.all(
                geo.dist_matrix == np.array([[0, 1, 2], [1, 0, 1], [2, 1, 0]]))

    def test_geography_show(self):
        geography.Geography(4).show(show_names=True)
        geography.Geography(4).show_config({0: [0, 1], 1: [2, 3]})
