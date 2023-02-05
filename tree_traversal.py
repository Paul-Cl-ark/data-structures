from queue import Queue
from binary_search_tree import BinarySearchTree

def breadth_first_search(tree):
  queue = Queue()
  values = []

  if tree.root: queue.enqueue(tree.root)

  while queue.size:
    node = queue.start.val
    if node.left: queue.enqueue(node.left)
    if node.right: queue.enqueue(node.right)
    values.append(node.val)
    queue.dequeue()

  return values



def pre_order_depth_first_search(tree):
  values = []

  def go_deeper(node):
    values.append(node.val)
    if (node.left): go_deeper(node.left)
    if (node.right): go_deeper(node.right)

  if tree.root: go_deeper(tree.root)

  return values

def post_order_depth_first_search(tree):
  values = []

  def go_deeper(node):
    if (node.left): go_deeper(node.left)
    if (node.right): go_deeper(node.right)
    values.append(node.val)

  if tree.root: go_deeper(tree.root)

  return values


def in_order_depth_first_search(tree):
  values = []

  def go_deeper(node):
    if (node.left): go_deeper(node.left)
    values.append(node.val)
    if (node.right): go_deeper(node.right)

  if tree.root: go_deeper(tree.root)

  return values
  

tree = BinarySearchTree()
# tree.insert(10)
# tree.insert(6)
# tree.insert(15)
# tree.insert(3)
# tree.insert(8)
# tree.insert(20)
tree.insert(10)
tree.insert(11)
tree.insert(8)
tree.insert(4)
tree.insert(6)
tree.insert(9)
tree.insert(7)
tree.insert(3)
# print(breadth_first_search(tree))
print(in_order_depth_first_search(tree))
