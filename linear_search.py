def linear_search(nums: list, target: int):
    """
    Returns the index position of the target if found, else returns -1
    """
    position = 0
    for x in nums:
        if x == target:
            return position
        position+=1

    return -1

# Test Case: 1
print(linear_search([1,2,3,5,6], 3))
