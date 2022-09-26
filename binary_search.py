def binary_search(nums: list, target: int):
    """
    Returns the position of target if found, else returns None
    """
    # Define pointers
    first = 0
    last = len(nums)-1
    
    # Perform binary search
    while first <= last:
        midpoint = (first+last)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
        
    
    return None

def verify(index: int):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in given list")


# Test Case: 1
numbers = [1,2,3,4,5,6,89,98,100]
index = binary_search(numbers, 6)
verify(index)
