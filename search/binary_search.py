def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if (guess > item):
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursive(list, item, low=0, high=None):
    if high is None:
        high = len(list) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
        return mid

    if guess > item:
        return binary_search_recursive(list, item, low, mid - 1)
    else:
        return binary_search_recursive(list, item, mid + 1, high)

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7)) # => 1
print(binary_search(my_list, -1)) # => None
print(binary_search_recursive(my_list, 7)) # => 1


# What is wrong with the code above ?
# Here are the outputs.

# 3
# None
# 3
