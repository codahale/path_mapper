#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.routes import parse_path

class PathParsingTests(unittest.TestCase):
  
  @test
  def should_turn_paths_into_tuples(self):
    self.assertEqual(('home', 'index', 'weeble'), parse_path('/home/index/weeble'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('/home/index/weeble/'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('home/index/weeble'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('home/index/weeble/'))

  
def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(PathParsingTests),
    ]
  )