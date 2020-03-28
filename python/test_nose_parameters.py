'''
 subset taken from readme in https://github.com/wolever/parameterized 
 subject to David Wolever's simplified BSD license 
 https://github.com/wolever/parameterized/blob/master/LICENSE.txt 
 '''

from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class

import unittest
import math

class TestMathUnitTest(unittest.TestCase):
   @parameterized.expand([
       ("negative", -1.5, -2.0),
       ("integer", 1, 1.0),
       ("large fraction", 1.6, 1),
   ])
   def test_floor(self, name, input, expected):
       assert_equal(math.floor(input), expected)

@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
   (1, 2, 3, 2),
   (5, 5, 10, 25),
])
class TestMathClass(unittest.TestCase):
   def test_add(self):
      assert_equal(self.a + self.b, self.expected_sum)

   def test_multiply(self):
      assert_equal(self.a * self.b, self.expected_product)

@parameterized_class([
   { "a": 3, "expected": 2 },
   { "b": 5, "expected": -4 },
])
class TestMathClassDict(unittest.TestCase):
   a = 1
   b = 1

   def test_subtract(self):
      assert_equal(self.a - self.b, self.expected)