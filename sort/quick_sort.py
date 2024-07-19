def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[len(arr)//2]
    less = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]

    return quicksort(less) + equal + quicksort(greater)


print(quicksort([10, 5, 2, 3]))  # => [2, 3, 5, 10]
print(quicksort([5, 3, 6, 2, 10]))  # => [2, 3, 5, 6, 10]
print(quicksort([100, 12, 30, 4, 85]))  # => [4, 12, 30, 85,100]
