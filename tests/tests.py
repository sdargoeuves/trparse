#!/usr/bin/python
import sys
import glob
from unittest import TestCase
sys.path.append("../")
import trparse

FILE_PATTERN = './data/*.txt'



class TracerouteTestCase(TestCase):

    def setUp(self):
        self.filenames = glob.glob(FILE_PATTERN)

    def test_simple(self):
        for filename in self.filenames:
            print(filename)
            with open(filename, 'r') as f:
                tr = trparse.load(f)
                print(f"result:\n{str(tr)}")
