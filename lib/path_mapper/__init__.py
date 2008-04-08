#!/usr/bin/env python
# -*- coding: utf8 -*-

class NotFoundError(Exception): pass


class PathMapper(object):
  def __init__(self):
    super(PathMapper, self).__init__()
    self.static_patterns = dict()
  
  def connect(self, pattern, options):
    if self.__is_static_pattern(pattern):
      self.static_patterns[pattern] = options
  
  def parse(self, path):
    result = self.static_patterns.get(path, None)
    if result:
      return result
    else:
      raise NotFoundError('%s not found' % path)
  
  def __is_static_pattern(self, pattern):
    return True