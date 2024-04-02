# File Recursion

# Finding Files For this problem, the goal is to write code for finding all files under a directory (and all
# directories beneath it) that end with ".c"
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Invalid input: path is invalid or null
    if not path or path == '':
        return []
    # Base case: path is .c file
    elif os.path.isfile(path) and path.endswith(suffix):
        return [path]
    # Base case: not .c file
    elif os.path.isfile(path):
        return []
    # Recursive case: subpaths in directory
    files = []
    for subpath in os.listdir(path):
        files = files + find_files(suffix, os.path.join(path, subpath))
    return files

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
solution = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print(find_files('.c', './testdir'))
assert find_files('.c', './testdir') == solution

## Test Case 2
solution = []
print(find_files('.c', ''))
assert find_files('.c', '') == solution

## Test Case 3
solution = []
print(find_files('', None))
assert find_files('', None) == solution
