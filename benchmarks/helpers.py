#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, timeit

sys.path.insert(0, 'benchmarks')
sys.path.insert(0, 'lib')

all_benchmarks = set()
tsv = 'tsv' in sys.argv

def benchmark(number=10000):
  """
    A decorator which adds the decorated function to the benchmark list.
  """
  def benchmark_decorator(f):
    all_benchmarks.add((f.__name__, number))
    return f
  return benchmark_decorator

def print_benchmarks(results):
  name_length = None
  for module, benchmarks in results.iteritems():
    name_length = max([len(name) for (name, time) in benchmarks] + [name_length])
  for module, benchmarks in sorted(results.iteritems(), key=lambda (x, y): x):
    if tsv:
      for benchmark, time in benchmarks:
        print '%s\t%f' % (benchmark, time)
    else:
      print (module + ' ').ljust(80, '_')
      for benchmark, time in sorted(benchmarks, key=lambda (x, y): x):
        time = ('%0.2f' % time).rjust(10)
        print '- %s %s usec/pass' % (benchmark.ljust(name_length), time)
      print

def run_benchmarks():
  """
    Runs all registered benchmarks.
  """
  results = list()
  for name, number in all_benchmarks:
    t = timeit.Timer('%s()' % name, 'from __main__ import %s' % name)
    results.append((name, 1000000*t.timeit(number=number)/number))
  print_benchmarks({sys.argv[0]: results})
