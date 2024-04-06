# Square Root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def find(arr, number):
        if number < 0 or len(arr) == 0:
            return -1
        mid_idx = len(arr) // 2
        mid = arr[mid_idx]
        mid_squared = mid * mid
        if number == mid_squared:
            return mid
        elif number < mid_squared:
            if number > arr[mid_idx-1] * arr[mid_idx-1]:
                return arr[mid_idx-1]
            return find(arr[:mid+1], number)
        else:
            if number < arr[mid_idx+1] * arr[mid_idx+1]:
                return mid
            return find(arr[mid:], number)

    return find([i for i in range(0, number+1)], number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
