# Max and Min of an Unsorted Integer Array

# In this problem, we will look for smallest and largest integer from a list of unsorted integers.
# The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
#
# Bonus Challenge: Is it possible to find the max and min in a single traversal?

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min, max = None, None
    if len(ints) == 0:
        return min, max
    for num in ints:
        if min is None or num < min:
            min = num
        if max is None or num > max:
            max = num
    return min, max


### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [-2, -4, -1, -1, 0]
print("Pass" if ((-4, 0) == get_min_max(l)) else "Fail")

l = [-1, -1, -1]
print("Pass" if ((-1, -1) == get_min_max(l)) else "Fail")

l = []
print("Pass" if ((None, None) == get_min_max(l)) else "Fail")