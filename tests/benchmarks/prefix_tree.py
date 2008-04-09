#!/usr/bin/env python
# -*- coding: utf8 -*-
import random, string, sys
sys.path.insert(0, 'lib')
from path_mapper.prefix_tree import PrefixTree

random.seed = 0xDEADBEEF
random_values = list()
for i in xrange(1, 500):  
  random_values.append(''.join([random.choice(string.letters + string.digits) for i in xrange(random.randint(1, 30))]))

def create_tree():
  tree = PrefixTree()
  for value in random_values:
    tree[value] = 20
  return tree

random_tree = create_tree()

def find_in_tree():
  return 'blah' in random_tree

if __name__=='__main__':
  from timeit import Timer
  
  print "Creating a tree with 500 elements..."
  t = Timer("create_tree()", "from __main__ import create_tree")
  print '200 loops, 3 times each: %f/%f/%f (s)' % tuple(t.repeat(number=200))
  
  print "Finding an element in a tree of 500 elements"
  t = Timer("find_in_tree()", "from __main__ import find_in_tree")
  print '%f (ms)' % (t.timeit() / 1000.0)