#!/usr/bin/env python3
import sys
import argparse
import math


def main(ns):
    aspect = ns.high / ns.wide
    a = 1
    b = aspect
    c = math.sqrt((a*a) + (b*b))
    A = math.asin(a/c)
    _c = ns.size
    _a = math.sin(A) * _c
    _b = math.cos(A) * _c
    print("width = {0:.2f}   height = {1:.2f}".format(_a, _b))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default=float(9.0), action='store',
                        dest='high', type=float, help="pixels high")
    parser.add_argument('-w', default=float(16.0), action='store',
                        dest='wide', type=float, help="pixels wide")
    parser.add_argument('-s', default=float(24.0), action='store',
                        dest='size', type=float, help="physical diagonal")
    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main(parse_args()))
