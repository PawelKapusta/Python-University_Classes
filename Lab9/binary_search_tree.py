class Node:

  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

  def insert(self, node):
    if node.data < self.data:
      if self.left:
        self.left.insert(node)
      else:
        self.left = node
    else:
      if self.right:
        self.right.insert(node)
      else:
        self.right = node

  def count(self):
    counter = 1
    if self.left:
      counter += self.left.count()
    if self.right:
      counter += self.right.count()
    return counter

  def search(self, data):
    if self.data == data:
      return self
    if data < self.data:
      if self.left:
        return self.left.search(data)
    else:
      if self.right:
        return self.right.search(data)
    return None

  def remove(self, data):
    if data < self.data:
      if self.left:
        self.left = self.left.remove(data)
    elif self.data < data:
      if self.right:
        self.right = self.right.remove(data)
    else:
      if self.left is None:
        return self.right
      else:
        node = self.left
        while node.right:
          node = node.right
        node.right = self.right
        return self.left
    return self

def bst_min(root):
  if root.left is not None:
    return bst_min(root.left)
  else:
    return root

def bst_max(root):
  if root.right is not None:
    return bst_max(root.right)
  else:
    return root
