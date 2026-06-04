from collections import deque

# =========================================
# 1. 顺序表（ArrayList）
# =========================================

class SeqList:
  def __init__(self):
    self.data = []
  def append(self, value):
    self.data.append(value)
  def insert(self, index, value):
    self.data.insert(index, value)
  def remove(self, value):
    self.data.remove(value)
  def get(self, index):
    return self.data[index]
  def __repr__(self):
    return str(self.data)
  

# =========================================
# 2. 链表（单向链表）
# =========================================
class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, value):
    new_node = ListNode(value)
    if not self.head:
      self.head = new_node
      return
    
    cur = self.head
    while cur.next:
      cur = cur.next

    cur.next = new_node
  
  def print_list(self):
    cur = self.head

    while cur:
      print(cur.value, end=" -> ")
      cur = cur.next
      
    print ("None")


# =========================================
# 3. 栈（Stack）
# =========================================

class Stack:
  def __init__(self):
    self.data = []

  def push(self, value):
    self.data.append(value)

  def pop(self):
    if self.is_empty():
      return None
    
    return self.data.pop()
  
  def peek(self):
    if self.is_empty():
      return None
    
    return self.data[-1]
  
  def is_empty(self):
    return len(self.data) == 0
  

# =========================================
# 4. 队列（Queue）
# =========================================
class Queue:
  def __init__(self):
    self.data = deque()

  def is_empty(self):
    return len(self.data) == 0
  
  def enqueue(self, value):
    self.data.append(value)

  def dequeue(self):
    if self.is_empty():
      return None
    
    return self.data.popleft()
  
class String:
  def __init__(self, value=""):
    self.data = value

  def concat(self, other):
    self.data += other

  def substring(self, start, end):
    return self.data[start:end]
  
  def __repr__(self):
    return self.data
  

# =========================================
# 6. 二叉树（Binary Tree）
# =========================================

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def preorder(self, root):
    if not root:
      return
    
    print(root.value, end=" ")
    self.preorder(root.left)
    self.preorder(root.right)
    

# =========================================
# 7. 普通树（多叉树）
# =========================================

class Tree:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, node):
    self.children.append(node)


# =========================================
# 8. 二叉搜索树（BST）
# =========================================

class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
class BST:
  def __init__(self):
    self.root = None

  def insert(self, value):
    self.root = self._insert(self.root, value)

  def _insert(self, node, value):
    if not node:
      return BSTNode(value)
    
    if value < node.value:
      node.left = self._insert(node.left, value)
    else:
      node.right = self._insert(node.right, value)

    return node
  
  def search(self, value):
    return self._search(self.root, value)

  def _search(self, node, value):
    if not node:
      return False
    
    if node.value == value:
      return True
    
    if value < node.value:
      return self._search(node.left, value)
    else:
      return self._search(node.right, value)



# =========================================
# 9. 图（Graph）
# =========================================

class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    
    self.graph[u].append(v)

  def print_graph(self):
    for node in self.graph:
      print(node, "->", self.graph[node])


# =========================================
# 10. 邻接表（Adjacency List）
# =========================================

class AdjacencyList:
  def __init__(self):
    self.adj = {}
  
  def add_edge(self, u, v):
    self.adj.setdefault(u, []).append(v)
    self.adj.setdefault(v, []).append(u)

  def print_graph(self):
    print(self.adj)


# =========================================
# 11. 邻接矩阵（Adjacency Matrix）
# =========================================

class AdjacencyMatrix:
  def __init__(self, size):
    self.size = size
    self.matrix = [[0] * size for _ in range(size)]
  
  def add_edge(self, u, v):
    self.matrix[u][v] = 1
    self.matrix[v][u] = 1

  def print_matrix(self):
    for row in self.matrix:
      print(row)


# =========================================
# 12. 哈希表（Hash Table）
# =========================================

class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]

  def _hash(self, key):
    return hash(key) % self.size
  
  def put(self, key, value):
    index = self._hash(key)

    for pair in self.table[index]:
      if pair[0] == key:
        pair[1] = value
        return
      
    self.table[index].append([key, value])

  def get(self, key):
    index = self._hash(key)

    for pair in self.table[index]:
      if pair[0] == key:
        return pair[1]
      
    return None
  
  def print_table(self):
    print(self.table)


# =========================================
# 测试
# =========================================

if __name__ == "__main__":

    print("===== 顺序表 =====")
    arr = SeqList()
    arr.append(1)
    arr.append(2)
    arr.insert(1, 100)
    print(arr)

    print("\n===== 链表 =====")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()

    print("\n===== 栈 =====")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())

    print("\n===== 队列 =====")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())

    print("\n===== 串 =====")
    s = String("hello")
    s.concat(" world")
    print(s)
    print(s.substring(0, 5))

    print("\n===== 二叉树 =====")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    bt = BinaryTree()
    bt.preorder(root)

    print("\n\n===== BST =====")
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)

    print(bst.search(7))
    print(bst.search(100))

    print("\n===== 图 =====")
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.print_graph()

    print("\n===== 邻接表 =====")
    adj_list = AdjacencyList()
    adj_list.add_edge(0, 1)
    adj_list.add_edge(0, 2)
    adj_list.print_graph()

    print("\n===== 邻接矩阵 =====")
    adj_matrix = AdjacencyMatrix(3)
    adj_matrix.add_edge(0, 1)
    adj_matrix.add_edge(1, 2)
    adj_matrix.print_matrix()

    print("\n===== 哈希表 =====")
    ht = HashTable(10)
    ht.put("name", "Tom")
    ht.put("age", 18)

    print(ht.get("name"))
    ht.print_table()