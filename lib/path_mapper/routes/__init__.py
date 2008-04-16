#!/usr/bin/env python
# -*- coding: utf8 -*-

from abstract_route import AbstractRoute
from static_route import StaticRoute

def parse_path(path):
  """
    Converts a path string into a tuple of path components.
  """
  return tuple([component for component in path.split('/') if len(component) > 0])

