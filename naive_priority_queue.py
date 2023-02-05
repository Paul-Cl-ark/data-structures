class NaivePriorityQueue:
  def __init__(self):
    self.values = []


  def __repr__(self):
    return str(self.values)

  
  def enqueue(self, value, priority):
    self.values.append({ 'value': value, 'priority': priority })
    self.values.sort(key=lambda item: item['priority'])


  def dequeue(self):
    return self.values.pop(0)['value']


# queue = NaivePriorityQueue()
# queue.enqueue('a', 10)
# queue.enqueue('b', 5)
# queue.enqueue('c', 20)
# queue.enqueue('d', 3)
# print(queue.dequeue())
# print(queue)
