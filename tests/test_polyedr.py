import unittest
from unittest.mock import patch, mock_open
import pytest
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.currentPolyedr = Polyedr(f"data/test1.geom")
        self.currentPolyedr2 = Polyedr(f"data/test2.geom")

    def test_num_vertexes(self):
        self.assertEqual(len(self.currentPolyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.currentPolyedr.facets), 6)

    def test_num_edges(self):
        self.assertEqual(len(self.currentPolyedr.edges), 12)

    def test_areas_facets1(self):
        assert self.currentPolyedr.calc() == pytest.approx(0.64, abs=1e-6)

    def test_areas_facets2(self):
        assert self.currentPolyedr2.calc() == pytest.approx(0, abs=1e-6)
