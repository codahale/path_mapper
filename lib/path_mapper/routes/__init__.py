#!/usr/bin/env python
# -*- coding: utf8 -*-

from re             import _pattern_type as regular_expression

from abstract_route import AbstractRoute
from static_route   import StaticRoute

def parse_path(path):
  """
    Converts a path string into a tuple of path components.
  """
  return tuple([component for component in path.split('/') if len(component) > 0])

def make_route(path, name=None, options=None):
  """
    Given a path and an optional name and options, returns a route object.
  """
  if isinstance(path, regular_expression):
    raise NotImplementedError, 'regular expression routes not implemented yet'
  elif ':' in path:
    raise NotImplementedError, 'component routes not implemented yet'
  else:
    return StaticRoute(path, name=name, options=options)
  
