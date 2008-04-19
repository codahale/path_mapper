#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
  Locates, runs, and prints the collected results from all benchmarks.
  
  python benchmarks/run.py

"""


import os, helpers

def find_and_run_benchmarks():
  benchmark_results = dict()
  for root, dirname, files in os.walk('benchmarks'):
    for f in files:
      if f[-14:] == '_benchmarks.py':
        module = os.path.join(root, f)
        benchmark_results[module] = list()
        for result in os.popen('python %s tsv' % os.path.join(root, f)):
          name, time = result.strip().split('\t')
          benchmark_results[module].append((name, float(time)))
  return benchmark_results

if __name__ == '__main__':
  helpers.print_benchmarks(find_and_run_benchmarks())