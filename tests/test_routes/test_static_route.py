#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.routes import StaticRoute

class StaticRouteTests(unittest.TestCase):
  
  def setUp(self):
    self.route = StaticRoute('/home', name='home', options={ 'controller': 'pages', 'action': 'index' })
  
  @test
  def should_have_a_name(self):
    self.assertEqual('home', self.route.name)
  
  @test
  def should_have_options(self):
    self.assertEqual({ 'controller': 'pages', 'action': 'index' }, self.route.options)
  
  @test
  def should_match_paths(self):
    self.assertTrue(self.route.match('/home'))
    self.assertFalse(self.route.match('dingo/weeble'))
    self.assertFalse(self.route.match('/blah'))
  
  @test
  def should_have_paths(self):
    self.assertEqual(('/home',), self.route.paths())
  
def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(StaticRouteTests)
    ]
  )