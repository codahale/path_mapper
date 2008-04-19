#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.containers import PrefixTree

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
    self.assertRaises(KeyError, self.tree.__getitem__, 'blah')
  
  @test
  def should_not_match_on_wildcard_none(self):
    mytree = PrefixTree(wildcard=None)
    mytree['bl?h'] = 40
    self.assertFalse('blah' in mytree)
  
  @test
  def should_raise_error_on_setting_None(self):
    self.assertRaises(ValueError, self.tree.__setitem__, 'yay', None)
  
  @test
  def should_set_default(self):
    self.assertEqual([], self.tree.setdefault('dingo', []))
    self.tree.setdefault('dingo', []).append(1)
    self.tree.setdefault('dingo', []).append(2)
    self.assertEqual([1, 2], self.tree['dingo'])
  
  @test
  def should_raise_error_on_setting_None_as_default(self):
    self.assertRaises(ValueError, self.tree.setdefault, 'yay', None)
  
  @test
  def should_generally_do_what_i_want(self):
    self.tree[('home',)] = '/home'
    self.tree['home', '?'] = '/home/:action'
    self.tree[('?',)] = '/:controller'
    self.tree['?', '?'] = '/:controller/:action'
    self.assertEqual('/:controller/:action', self.tree.get('dingo/majesty'.split('/')))
    self.assertEqual('/home', self.tree.get('home'.split('/')))
  

def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(PrefixTreeTests)
    ]
  )

