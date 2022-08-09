#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_nb_objects(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
