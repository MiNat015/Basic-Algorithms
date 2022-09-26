def quicksort(values):
    """
    Sorts unsorted list using the quicksort algoritm
    Returns sorted list
    """
    # Base Case
    if len(values) <= 1:
        return values
    
    # Stores values less than pivot
    less_than_pivot = []
    # Stores values greater than pivot
    greater_than_pivot = []

    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
   
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Test Case: 1
numbers = [1, 56, 5, 89, 11, 2, 55, 8, 9, 4]

print("Unsorted: ", numbers)
print("Sorted: ", quicksort(numbers))


# Test Case: 2
names = ['Arjun Srikanth', 'Jack Stubbs', 'Ahmad Haqeem', 'Luke Dunphy', 'Zuman Saleem', 'Ben Stiller']
sorted_names = quicksort(names)

for x in sorted_names:
    print(x)
