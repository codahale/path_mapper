#!/usr/bin/env python
# -*- coding: utf8 -*-

from path_mapper.routes import parse_path
from prefix_tree import PrefixTree
from route_list import RouteList

class RouteTree(PrefixTree):
  def __init__(self, wildcard='?'):
    super(ListTree, self).__init__(wildcard=wildcard)
  
  def add(self, route):
    # TODO add a real check here -- does paths() make any sense?
    for path in route.paths():
      self.setdefault(parse_path(path), RouteList()).add(route)
  
  def match(self, path):
    return self.get(parse_path(path), RouteList()).match(path)
  

