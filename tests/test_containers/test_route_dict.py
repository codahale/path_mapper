#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest, warnings
from helpers import test

from path_mapper.containers import RouteDict
from path_mapper.routes import StaticRoute

class RouteDictTests(unittest.TestCase):
  
  def setUp(self):
    self.route1 = StaticRoute('/home')
    self.route2 = StaticRoute('/home/about', name='Primero')
    self.dict = RouteDict()
    self.dict.add(self.route1)
    self.dict.add(self.route2)
  
  @test
  def should_match_routes(self):
    self.assertEqual(self.route1, self.dict.match('/home'))
  
  @test
  def should_warn_and_drop_on_path_collision(self):
    self.warnings = list()
    def warn(msg):
      self.warnings.append(msg)
    try:
      old_warn = warnings.warn
      warnings.warn = warn
      self.dict.add(StaticRoute('/home', options={ 'blah': True }))
      self.assertEqual(["Route collision: <Route path='/home', name=None, options={'blah': True}> was dropped for '/home'"], self.warnings)
      self.assertEqual(self.route1, self.dict.match('/home'))
    finally:
      warnings.warn = old_warn
  

def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(RouteDictTests)
    ]
  )

