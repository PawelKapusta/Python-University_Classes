from Lab10.queue_lib import *
import unittest


class TestQueue(unittest.TestCase):

  def setUp(self):
    self.queue = Queue()

  def test_str(self):
    self.assertEqual(str(self.queue), '[]')

  def test_eq(self):
    self.assertEqual(self.queue, Queue())

  def test_is_empty(self):
    self.assertEqual(self.queue.is_empty(), True)

  def test_is_full(self):
    self.assertEqual(self.queue.is_full(), False)

  def test_pop(self):
    with self.assertRaises(ValueError):
      Queue().get()
    self.queue.put(10)
    self.assertEqual(self.queue.get(), 10)

  def test_push(self):
    self.queue.put(5)
    self.queue.put(3)
    self.queue.put(7)
    self.assertEqual(self.queue, Queue([5, 3, 7]))

  def tearDown(self): pass


if __name__ == '__main__':
  unittest.main()
