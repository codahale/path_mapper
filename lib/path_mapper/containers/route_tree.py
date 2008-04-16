#!/usr/bin/env python
# -*- coding: utf8 -*-

from path_mapper.routes import parse_path
from prefix_tree import PrefixTree
from route_list import RouteList

class RouteTree(PrefixTree):
  """
    A prefix tree for routes. O(m) matching for paths with m components (e.g.,
    for '/1/2/3', m = 3).
  """
  
  def __init__(self, wildcard='?'):
    super(ListTree, self).__init__(wildcard=wildcard)
  
  def add(self, route):
    """
      Adds route to the tree for each path in route.paths().
    """
    for path in route.paths():
      self.setdefault(parse_path(path), RouteList()).add(route)
  
  def match(self, path):
    """
      Returns the first route matching path. Returns None if no matches were
      found.
    """
    return self.get(parse_path(path), RouteList()).match(path)
  
