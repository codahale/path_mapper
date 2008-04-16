#!/usr/bin/env python
# -*- coding: utf8 -*-

from errors import NotFoundError

class PathMapper(object):
  def __init__(self):
    super(PathMapper, self).__init__()
    self.static_patterns = dict()
  
  def connect(self, pattern, options):
    self.static_patterns[pattern] = options
  
  def parse(self, path):
    result = self.static_patterns.get(path, None)
    if result:
      return result
    else:
      raise NotFoundError('%s not found' % path)
  
