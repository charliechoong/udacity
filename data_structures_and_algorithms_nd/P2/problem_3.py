# Rearrange Array Digits

# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can
# assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by
# more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity
# is O(nlog(n)).
#
# for e.g. [1, 2, 3, 4, 5]
#
# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when
# there are more than one possible answers, return any one.

def merge_sort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    # Given two ordered lists, merge them together in order, returning the merged list.
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    if l < len(left):
        merged += left[l:]
    elif r < len(right):
        merged += right[r:]
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Merge sort the digits in ascending order
    input_list = merge_sort(input_list)

    # Using digits from highest, form two numbers by alternating the digits
    first, second = '', ''
    for i in range(len(input_list)-1, -1, -1):
        if i%2 == 0:
            first = first + str(input_list[i])
        else:
            second = second + str(input_list[i])
    return int(first), int(second)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[1, 1, 1, 1, 1, 1], [111, 111]]
test_function(test_case)

test_case = [[1, 0, 1, 1, 0, 0], [110, 100]]
test_function(test_case)