from queue import Queue
from naive_priority_queue import NaivePriorityQueue
from priority_queue import PriorityQueue
from math import inf

class WeightedGraph:
  def __init__(self):
    self.adjacency_list = {}


  def __repr__(self):
    return str(self.adjacency_list)

  def add_vertex(self, key):
    if key not in self.adjacency_list: self.adjacency_list[key] = []


  def add_edge(self, vertex_1, vertex_2, weight):
    if vertex_1 in self.adjacency_list and vertex_2 in self.adjacency_list:
      self.adjacency_list[vertex_1].append({ 'value': vertex_2, 'weight': weight })
      self.adjacency_list[vertex_2].append({ 'value': vertex_1, 'weight': weight })

  # def remove_edge(self, vertex_1, vertex_2):
  #   if vertex_1 in self.adjacency_list and vertex_2 in self.adjacency_list:
  #     self.adjacency_list[vertex_1] = [vertex for vertex in self.adjacency_list[vertex_1] if vertex != vertex_2]
  #     self.adjacency_list[vertex_2] = [vertex for vertex in self.adjacency_list[vertex_2] if vertex != vertex_1]


  # def remove_vertex(self, vertex):
  #   if vertex in self.adjacency_list:
  #     for vertex_2 in self.adjacency_list:
  #       self.remove_edge(vertex, vertex_2)
  #     del self.adjacency_list[vertex]


  # def depth_first_traversal_recursive(self, start):
  #   values = []
  #   visited = {}

  #   def traverse(vertex):
  #     if vertex not in self.adjacency_list: 
  #       return None

  #     visited[vertex] = True
  #     values.append(vertex) 
  #     edges = self.adjacency_list[vertex]

  #     for neighbour in edges:
  #       if neighbour not in visited:
  #         traverse(neighbour)

  #   traverse(start)

  #   return values


  # def depth_first_traversal_iterative(self, start):
  #   if start not in self.adjacency_list:
  #     return []

  #   stack = [start]
  #   values = []
  #   visited = {}

  #   while len(stack):
  #     value = stack.pop()
  #     if value not in visited:
  #       visited[value] = True
  #       values.append(value)
  #       for neighbour in [v for v in self.adjacency_list[value] if v not in visited]:
  #         stack.append(neighbour)
    
  #   return values


  # def breadth_first_traversal(self, start):
  #   if start not in self.adjacency_list:
  #     return []
    
  #   queue = Queue()
  #   queue.enqueue(start)
  #   values = []
  #   visited = { start: True }

  #   while queue.size:
  #     node = queue.dequeue()
  #     values.append(node.val)

  #     for neighbour in self.adjacency_list[node.val]:
  #       if neighbour not in visited:
  #         visited[neighbour] = True
  #         queue.enqueue(neighbour)

  #   return values


  def dijkstra(self, start, end):
    queue = PriorityQueue()
    # queue = NaivePriorityQueue()
    distances = { key: 0 if key == start else inf for key in self.adjacency_list.keys() }
    previous = { key: None for key in self.adjacency_list.keys() }

    for k, distance in distances.items(): 
      queue.enqueue(k, distance)

    while len(queue.values):
      item = queue.dequeue()
      
      if item == end:
        result = []
        while previous[item]:
          result.insert(0, item)
          item = previous[item]
        
        result.insert(0, start)
        return result

      if item or distances[item] != inf:
        for edge in self.adjacency_list[item]:
          new_distance = distances[item] + edge['weight']
          neighbour = edge['value']

          if new_distance < distances[neighbour]:
            distances[neighbour] = new_distance
            previous[neighbour] = item
            queue.enqueue(neighbour, new_distance)




graph = WeightedGraph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_edge('a', 'b', 4)
graph.add_edge('a', 'c', 2)
graph.add_edge('b', 'e', 3)
graph.add_edge('c', 'd', 2)
graph.add_edge('c', 'f', 4)
graph.add_edge('d', 'e', 3)
graph.add_edge('d', 'f', 1)
graph.add_edge('e', 'f', 1)
print(graph.dijkstra('a', 'f'))
# print(graph.depth_first_traversal_recursive('a'))
# print(graph.depth_first_traversal_recursive('z'))
# print(graph.depth_first_traversal_iterative('a'))
# print(graph.depth_first_iterative('a'))
# print(graph.breadth_first_traversal('a'))
# print(graph.breadth_first_traversal('z'))
