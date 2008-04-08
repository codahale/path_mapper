#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
  A module containing PrefixTree.
"""

class PrefixTree(object):
  """
    A prefix tree (a.k.a. "trie") implementation which supports wildcard
    matching.
  """
  
  def __init__(self, wildcard='?'):
    """
      Creates a new instance of PrefixTree.
      
      Accepts wildcard as an optional parameter. If wildcard is None, no
      wildcard matching will be performed.
    """
    super(PrefixTree, self).__init__()
    self.root = [None, dict()]
    self.wildcard = wildcard
  
  def get(self, key, default=None):
    """
      Returns the value associated with the key, or default if none exists.
      default defaults to None.
      
        >>> tree.get('known')
        'yay'
        >>> tree.get('unknown')
        >>> tree.get('unknown', 0)
        0
    """
    node = self.root
    for element in key:
      if element in node[1]:
        node = node[1][element]
      elif self.wildcard and (self.wildcard in node[1]):
        node = node[1][self.wildcard]
      else:
        return default
    return node[0]
  
  def __getitem__(self, key):
    """
      Returns the value associated with the key, or raises a KeyError if none
      exists.
    """
    value = self.get(key)
    if value == None:
      raise KeyError, key
    else:
      return value
  
  def __setitem__(self, key, value):
    """
      Associates value with key. If value is None, raises a ValueError.
    """
    if value == None:
      raise ValueError, 'None is not a valid value'
    node = self.root
    for element in key:
      node = node[1].setdefault(element, [None, {}])
    node[0] = value
  
  def __contains__(self, key):
    """
      Returns True if key exists in the tree, False otherwise.
    """
    return self.get(key) != None
  
