#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper import *

class PathMapperTests(unittest.TestCase):
  @test
  def should_have_tests(self):
    pass
  
def suite():
  return unittest.makeSuite(PathMapperTests)

if __name__ == '__main__':
  unittest.main()