#!/usr/bin/env python
# -*- coding: utf8 -*-

class AbstractRoute(object):
  """
    An abstract class wrapping the basics of path matching. Routes do two
    things:
    
      1. Register themselves with various containers as being able to match
         paths which match particular broad patterns (e.g., '/posts/?').
      
      2. Determine whether or not a path matches exactly, and if it does,
         parses it into a set of options.
  """
  
  def __init__(self, path, name=None, options=None):
    super(AbstractRoute, self).__init__()
    self.static = False
    self.path = path
    self.name = name
    if options:
      self.options = options
    else:
      self.options = dict()
  
  def __repr__(self):
    return '<Route path=%s, name=%s, options=%s>' % (repr(self.path), repr(self.name), repr(self.options))
  
  def match(self, path):
    """
      Returns True if path matches the route. Returns False, otherwise.
    """
    raise NotImplementedError, 'Route is an abstract class.'
  
  def paths(self):
    """
      Returns a set of paths which this route should respond to.
    """
    raise NotImplementedError, 'Route is an abstract class.'
  
