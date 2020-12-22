from Lab10.stack_lib import *
import unittest


class Test(unittest.TestCase):

  def setUp(self):
    self.stack = Stack()

  def test_str(self):
    self.assertEqual(str(self.stack), '[]')

  def test_eq(self):
    self.assertEqual(self.stack, Stack())

  def test_is_empty(self):
    self.assertEqual(self.stack.is_empty(), True)

  def test_is_full(self):
    self.assertEqual(self.stack.is_full(), False)

  def test_pop(self):
    with self.assertRaises(ValueError):
      Stack().pop()
    self.stack.push(10)
    self.assertEqual(self.stack.pop(), 10)

  def test_push(self):
    self.stack.push(6)
    self.stack.push(2)
    self.stack.push(8)
    self.assertEqual(self.stack, Stack([6, 2, 8]))

  def tearDown(self): pass


if __name__ == '__main__':
  unittest.main()
