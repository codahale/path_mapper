#!/usr/bin/env python
# -*- coding: utf8 -*-
import re, unittest
from helpers import test

from path_mapper.routes import make_route, StaticRoute

class RouteMakingTests(unittest.TestCase):
  
  @test
  def should_make_static_routes(self):
    route = make_route('/home')
    self.assertTrue(isinstance(route, StaticRoute))
  
  @test
  def should_not_be_able_to_make_component_routes(self):
    self.assertRaises(NotImplementedError, make_route, '/posts/:id')
  
  @test
  def should_not_be_able_to_make_regex_routes(self):
    self.assertRaises(NotImplementedError, make_route, re.compile(r'/posts/([\d]{4})/([\d]{2})/([\d]{2})'))

  
def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(RouteMakingTests)
    ]
  )
