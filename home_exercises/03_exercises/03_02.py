def linear_search(lst, value):
    loops = 0
    for i, item in enumerate(lst):
        loops += 1
        if item == value:
            print(f"Number of loops: {loops}")
            print(f"The value {value} is located on index {i}.")
            return i
    print(f"Number of loops: {loops}")
    print(f"The value {value} is not found in the list.")

def binary_search(lst, value):
    lst.sort()
    left, right = 0, len(lst) - 1
    loops = 0
    while left <= right:
        loops += 1
        mid = (left + right) // 2
        if lst[mid] == value:
            print(f"Number of loops: {loops}")
            print(f"The value {value} is located on index {mid}.")
            return mid
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Number of loops: {loops}")
    print(f"The value {value} is not found in the list.")



unsorted_list = [34, 7, 10, 17, 21, 5, 16, 75, 23, 32, 5, 62]
value = 75

print("Linear search: ")
linear_search(unsorted_list, value)
print("Binary search: ")
binary_search(unsorted_list, value)