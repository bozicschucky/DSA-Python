def count_items_in_array(arr):
    count = 0

    if arr == []:
        return count

    count += 1
    return count + count_items_in_array(arr[1:])


print(count_items_in_array([1, 2, 3, 4, 5]))  # => 5
