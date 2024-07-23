
# test graph
from collections import deque


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


person_graph = {'you': set(['alice', 'bob', 'claire']),
                'bob': set(['anuj', 'peggy']),
                'alice': set(['peggy']),
                'claire': set(['thom', 'jonny']),
                'anuj': set([]),
                'peggy': set([]),
                'thom': set([]),
                'jonny': set([])
                }


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def search(name, graph):
  search_queue = deque()
  search_queue += graph[name]
  searched = []

  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False


def person_is_seller(name):
  return name[-1] == 'm'


#  test cases for the function
print(dfs(graph, 'A'))  # => {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs(graph, 'C'))  # => {'A', 'E', 'F', 'C', 'D', 'B'}
print(dfs(graph, 'F'))  # => {'A', 'F', 'E', 'C', 'D', 'B'}


# test the search function
print(search('you', person_graph))  # => True
print(search('bob', person_graph))  # => False
print(search('claire', person_graph))  # => False
print(search('alice', person_graph))  # => False
print(search('thom', person_graph))  # => False
print(search('jonny', person_graph))  # => False
