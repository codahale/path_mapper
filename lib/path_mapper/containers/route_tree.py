#!/usr/bin/env python
# -*- coding: utf8 -*-

from prefix_tree import PrefixTree

class RouteTree(PrefixTree):
  def __init__(self, wildcard='?'):
    super(ListTree, self).__init__(wildcard=wildcard)
  
  def add(self, route):
    # TODO add a real check here -- does paths() make any sense?
    for path in route.paths():
      self.setdefault(path, RouteList()).add(route)
  
  def match(self, path):
    return self.get(path, RouteList()).match(path)
  

