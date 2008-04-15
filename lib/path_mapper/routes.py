#!/usr/bin/env python
# -*- coding: utf8 -*-

class Route(object):
  """
    An abstract class wrapping the basics of path matching. Routes do two
    things:
    
      1. Register themselves with various containers as being able to match
         paths which match particular broad patterns (e.g., '/posts/?').
      
      2. Determine whether or not a path matches exactly, and if it does,
         parses it into a set of options.
  """
  
  def __init__(self, path, name=None, options=None):
    super(Route, self).__init__()
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
  

class StaticRoute(Route):
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
  
