#!/usr/bin/env python
# -*- coding: utf8 -*-
import re, unittest
from helpers import test

from path_mapper.routes import parse_path, make_route, StaticRoute

class ParsingTests(unittest.TestCase):
  
  @test
  def should_turn_paths_into_tuples(self):
    self.assertEqual(('home', 'index', 'weeble'), parse_path('/home/index/weeble'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('/home/index/weeble/'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('home/index/weeble'))
    self.assertEqual(('home', 'index', 'weeble'), parse_path('home/index/weeble/'))
  

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
      unittest.makeSuite(ParsingTests),
      unittest.makeSuite(StaticRouteTests),
      unittest.makeSuite(RouteMakingTests)
    ]
  )

if __name__ == '__main__':
  unittest.main()