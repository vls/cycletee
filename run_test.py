#!/usr/bin/env python

import unittest
import os
import subprocess
from subprocess import Popen, PIPE

def file_get_contents(fname):
    return (line.rstrip(os.linesep) for line in open(fname, 'r').readlines())

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

    def test_binary(self):
        s = 'abc' + ''.join((chr(i) for i in xrange(256)))
        with open('input.txt', 'w') as wf:
            wf.write(s)

        os.system("cat input.txt | bin/cycletee 1.txt > /dev/null")
        lines = file_get_contents("1.txt")
        expect_arr = s.split('\n')
        ae = self.assertEqual
        for i, line in enumerate(lines):
            ae(line, expect_arr[i])

    def test_nostdout(self):

        p1 = Popen(["echo", "123"], stdout=PIPE)
        p2 = Popen(["bin/cycletee", "-n"], stdin = p1.stdout, stdout = PIPE, cwd = os.getcwd())
        output = p2.communicate()[0]
        ae = self.assertEqual
        ae(output, '')




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

