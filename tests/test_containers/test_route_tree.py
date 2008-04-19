#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest
from helpers import test

from path_mapper.containers import RouteTree

class RouteTreeTests(unittest.TestCase):
  # TODO write tests
  pass


def suite():
  return unittest.TestSuite(
    [
      unittest.makeSuite(RouteTreeTests)
    ]
  )

