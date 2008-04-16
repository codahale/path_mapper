#!/usr/bin/env python
# -*- coding: utf8 -*-

from abstract_route import AbstractRoute

class StaticRoute(AbstractRoute):
  """
    A class managing simple, static routes (e.g., '/about/contact' -> 
    { 'controller': 'about', 'action': 'contact' }).
  """
  
  def __init__(self, path, name=None, options=None):
    super(StaticRoute, self).__init__(path, name=name, options=options)
  
  def match(self, path):
    """
      Returns true if path and the route's path are the same.
    """
    return self.path == path
  
  def paths(self):
    """
      Returns the route's path. Use a dictionary table for (potentially) O(n)
      win.
    """
    return (self.path,)
  
