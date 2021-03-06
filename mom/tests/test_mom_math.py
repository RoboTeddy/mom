#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright 2012 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import unittest2

from mom.math import gcd, lcm, is_prime, _pure_is_prime,\
  generate_random_prime, generate_random_safe_prime, exact_log2
from mom._prime_sieve import make_prime_sieve

class Test__pure_is_prime(unittest2.TestCase):
  def test_pure_is_prime_for_sieves(self):
    for i in [10, 100, 1000, 10000]:
      sieve = make_prime_sieve(i)
      odds = []
      for x in sieve:
        if not _pure_is_prime(x, _sieve=[2, 3]):
          odds.append(x)
      self.assertEqual(odds, [])

  def test_non_prime_by_sieve(self):
    self.assertFalse(_pure_is_prime(100))


class Test_generate_random_prime(unittest2.TestCase):
  def test_generate_random_prime(self):
    for _ in range(100):
      self.assertTrue(is_prime(generate_random_prime(64)))


class Test_generate_random_safe_prime(unittest2.TestCase):
  def test_generate_random_safe_prime(self):
    for _ in range(20):
      self.assertTrue(is_prime(generate_random_safe_prime(32)))


class Test_gcd(unittest2.TestCase):
  def test_gcd(self):
    self.assertEqual(gcd(54, 24), 6)

  def test_gcd_swap(self):
    self.assertEqual(gcd(24, 54), 6)


class Test_lcm(unittest2.TestCase):
  def test_lcm(self):
    self.assertEqual(lcm(4, 6), 12)
    self.assertEqual(lcm(6, 4), 12)
    self.assertEqual(lcm(21, 6), 42)


class Test_exact_log2(unittest2.TestCase):
  def test_ValueError_when_not_found(self):
    self.assertRaises(ValueError, exact_log2, 7)
    self.assertRaises(ValueError, exact_log2, 58)
    self.assertRaises(ValueError, exact_log2, 62)
    self.assertRaises(ValueError, exact_log2, 85)

  def test_ValueError_when_not_negative_or_0(self):
    self.assertRaises(ValueError, exact_log2, 0)
    self.assertRaises(ValueError, exact_log2, -1)
    self.assertRaises(ValueError, exact_log2, -1024)

  def test_correctness(self):
    powers = range(20)
    for power in powers:
      self.assertEqual(exact_log2(1 << power), power)
