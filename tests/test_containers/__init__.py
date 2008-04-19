#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest

import test_prefix_tree, test_route_dict, test_route_list, test_route_tree

def suite():
  return unittest.TestSuite((
    test_prefix_tree.suite(),
    test_route_dict.suite(),
    test_route_list.suite(),
    test_route_tree.suite(),
    
  ))