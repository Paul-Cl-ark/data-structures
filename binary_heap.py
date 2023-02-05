from math import floor

class BinaryHeap:
  def __init__(self):
    self.values = []

  
  def __repr__(self):
    return self.values


  def insert(self, value):
    self.values.append(value)

    i = len(self.values) - 1
    parent_i = floor((i - 1) / 2)

    while self.values[i] > self.values[parent_i] and i > 0:
      self.values[i], self.values[parent_i] = self.values[parent_i], self.values[i]
      i = parent_i
      parent_i = floor((i - 1) / 2)

    return self.values


  def extract_max(self):
    if len(self.values) == 0: return None

    self.values[0], self.values[-1] = self.values[-1], self.values[0]

    max_value = self.values.pop()

    length = len(self.values)

    i = 0
    swapped = True

    while swapped and length:
      val = self.values[i]
      l_i = 2 * i + 1 
      r_i = l_i + 1
      l = l_i < length
      r = r_i < length
      swapped = False

      if l and r and self.values[l_i] > val and self.values[l_i] > self.values[r_i] \
        or l and not r and self.values[l_i] > val:
          self.values[l_i], self.values[i] = self.values[i], self.values[l_i]
          i = l_i
          swapped = True
      elif l and r and self.values[r_i] > val and self.values[r_i] > self.values[l_i] \
        or r and not l and self.values[r_i] > val:
          self.values[r_i], self.values[i] = self.values[i], self.values[r_i]
          i = r_i
          swapped = True

    return max_value


binary_heap = BinaryHeap()
binary_heap.insert(41)
binary_heap.insert(39)
binary_heap.insert(33)
binary_heap.insert(18)
binary_heap.insert(27)
binary_heap.insert(12)
binary_heap.insert(55)
binary_heap.insert(11)
binary_heap.insert(7)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
print(binary_heap.extract_max())
print(binary_heap.values)
