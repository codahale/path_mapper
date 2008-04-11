#!/usr/bin/env python
# -*- coding: utf8 -*-
import unittest

import test_path_mapper, test_containers

def test_suite():
  return unittest.TestSuite((
    test_path_mapper.suite(),
    test_containers.suite()
  ))

if __name__ == '__main__':
  unittest.main(defaultTest='test_suite')