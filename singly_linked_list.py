class Node:
  def __init__(self, val, nextVal = None):
    self.val = val
    self.next = nextVal

  def set_val(self, val):
    self.val = val

  def __repr__(self):
    return repr({ 'val': self.val })
    # return repr({ 'val': self.val, 'next': self.next })


class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0


  def __repr__(self):
    return repr({ 'head': self.head, 'tail': self.tail, 'size': self.size })


  def push(self, val):
    node = Node(val)
    
    if self.head is None: self.head = node
    else: self.tail.next = node

    self.tail = node
    self.size += 1

    return self


  def pushleft(self, val):
    node = Node(val, self.head)
    self.head = node
    self.size += 1

    if self.size == 1: self.tail = self.head

    return self


  def pop(self):
    if self.size == 0: return None

    popped = self.head
    tail = popped

    while popped.next:
      tail, popped = popped, popped.next

    if self.size == 1:
      self.head = None
      self.tail = None
    else: 
      tail.next = None
      self.tail = tail
    
    self.size -= 1
    return popped


  def popleft(self):
    if self.size == 0: return None

    popped = self.head
    self.head = popped.next
    self.size -= 1

    if self.size == 0:
      self.tail = None

    return popped


  def get(self, index):
    if index < 0 or index >= self.size: 
      return None

    current_index = 0
    node = self.head

    while current_index < index:
      node = node.next
      current_index += 1
    
    return node


  def set_val(self, index, val):
    node = self.get(index)

    if node:
      node.set_val(val)
      return True
    
    return False


  def insert(self, index, val):
    if index < 0 or index > self.size: return False
    if index == 0: self.pushleft(val)
    elif index == self.size: self.push(val)
    else:
      node = Node(val)
      previous_node = self.get(index - 1)
      previous_node.next, node.next = node, previous_node.next
      self.size += 1
    
    return True


  def remove(self, index):
    if index < 0 or index >= self.size: return None
    elif index == 0: return self.popleft()
    elif index == self.size - 1: return self.pop()
    else:
      previous_node = self.get(index - 1)
      node = previous_node.next
      previous_node.next = previous_node.next.next
      self.size -= 1
      return node


  def reverse(self):
    node = self.head
    self.head, self.tail = self.tail, self.head
    previous_node = None
    next_node = None

    for n in range(self.size):
      next_node = node.next
      node.next = previous_node
      previous_node = node
      node = next_node

    return self


singly_linked_list = SinglyLinkedList()
# print(singly_linked_list)
singly_linked_list.push(0)
singly_linked_list.push(1)
singly_linked_list.push(2)
# singly_linked_list.push('Good')
# singly_linked_list.push('Bye')
# singly_linked_list.push('!')
# print(singly_linked_list.head.next.val)
# print(singly_linked_list.tail)
# print(singly_linked_list.tail.next)
# print(singly_linked_list.size)
# singly_linked_list.traverse()
# singly_linked_list.push('Poo')
# print(singly_linked_list)
# print(singly_linked_list.pushleft(2))
# print(singly_linked_list.pushleft(1))
# print(singly_linked_list.pop())
# print(singly_linked_list.popleft())
# print(singly_linked_list)
# print(singly_linked_list.get(-1))
# print(singly_linked_list.get(1))
# print(singly_linked_list.get(2))
# print(singly_linked_list.get(3))
# print(singly_linked_list.set_val(-1, 1))
print(singly_linked_list.insert(3, 3))
print(singly_linked_list.insert(0, -1))
# print(singly_linked_list.get(0))
# print(singly_linked_list.get(1))
# print(singly_linked_list.get(2))
# print(singly_linked_list.get(3))
# print(singly_linked_list.get(4))
# print(singly_linked_list.get(5))
singly_linked_list.reverse()
# print(singly_linked_list.get(0))
# print(singly_linked_list.get(1))
# print(singly_linked_list.get(2))
# print(singly_linked_list.get(3))
# print(singly_linked_list.get(4))
# print(singly_linked_list.get(5))
# print('\n', singly_linked_list.remove(2), '\n')
# print(singly_linked_list.get(1))
# print(singly_linked_list.get(2))
# print(singly_linked_list.get(3))
# print(singly_linked_list.get(4))

