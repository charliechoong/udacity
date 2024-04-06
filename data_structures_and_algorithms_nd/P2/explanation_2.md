First, binary search is used to find the pivot in O(log n).
Then, the original is split into 2 subarrays based on pivot.
Number is determined in the subarray by comparing the 2 extreme values in each subarray.
Then, binary search is used again to find the number in the subarray in O(log n).

Hence, overall time complexity is O(log n).