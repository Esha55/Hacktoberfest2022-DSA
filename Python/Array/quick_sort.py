# Quick sort in Python

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quick_Sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quick_Sort(array, low, pi - 1)
    quick_Sort(array, pi + 1, high)

data = [24, 4, 8, 0, 5, 19, 16]
print("Unsorted Array")
print(data)

size = len(data)

quick_Sort(data, 0, size - 1)

print('Sorted Array in Ascending Order is:')
print(data)