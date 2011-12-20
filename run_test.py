#!/usr/bin/env python

import unittest
import os

def file_get_contents(fname):
    return open(fname, 'r').readlines()

class TestCycletee(unittest.TestCase):
    def test_10line(self):
        os.system('seq 10 | bin/cycletee 1.txt 2.txt 3.txt > /dev/null')
        lines = file_get_contents('1.txt')
        expect_arr = [1, 4, 7, 10]

        ae = self.assertEqual
        for i, line in enumerate(lines):
            ae(line.strip('\r\n'),  str(expect_arr[i]))



    def test_incomplete_line(self):
        os.system("echo -n 'test' | bin/cycletee 1.txt > /dev/null")
        lines = file_get_contents('1.txt')
        expect_arr = ['test']

        ae = self.assertEqual
        for i, line in enumerate(lines):
            ae(line, expect_arr[i])


    def test_large_line(self):
        s = 's' * 16384
        with open('input.txt', 'w') as wf:
            wf.write(s)

        os.system("cat input.txt | bin/cycletee 1.txt > /dev/null")
        lines = file_get_contents("1.txt")
        expect_arr = [s]
        ae = self.assertEqual
        for i, line in enumerate(lines):
            ae(line, expect_arr[i])


    def tearDown(self):
        file_list = [
                "1.txt",
                "2.txt",
                "3.txt",
                "input.txt",
                ]

        os.system("rm -f %s 2>/dev/null" % (' '.join(file_list)))





if __name__ == '__main__':
    unittest.main()

