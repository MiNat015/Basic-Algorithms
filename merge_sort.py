def merge_sort(nums: list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    Overall takes O(k*n log n) time
    """
    

    # Base Case
    if len(nums) <= 1:
        return nums
    
    # Divide Step
    left_half, right_half = split(nums)

    # Conquer Step
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    # Combine Step
    return merge(left, right)

def split(ls: list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Overall takes O(k log n) time (list slicing takes O(k) time)
    """

    mid = len(ls)//2
    left = ls[:mid]
    right = ls[mid:]

    return left, right

def merge(left: list, right: list):
    """
    Merges two lists(arrays), sorting them in the process
    Returns a new merged listi

    Takes O(n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(ls: list):
    n = len(ls)

    if n == 0 or n == 1:
        return True

    return ls[0] <= ls[1] and verify_sorted(ls[1:])



alist = [54, 832, 54, 23, 15, 1, 89, 57, 2, 4, 5, 6, 7, 8]
l = merge_sort(alist)
print(l)
print("Verify sorted: ", verify_sorted(l))

