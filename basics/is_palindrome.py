
def is_palidrome(s):
    reversed_list = list(s)
    reversed_list.reverse()
    #  join the list to make a string
    reversed_str = ''.join(reversed_list)
    return s == reversed_str


    # return s == s[::-1]
# Test
print(is_palidrome('hello'))  # False
print(is_palidrome('radar'))  # True
