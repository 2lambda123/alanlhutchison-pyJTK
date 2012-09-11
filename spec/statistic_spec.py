#!/usr/bin/epython

import sys
import os.path

p = os.path.realpath(__file__)
q = os.path.split(os.path.dirname(p))
sys.path.append(os.path.join(q[0], "src"))
del p, q # keep globals clean

import unittest
import numpy as np

import statistic

class ScoreFactorySpec(unittest.TestCase):
    def setUp(self):
        self.scorer = statistic.ScoreFactory()
    
    def test_score_trivial(self):
        data = np.arange(12)
        ref = np.ones(12)
        expect = 0.0
        actual = self.scorer.score(data,ref)
        self.assertEqual(expect, actual)
    
    def test_score(self):
        data = np.array([1,3,2,4],dtype='float')
        ref = np.arange(4)
        expect = 4.0
        actual = self.scorer.score(data,ref)
        self.assertEqual(expect, actual)
    
    def test_tau_vector(self):
        data = np.array([1,3,5,7,9,2,4,6,8,10],dtype='float')
        expect = np.array([
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,-1,
                1, 1, 1, 1, 1, 1,-1,-1, 1, 1, 1, 1,-1,
               -1,-1, 1, 1,-1,-1,-1,-1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1
                ],dtype='float')
        actual = self.scorer.tau_vector(data)
        for p in zip(expect, actual):
            self.assertEqual(p[0],p[1])
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()