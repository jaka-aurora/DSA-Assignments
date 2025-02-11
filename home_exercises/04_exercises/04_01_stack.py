from queue import LifoQueue

animal_stack = LifoQueue()
animals = ['cat', 'dog', 'lion', 'elephant', 'giraffe', 'tiger']

for animal in animals:
    animal_stack.put(animal)

print("Number of animals in the stack:", animal_stack.qsize())

new_stack = LifoQueue()

for _ in range(3):
    new_stack.put(animal_stack.get())

print("\nOriginal stack after moving top three animals:")
original_stack = []
while not animal_stack.empty():
    original_stack.append(animal_stack.get())
print(original_stack)

print("\nNew stack:")
new_stack_list = []
while not new_stack.empty():
    new_stack_list.append(new_stack.get())
print(new_stack_list)

print("\nIs animal_stack empty?", animal_stack.empty())
print("Is new_stack empty?", new_stack.empty())

#copy content of the stack to another stack

def copy_stack(original_stack):
    temp_list = []

    # Move elements from original_stack to temp_list
    while not original_stack.empty():
        temp_list.append(original_stack.get())

    # Restore original_stack and create a copy
    copied_stack = LifoQueue()
    for item in reversed(temp_list):  # Reverse to maintain original order
        original_stack.put(item)
        copied_stack.put(item)

    return copied_stack