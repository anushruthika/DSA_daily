# heap: complete binary tree 
# minheap : child>parent 
# max_heap: child<parent

# node: i 
# parent: i//2, left: 2*i+1, right: 2*i+2

# insert delete in minheap
class minHeap:
  def __init__(self,capacity):
    self.heap = [0]*capacity
    self.size = 0
    self.capacity = capacity
  def parent(self,node):
    if node==0:
      return "no more parent"
    return node//2
  def left(self,node):
    left = node*2+1
    if left<=self.size:
      return left
    return "No left child"
  def right(self,node):
    right = node*2+2
    if right<=self.size:
      return right
    return "No right child"
  def insert(self,val):
    if self.size==self.capacity:
      return "Cant insert"
    self.heap[self.size] = val
    index = self.size
    self.size+=1
    parent = index//2
    while parent>=0:
      if self.heap[parent]>self.heap[index]:
        self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
        index = parent
        parent = index//2
      else:
        break
    # self.printHeap()
    return "inserted"
  def printHeap(self):
    print(self.heap)
  def delete(self):
    if self.size == 0:
      return "cant delete"
    delt = self.heap[0]
    self.size-=1
    self.heap[0] = self.heap[self.size]
    self.heap[self.size] = 0
    node = 0
    while node < self.size:
      left = 2*node+1
      right = 2*node+2
      if left<self.size and self.heap[left]<self.heap[node]:
        if right<self.size and self.heap[right]<self.heap[left]<self.heap[node]:
          self.heap[right],self.heap[node] = self.heap[node],self.heap[right]
          node = right
        else:
          self.heap[left],self.heap[node] = self.heap[node],self.heap[left]
          node = left
      elif right<self.size and self.heap[right]<self.heap[node]:
        self.heap[right],self.heap[node] = self.heap[node],self.heap[right]
        node = right
      else:
        break   
    
    return "deleted"+str(delt)      
  # Test
h = minHeap(20)

h.insert(20)
h.insert(15)
h.insert(30)
h.insert(5)
h.insert(10)
h.insert(25)
h.insert(35)
h.insert(2)
h.insert(8)
h.insert(18)

print("Heap:", h.heap[:h.size])

print(h.delete())
h.printHeap()
print(h.delete())
h.printHeap()
