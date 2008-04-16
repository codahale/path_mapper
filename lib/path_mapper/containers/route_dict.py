#!/usr/bin/env python
# -*- coding: utf8 -*-

import warnings

class RouteDict(dict):
  """
    A hash-table dictionary of Routes. O(1) matching.
  """
  
  def add(self, route):
    """
      Adds route to the dictionary. If route is already in the dictionary, drops
      the route while issuing a warning.
    """
    for path in route.paths():
      if path in self:
        warnings.warn('Route collision: %s was dropped for %s' % (repr(route), repr(path)))
      else:
        self[path] = route
  
  def match(self, path):
    """
      Returns the rotue which matches path. Returns False if no route matches.
    """
    return self.get(path, False)
  
