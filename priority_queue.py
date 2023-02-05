from math import floor


class Node:
  def __init__(self, val, priority):
    self.val = val
    self.priority = priority

  
  def __repr__(self):
    return repr({ 'val': self.val, 'priority': self.priority })




class PriorityQueue:
  def __init__(self):
    self.values = []

  
  def __repr__(self):
    return repr(self.values)


  def enqueue(self, value, priority):
    node = Node(value, priority)
    self.values.append(node)

    i = len(self.values) - 1
    parent_i = floor((i - 1) / 2)

    while i > 0 and self.values[i].priority < self.values[parent_i].priority:
      self.values[i], self.values[parent_i] = self.values[parent_i], self.values[i]
      i = parent_i
      parent_i = floor((i - 1) / 2)

    return self.values


  def dequeue(self):
    if len(self.values) == 0: return None

    self.values[0], self.values[-1] = self.values[-1], self.values[0]

    max_value = self.values.pop()

    length = len(self.values)

    i = 0
    swapped = True

    while swapped and length:
      priority = self.values[i].priority
      l_i = 2 * i + 1 
      r_i = l_i + 1
      l = l_i < length
      r = r_i < length
      swapped = False

      if l and r and self.values[l_i].priority < priority and self.values[l_i].priority < self.values[r_i].priority \
        or l and not r and self.values[l_i].priority < priority:
          self.values[l_i], self.values[i] = self.values[i], self.values[l_i]
          i = l_i
          swapped = True
      elif l and r and self.values[r_i].priority < priority and self.values[r_i].priority < self.values[l_i].priority \
        or r and not l and self.values[r_i].priority < priority:
          self.values[r_i], self.values[i] = self.values[i], self.values[r_i]
          i = r_i
          swapped = True

    return max_value.val

# queue = PriorityQueue()
# print(queue.enqueue('Take a dump', 3))
# print(queue.enqueue('Eat food', 2))
# print(queue.enqueue('Sleep', 4))
# print(queue.enqueue('Go for a walk', 5))
# print(queue.enqueue('Drink water', 1))
# print(queue.dequeue())
# print(queue)
# print(queue.dequeue())
# print(queue)
# print(queue.enqueue('Think about stuff', 2))
# print(queue)
# print(queue.dequeue())
