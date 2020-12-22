from Lab10.randomqueue_lib import *

randomQueue = RandomQueue()

for i in range(50):
  randomQueue.insert(i)
print('My queue:', randomQueue)

while not randomQueue.is_empty():
  print("Removing element:", randomQueue.remove())
  print('My queue:', randomQueue)
