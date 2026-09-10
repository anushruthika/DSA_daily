# for a specific tree, and subtrees within this tree as assumed to follow max_heap property
def max_heapify(arr,n,node):
  while True:
    left = node*2+1
    right = node*2+2
    largest = node
    if left<n and arr[largest]<arr[left]:
      largest = left
    if right<n and arr[largest]<arr[right]:
      largest = right
    if largest == node:
      break
    arr[node],arr[largest] = arr[largest],arr[node]
    node = largest
def heapsort(arr):
  n = len(arr)
  for node in range(n-1,-1,-1):
    max_heapify(arr,n,node)
  for end in range(n-1,-1,-1):
    arr[end],arr[0] = arr[0],arr[end]
    max_heapify(arr,end,0)
  return arr
print(heapsort([5,4,6,8,3,2,7]))
  
  
