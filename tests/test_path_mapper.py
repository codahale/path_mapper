#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper import PathMapper
from path_mapper.errors import NotFoundError

class PathMapperTests(unittest.TestCase):
  def setUp(self):
    self.path_mapper = PathMapper()
    self.path_mapper.connect('/home', options={ 'controller': 'home', 'action': 'weebles' })
  
  @test
  def should_parse_a_static_url(self):
    self.assertEqual({ 'controller': 'home', 'action': 'weebles' }, self.path_mapper.parse('/home'))
  
  @test
  def should_raise_an_exception_if_parsing_an_unknown_static(self):
    try:
      self.path_mapper.parse('/dingo')
      self.fail('Should have raised a PathNotFoundError')
    except NotFoundError, e:
      self.assertEqual('/dingo not found', e.message)
  
def suite():
  return unittest.makeSuite(PathMapperTests)

if __name__ == '__main__':
  unittest.main()