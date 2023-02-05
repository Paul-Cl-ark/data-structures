class Node:
  def __init__(self, val, nextVal = None, prevVal = None):
    self.val = val
    self.next = nextVal
    self.prev = prevVal

  def set_val(self, val):
    self.val = val

  def __repr__(self):
    return repr({ 'val': self.val })
    # return repr({ 'val': self.val, 'next': self.next, 'prev': self.prev })


class DoublyLinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.size = 0


  def __repr__(self):
    return repr({ 'head': self.head, 'tail': self.tail, 'size': self.size })


  def push(self, val):
    node = Node(val)
    
    if self.head is None: self.head = node
    else: 
      self.tail.next = node
      node.prev = self.tail

    self.tail = node
    self.size += 1

    return self


  def pushleft(self, val):
    node = Node(val, self.head)

    if self.size == 0: self.tail = node
    else: self.head.prev = node
      
    self.head = node
    self.size += 1

    return self


  def pop(self):
    if self.size == 0: return None

    popped = self.tail

    if self.size == 1:
      self.head = self.tail = None
    else: 
      self.tail = popped.prev
      self.tail.next = None
    
    self.size -= 1

    popped.prev = None
    return popped


  def popleft(self):
    if self.size == 0: return None
    
    popped = self.head
    self.head = popped.next

    self.size -= 1

    if self.size == 0: self.tail = None
    else: self.head.prev = None

    popped.next = None
    return popped


  def get(self, index):
    if index < 0 or index >= self.size: return None

    current_index = 0 if index <= self.size // 2 else self.size - 1
    node = self.head if index <= self.size // 2 else self.tail

    while current_index != index:
      node = node.next if index <= self.size // 2 else node.prev
      if index <= self.size // 2: current_index += 1
      else: current_index -= 1
    
    return node


  def set_val(self, index, val):
    node = self.get(index)

    if node:
      node.set_val(val)
      return True
    
    return False


  def insert(self, index, val):
    if index < 0 or index > self.size: return False
    elif index == 0: self.pushleft(val)
    elif index == self.size: self.push(val)
    else:
      previous_node = self.get(index - 1)
      node = Node(val, previous_node.next, previous_node)
      node.next.prev = previous_node.next = node
      self.size += 1
    
    return True


  def remove(self, index):
    if index < 0 or index >= self.size: return None
    elif index == 0: return self.popleft()
    elif index == self.size - 1: return self.pop()
    else:
      node = self.get(index)
      node.prev.next = node.next
      node.next.prev = node.prev 
      self.size -= 1

      node.next = node.prev = None
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
      node.prev = node = next_node

    return self


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.pushleft('Five')
doubly_linked_list.pushleft('Four')
doubly_linked_list.pushleft('Three')
doubly_linked_list.pushleft('Two')
doubly_linked_list.pushleft('One')
doubly_linked_list.pushleft('Zero')
# print(doubly_linked_list.push(5))
# print(doubly_linked_list.popleft())
# print(doubly_linked_list.popleft())
# print(doubly_linked_list.popleft())
# print(doubly_linked_list.popleft())
doubly_linked_list.insert(2, 'New Two')
# print(doubly_linked_list.get(0))
# print(doubly_linked_list.get(1))
# print(doubly_linked_list.get(2))
# print(doubly_linked_list.get(3))
# print(doubly_linked_list.get(4))
# print(doubly_linked_list.remove(2))
# two = doubly_linked_list.get(2)
# print(two, two.next, two.prev)
# print(doubly_linked_list.get(0))
# print(doubly_linked_list.get(1))
# print(doubly_linked_list.get(2))
# print(doubly_linked_list.get(3))
print(doubly_linked_list.head)
doubly_linked_list.reverse()
print(doubly_linked_list.tail.prev)
print(doubly_linked_list)
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(1))
# print(doubly_linked_list.remove(0))
