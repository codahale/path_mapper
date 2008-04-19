#!/usr/bin/env python
# -*- coding: utf8 -*-
import random, string, sys
from helpers import benchmark, run_benchmarks
from path_mapper.containers import PrefixTree

random.seed = 0xDEADBEEF
random_values = list()
for i in xrange(1, 500):  
  random_values.append(''.join([random.choice(string.letters + string.digits) for i in xrange(random.randint(1, 30))]))

@benchmark(100)
def create_tree():
  tree = PrefixTree()
  for value in random_values:
    tree[value] = 20
  return tree

random_tree = create_tree()
random_value = random.choice(random_values)

@benchmark(100000)
def find_in_tree():
  return random_value in random_tree

if __name__ == '__main__':
  run_benchmarks()