#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.containers import RouteList
from path_mapper.routes import StaticRoute

class RouteListTests(unittest.TestCase):
  
  def setUp(self):
    self.route1 = StaticRoute('/home')
    self.route2 = StaticRoute('/home/about', name='Primero')
    self.route3 = StaticRoute('/home/about', name='Segundo')
    self.list = RouteList()
    self.list.add(self.route1)
    self.list.add(self.route2)
    self.list.add(self.route3)
  
  @test
  def should_match_first_route(self):
    self.assertEqual(self.route2, self.list.match('/home/about'))

def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(RouteListTests)
    ]
  )

