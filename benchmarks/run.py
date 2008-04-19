#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
  Locates, runs, and prints the collected results from all benchmarks.
  
  python benchmarks/run.py

"""


import os

def find_and_run_benchmarks():
  benchmark_results = dict()
  for root, dirname, files in os.walk(os.path.join(os.path.curdir, 'benchmarks')):
    for f in files:
      if f[-14:] == '_benchmarks.py':
        module = f[:-14]
        benchmark_results[module] = list()
        for result in os.popen('python %s tsv' % os.path.join(root, f)):
          name, time = result.strip().split('\t')
          benchmark_results[module].append((name, float(time)))
  return benchmark_results

def print_results(results):
  # name_length = max(len(name) for (name, time) in [b for (m, b) in results.iteritems()])
  name_length = None
  for module, benchmarks in results.iteritems():
    name_length = max([len(name) for (name, time) in benchmarks] + [name_length])
  for module, benchmarks in sorted(results.iteritems(), key=lambda (x, y): x):
    print (module + ' ').ljust(80, '_')
    for benchmark, time in sorted(benchmarks, key=lambda (x, y): x):
      print '> %s = %f' % (benchmark.ljust(name_length), time)
    print

if __name__ == '__main__':
  print_results(find_and_run_benchmarks())