#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper import *

class PathMapperTests(unittest.TestCase):
  def setUp(self):
    self.path_mapper = PathMapper()
    self.path_mapper.connect('/home', { 'controller': 'home', 'action': 'weebles' })
  
  @test
  def should_parse_a_static_url(self):
    self.assertEqual({ 'controller': 'home', 'action': 'weebles' }, self.path_mapper.parse('/home'))
  
def suite():
  return unittest.makeSuite(PathMapperTests)

if __name__ == '__main__':
  unittest.main()