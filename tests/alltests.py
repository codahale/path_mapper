#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest

import test_path_mapper, test_prefix_tree

def test_suite():
  return unittest.TestSuite((
    test_path_mapper.suite(),
    test_prefix_tree.suite()
  ))

if __name__ == '__main__':
  unittest.main(defaultTest='test_suite')