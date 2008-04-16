#!/usr/bin/env python
# -*- coding: utf8 -*-

class RouteList(list):
  """
    A simple array of Routes. O(n) matching.
  """
  
  def add(self, route):
    """
      Appends route to the end of the list.
    """
    self.append(route)
  
  def match(self, path):
    """
      Returns the first route which matches path. Returns False if no routes
      match. O(n).
    """
    for route in self:
      if route.match(path):
        return route
    return False
  
