

def find_max_num(nums):
    max_num = nums[0]
    if (len(nums) == 1):
        return max_num

    max_num = find_max_num(nums[1:])

    if (nums[0] > max_num):
        max_num = nums[0]

    return max_num


#  test cases for the function

print(find_max_num([1, 2, 3, 4, 5]))  # => 5
print(find_max_num([12, 21, 300, 4, 580]))  # => 580
