#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest

import test_path_parsing, test_route_making, test_static_route

def suite():
  return unittest.TestSuite((
    test_path_parsing.suite(),
    test_route_making.suite(),
    test_static_route.suite(),
  ))