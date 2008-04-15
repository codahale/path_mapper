#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, unittest, warnings
from helpers import test
from pprint import pprint

from path_mapper.containers import PrefixTree, RouteTree, RouteList, RouteDict
from path_mapper.routes import StaticRoute

class PrefixTreeTests(unittest.TestCase):
  
  def setUp(self):
    self.tree = PrefixTree()
  
  @test
  def should_get_set_values(self):
    self.tree['blah'] = 300
    self.assertEqual(300, self.tree['blah'])
  
  @test
  def should_return_None_for_missing_values(self):
    self.assertEqual(None, self.tree.get('blah'))
  
  @test
  def should_return_default_for_missing_values(self):
    self.assertEqual([], self.tree.get('blah', []))
  
  @test
  def should_get_set_values_with_wildcards(self):
    self.tree['bla?ee'] = 400
    self.assertEqual(400, self.tree['blaoee'])
    self.assertEqual(400, self.tree['blalee'])
  
  @test
  def should_work_with_lists(self):
    self.tree[1, 2, 3, '?'] = 300
    self.assertEqual(300, self.tree[1, 2, 3, 4])
  
  @test
  def should_have_membership_test(self):
    self.tree['blah'] = 400
    self.assertTrue('blah' in self.tree)
    self.assertFalse('bla' in self.tree)
  
  @test
  def should_raise_error_on_missing_key(self):
    try:
      self.tree['blah']
    except KeyError, e:
      self.assertEqual('blah', e.message)
  
  @test
  def should_not_match_on_wildcard_none(self):
    mytree = PrefixTree(wildcard=None)
    mytree['bl?h'] = 40
    self.assertFalse('blah' in mytree)
  
  @test
  def should_raise_error_on_setting_None(self):
    try:
      self.tree['yay'] = None
      self.fail("should have raised a ValueError but didn't")
    except ValueError, e:
      self.assertEqual('None is not a valid value', e.message)
  
  @test
  def should_set_default(self):
    self.assertEqual([], self.tree.setdefault('dingo', []))
    self.tree.setdefault('dingo', []).append(1)
    self.tree.setdefault('dingo', []).append(2)
    self.assertEqual([1, 2], self.tree['dingo'])
  
  @test
  def should_raise_error_on_setting_None_as_default(self):
    try:
      self.tree.setdefault('yay', None)
      self.fail("should have raised a ValueError but didn't")
    except ValueError, e:
      self.assertEqual('None is not a valid default', e.message)
  
  @test
  def should_generally_do_what_i_want(self):
    self.tree[('home',)] = '/home'
    self.tree['home', '?'] = '/home/:action'
    self.tree[('?',)] = '/:controller'
    self.tree['?', '?'] = '/:controller/:action'
    self.assertEqual('/:controller/:action', self.tree.get('dingo/majesty'.split('/')))
    self.assertEqual('/home', self.tree.get('home'.split('/')))
  
class RouteTreeTests(unittest.TestCase):
  # TODO write tests
  pass
  

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
      unittest.makeSuite(PrefixTreeTests),
      unittest.makeSuite(RouteTreeTests),
      unittest.makeSuite(RouteListTests),
      unittest.makeSuite(RouteDictTests)
    ]
  )

if __name__ == '__main__':
  unittest.main()