#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest

import test_path_mapper, test_containers, test_routes


def suite():
  return unittest.TestSuite((
    test_path_mapper.suite(),
    test_containers.suite(),
    test_routes.suite()
  ))

if __name__ == '__main__':
  unittest.main(defaultTest='suite')