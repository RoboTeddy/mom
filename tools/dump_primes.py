#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path[0:0] = [
    os.curdir,
]

from mom._prime_sieve import make_prime_sieve
from pprint import pprint

header = """\
#/usr/bin/env python
# -*- coding: utf-8 -*-
# Automatically-generated by dump_primes.py
#
# Pre-computated lookups are faster than calculation at runtime.
#

"""
print(header)

a = set(make_prime_sieve(9999))

sys.stdout.write("sieve = ")
pprint(a)

