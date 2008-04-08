#!/usr/bin/env python
# -*- coding: utf8 -*-

class PathMapper(object):
  def __init__(self):
    super(PathMapper, self).__init__()
    self.patterns = dict()
  
  def connect(self, pattern, options):
    self.patterns[pattern] = options
  
  def parse(self, path):
    return self.patterns[path]