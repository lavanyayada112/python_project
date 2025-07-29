import time
import random

def bubble_sort(arr):
  """Implements bubble sort."""
  n = len (arr)
  for i in range(n):
     for j in range (0, n - i -1):
      if arr[j] > arr[j + 1]:
       arr[j],arr[j + 1] = arr[j + 1], arr[j]
  return arr 
arr=[13,4,11,2]
print ("Array before Bubble Sorting",arr)
arr2=bubble_sort(arr)
print("Array after Bubble sorting",arr2)


def insertion_sort(arr):
    """ Implements insertion sort."""
    for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >= 0 and key < arr[j]:
        arr[j +1] = arr[j]
        j -= 1
      arr [j + 1] = key
    return arr
arr=[13,4,11,2]
print("Array before Insertion Sorting",arr)
arr2=insertion_sort(arr)
print("Array after Insertion sorting",arr2)


def merge_sort(arr):
    """Implements merge sort."""
    if len(arr) > 1:
      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]
      merge_sort(left_half)
      merge_sort(right_half)
      i = j = k = 0
      while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
          arr[k] = left_half[i]
          i +=1
        else:
          arr[k] = right_half[j]
          j += 1
        k += 1
      while i < len(left_half):
       arr[k] = left_half[i]
       i += 1
       k += 1
      while j <len(right_half):
       arr[k] = right_half[j]
       j += 1
       k += 1
    return arr
arr=[13,4,11,2]
print("Array before Merge Sorting",arr)
arr2=merge_sort(arr)
print("Array after Merge sorting",arr2)

input_sizes = [1000, 5000, 10000]

for n in input_sizes:
  print(f"Testing with input size: {n}")
  # Generate a randaom list of integers
  data = [random.randint (0, n) for _ in range(n)]

  #Test Bubble Sort
  data_bubble = data[:] #Create a copy to avoid modifying the original data
  start_time = time.time()
  bubble_sort(data_bubble)
  end_time = time.time()
  print(f"bubble Sort time: {end_time - start_time:.6f} seconds")

  #Test Insertion Sort
  data_insertion = data[:] #Create a copy
  start_time = time.time()
  insertion_sort(data_insertion)
  end_time = time.time()
  print(f"insertion Sort time: {end_time - start_time:.6f} seconds")

  #Test Merge Sort
  data_merge = data[:] #create a copy
  start_time = time.time()
  merge_sort(data_merge)                            
  end_time = time.time()
  print(f"merge Sort time: {end_time - start_time:.6f} seconds")
  print("-" *30)












 

