#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.prefix_tree import PrefixTree

class PrefixTreeTests(unittest.TestCase):
  def setUp(self):
    self.tree = PrefixTree()
  
  @test
  def should_get_set_values(self):
    self.tree['blah'] = 300
    self.assertEqual(300, self.tree['blah'])
  
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
  
  
def suite():
  return unittest.makeSuite(PrefixTreeTests)

if __name__ == '__main__':
  unittest.main()