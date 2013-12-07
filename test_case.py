#!/usr/bin/env python

import argparse
import random
import time

argparse.ArgumentParser(description="""
Output test case for Paiza Online Hachathon.
https://paiza.jp/poh/ec-campaign/

# Conditions

- N (1<=N<=200000)        -> Number of items
- D (1<=D<=75)            -> Number of days for campaign
- p_i (10<=p_i<=1000000)  -> Item price
- m_j (10<=m_j<=1000000)  -> Campaign price

# Format

N D
p_0
p_1
...
p_N
m_0
m_1
...
m_N
""", formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()

def main():
    n = N()
    d = D()

    print('%d %d' % (n, d))

    for i in range(n):
        print(p_i())

    for j in range(d):
        print(m_j())

def N():
    return _randint(1, 200000)

def D():
    return _randint(1, 75)

def p_i():
    return _randint(10, 1000000)

def m_j():
    return _randint(10, 1000000)

def _randint(a, b):
    random.seed(time.time())
    return random.randint(a, b)


if __name__ == '__main__':
    main()
