def array_multiplication_table(arr):
    if arr == []:
        return []

    return [[i * j for j in arr] for i in arr]


# print the grid of the array
def print_arr(arr):
    for row in arr:
        print(row)


# test the function
arr = [1, 2, 3, 4, 5]
print_arr(array_multiplication_table(arr))
