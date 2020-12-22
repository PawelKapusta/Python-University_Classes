class Queue:

  def __init__(self, elems=None):
    if elems is None:
      elems = []
    self.items = elems

  def __str__(self):
    return str(self.items)

  def __eq__(self, other):
    return self.items == other.items

  def is_empty(self):
    return not self.items

  def is_full(self):
    return False

  def put(self, data):
    if self.is_full():
      raise OverflowError("Queue is full!")
    self.items.append(data)

  def get(self):
    if self.is_empty():
      raise ValueError("Queue is empty!")
    return self.items.pop(0)
