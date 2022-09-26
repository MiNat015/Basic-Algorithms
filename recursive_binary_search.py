def recursive_binary_search(nums: list, target: int):
    """
    Implements binary search to find target value in the list
    Returns the index of the target value
    """
    # Base Case
    if len(nums) == 0:
        return False
    
    midpoint = (len(nums))//2
        
    if nums[midpoint] == target:
        return True
    else:
        if nums[midpoint] < target:
            return recursive_binary_search(nums[midpoint+1:], target)
        else:
            return recursive_binary_search(nums[:midpoint], target)



def verify(result):
    print("Target found: ", result)


nums = [1,2,3,5,6,10,200,205]

result = recursive_binary_search(nums, 10)
verify(result)
