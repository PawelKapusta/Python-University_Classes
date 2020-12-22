class Stack:

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

  def push(self, item):
    if self.is_full():
      raise OverflowError("Stack is full!")
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      raise ValueError("Stack is empty!")
    return self.items.pop()
