from Lab9.double_list import *

db_list = DoubleList()

for index in range(15):
  db_list.insert_tail(Node(index))

print("My list:", db_list)
node1 = Node(0)
node2 = Node(db_list.length - 1)
node3 = Node(6)
db_list.remove(node1)
print("After removing first node:", db_list)
db_list.remove(node2)
print("After removing last element:", db_list)
db_list.remove(node3)
print("After removing node on index 6", db_list)

print("Min in list:", db_list.find_min())
print("Max in list:", db_list.find_max())

db_list.clear()
print("After clear all list:", db_list)
