#!/usr/bin/env python
# -*- coding: utf8 -*-

from containers import RouteDict
from errors     import NotFoundError
from routes     import make_route, StaticRoute

class PathMapper(object):
  def __init__(self):
    super(PathMapper, self).__init__()
    self.static_patterns = RouteDict()
  
  def connect(self, path, name=None, options=None):
    route = make_route(path, name=name, options=options)
    if route.static:
      self.static_patterns.add(route)
  
  def parse(self, path):
    result = self.static_patterns.match(path)
    if result:
      return result.options
    else:
      raise NotFoundError('%s not found' % path)
  
