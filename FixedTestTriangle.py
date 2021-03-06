# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from FixedTriangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,5),'NotATriangle','2,2,5 should not be a triangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(3,3,7),'NotATriangle','3,3,7 should not be a triangle')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(2,1,2),'Isoceles','2,1,2 should be isoceles')
        
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be isoceles')
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

