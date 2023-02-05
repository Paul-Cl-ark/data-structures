class Node:
  def __init__(self, val, nextVal = None):
    self.val = val
    self.next = nextVal

  def set_val(self, val):
    self.val = val

  def __repr__(self):
    return repr({ 'val': self.val })
    # return repr({ 'val': self.val, 'next': self.next })


class Queue:
  def __init__(self):
    self.start = None
    self.end = None
    self.size = 0


  def __repr__(self):
    return repr({ 'start': self.start, 'end': self.end, 'size': self.size })


  def enqueue(self, val):
    node = Node(val)
    
    if self.start is None: self.start = node
    else: self.end.next = node

    self.end = node
    self.size += 1

    return self.size


  def dequeue(self):
    if self.size == 0: return None

    popped = self.start
    self.start = popped.next
    self.size -= 1

    if self.size == 0:
      self.end = None

    return popped


# queue = Queue()

# print(queue.enqueue(1))
# print(queue.enqueue(2))
# print(queue.enqueue(3))
# print(queue.enqueue(4))
# print(queue.enqueue(5))
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
