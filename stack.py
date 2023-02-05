class Node:
  def __init__(self, val, nextVal = None):
    self.val = val
    self.next = nextVal

  def set_val(self, val):
    self.val = val

  def __repr__(self):
    return repr({ 'val': self.val })
    # return repr({ 'val': self.val, 'next': self.next })


class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.size = 0


  def __repr__(self):
    return repr({ 'top': self.top, 'bottom': self.bottom, 'size': self.size })

  def push(self, val):
    node = Node(val, self.top)
    self.top = node
    self.size += 1

    if self.size == 1: self.bottom = self.top

    return self.size

  def pop(self):
    if self.size == 0: return None

    popped = self.top
    self.top = popped.next
    self.size -= 1

    if self.size == 0: self.bottom = None

    return popped

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
