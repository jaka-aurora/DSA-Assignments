## Your answers 

## Update your home exercises in this directory when you have completed the given exercises.

## * Return tasks as source code (.py) or text file (.txt), depending on the exercise

list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 10]
list_3 = [None, 'a', 'b', 'c', 'd']
combined_list = []

def create_new_list(a,b,c):
    for i in a + b + c:
        if i not in combined_list: # skips same values, i.e gives unique values from all three lists
            combined_list.append(i)

    return combined_list

create_new_list(list_1, list_2, list_3)
print(combined_list)