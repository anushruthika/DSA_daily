def heapify(arr):
  n = len(arr)
  for node in range(n-1,-1,-1):
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
    
print(heapify([1,2,3,4,5]))
print(heapify([1, 2, 3, 4, 5]))
print(heapify([5, 2, 3]))
print(heapify([5, 7, 2]))
print(heapify([1, 5, 3]))
print(heapify([10, 3, 5]))
print(heapify([10, 7, 3]))
print(heapify([10, 3, 8, 1, 2]))
print(heapify([20, 5, 10, 2, 3, 7, 8]))
print(heapify([5, 4, 3, 2, 1]))
print(heapify([5]))
print(heapify([1, 2]))
print(heapify([2, 1]))
print(heapify([3, 2, 1]))
print(heapify([5, 2, 2, 3, 1, 2]))
print(heapify([20, 5, 15, 3, 8, 10, 2, 1, 7, 6]))
        
    
