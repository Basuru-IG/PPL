import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """class Program{ const a, b, c: int = 3, 4, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
