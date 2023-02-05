class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  
  def __repr__(self):
    return repr({ 'val': self.val })
    # return repr({ 'val': self.val, 'left': self.left, 'right': self.right })




class BinarySearchTree:
  def __init__(self, root = None):
    self.root = root
  

  def __repr__(self):
    return repr({ 'root': self.root })


  @classmethod
  def get_side(cls, node, val): return 'right' if val > node.val else 'left'


  def insert(self, val):
    node = Node(val)
    inserted = False

    if not self.root: 
      self.root = node
      inserted = True

    current_node = self.root

    while not inserted:
      if val == current_node.val: return None

      side = self.get_side(current_node, val)
      next_node = getattr(current_node, side)
      
      if next_node: 
        current_node = next_node
      else:
        setattr(current_node, side, node)
        inserted = True

    return self


  def contains(self, val):
    node = self.root
    found = False

    while not found and node:
      if node.val == val: found = True
      else: node = getattr(node, self.get_side(node, val))
    
    return found



# tree = BinarySearchTree()
# tree.insert(10)
# tree.insert(11)
# tree.insert(9)
# tree.insert(6)
# tree.insert(8)
# tree.insert(7)
# print(tree.contains(1))
