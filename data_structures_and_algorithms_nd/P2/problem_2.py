# Search in a Rotated Sorted Array

# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of
# O(log n).
#
# Example: Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

def find_pivot(arr):
    def _find_recursive(arr, start, stop):
        if start > stop:
            return None
        mid = start + (stop-start)//2
        if arr[mid-1] > arr[mid]:
            return mid
        else:
            right = _find_recursive(arr, mid+1, stop)
            if right is not None:
                return right
            left = _find_recursive(arr, start, mid-1)
            if left is not None:
                return left
        return None
    return _find_recursive(arr, 0, len(arr)-1)


def binary_search(arr, number):
    def _binary_search_recursive(arr, target, start, stop):
        if start > stop:
            return -1
        mid = start + (stop-start)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return _binary_search_recursive(arr, target, start, mid - 1)
        else:
            return _binary_search_recursive(arr, target, mid + 1, stop)
    return _binary_search_recursive(arr, number, 0, len(arr)-1)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # First, find the pivot using binary search.
    pivot = find_pivot(input_list)

    # Then split array into 2 subarrays. Determine which one is within the range.
    # Then do binary search in the selected subarray.
    left, right = input_list[:pivot], input_list[pivot:]
    if left[0] <= number <= left[len(left)-1]:
        return binary_search(left, number)
    elif right[0] <= number <= right[len(right)-1]:
        return pivot + binary_search(right, number)
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#test_function([[1, 2, 3, 4], 4])
