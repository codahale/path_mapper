#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, timeit

sys.path.insert(0, 'benchmarks')
sys.path.insert(0, 'lib')

all_benchmarks = set()

def benchmark(number=10000):
  """
    A decorator which adds the decorated function to the benchmark list.
  """
  def benchmark_decorator(f):
    all_benchmarks.add((f.__name__, number))
    return f
  return benchmark_decorator


def run_benchmarks():
  """
    Runs all registered benchmarks.
  """
  results = list()
  for name, number in all_benchmarks:
    t = timeit.Timer('%s()' % name, 'from __main__ import %s' % name)
    results = 1000000*t.timeit(number=number)/number
    if 'tsv' in sys.argv:
      print '%s\t%s' % (name, results)
    else:
      print '%s: %.02f usec/pass' % (name, results)
  
