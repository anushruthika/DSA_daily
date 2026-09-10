# min heap to sort desc

def min_heapify(arr,n,node):
  while True:
    left = 2*node+1
    right = 2*node+2
    smallest = node
    if left<n and arr[left]<arr[smallest]:
      smallest = left
    if right<n and arr[right]<arr[smallest]:
      smallest = right
    if smallest == node:
      break
    arr[node],arr[smallest] = arr[smallest],arr[node]
    node = smallest
  return arr
import heapq
def heapsort_minheap_descending(arr):
  l = len(arr)
  heapq.heapify(arr)
  for end in range(l-1,0,-1):
    arr[0],arr[end] = arr[end],arr[0]
    min_heapify(arr,end,0)
  return arr
print(heapsort_minheap_descending([1,3,2,4,6,5]))
