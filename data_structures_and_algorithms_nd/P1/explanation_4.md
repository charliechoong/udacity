As it requires searching through recursive directories, recursion is effective method.
If any recursive call returns True, the highest call will return True as well.
The worst case time complexity is O(n^d) where n is the largest number of subdirectories and d is the greatest depth
of directory.