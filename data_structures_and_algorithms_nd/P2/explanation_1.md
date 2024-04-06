Binary search is performed on a list of numbers from 0 to n.
In each recursive call, the search space is halved, depending on whether the square of the number is greater or less
than the target number.
Time complexity is O(log n).
Space complexity is n + n/2 + n/4 + ... + 2 + 1 = 2n ~= O(n)