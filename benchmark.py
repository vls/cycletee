#!/usr/bin/env python

import time
import os

def run():
    t0 = time.time()

    os.system('seq 300000 | bin/cycletee -n')

    total = time.time() - t0
    total *= 1000
    print "Cost time = %f" % total 
    return total



def main():
    arr = []
    for i in xrange(10):
        arr.append(run())

    print "Avg time = %f" % (sum(arr) / len(arr))




if __name__ == '__main__':
    main()

