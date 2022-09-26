from linked_list import LinkedList

def merge_sort(nums: LinkedList):
    """
    Sorts linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """
    
    # Base Case
    if nums.size() == 1 or nums.head is None:
        return nums

    left_half, right_half = split(nums)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(ls: LinkedList):
    """
    Divide the unsorted list into sublists

    Returns left-half and right-half
    """
    
    if ls == None or ls.head is None:
        left_half = ls
        right_half = None
    
        return left_half, right_half
    else:
        size = ls.size()
        mid = size//2
        
        mid_node = ls.get_node(mid-1)

        left_half = ls
        right_half = LinkedList()

        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in the nodes
    Returns a new, merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right

    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach 
    # the tail node of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head

            # Call next on left to set loop condition to False
            left_head = left_head.next_node
            
        else:
            # Not at either tail node
            # Obtain node data to perform comparision operation
            left_data = left_head.data 
            right_data = right_head.data
            # if left_data is less than right_data, set current to left node
            if left_data < right_data:
                current.next_node = left_head

                # Move left head to next node
                left_head = left_head.next_node

            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                
                # Move right head to next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

def verify(ls: LinkedList):
    """
    Verify's whether the linked list is sorted or not
    Returns True if sorted and False otherwise
    """
    # Gets the size of the linked list
    size = ls.size()
    
    # Returns True if size is less than or equal to 1
    if size == 0 or size == 1:
        return True
    
    split_node = ls.get_node(1)
    left_half = ls
    right_half = LinkedList()
    
    right_half.head = split_node.next_node
    split_node.next_node = None

    return left_half.head.data <= left_half.head.next_node.data and verify(right_half)
    

nums = LinkedList()
nums.add(10)
nums.add(2)
nums.add(5)
nums.add(22)
nums.add(80)
nums.add(1)

print('Original Linked List: ', nums)

sorted_list = merge_sort(nums)

print('Sorted List: ', sorted_list)

