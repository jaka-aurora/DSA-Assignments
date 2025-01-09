## 04-01. Using Stack 

In this exercise, you practice using the stack by adding and removing items in to the stack. 

 Add the following animals to the stack:
 'cat', 'dog', 'lion', 'elephant', 'giraffe', 'tiger'.

* Get the number of animals in the stack
* Take the top three animals from the original stack and move them to the new stack.
* Print the contents of the original stack and the contents of the new stack into which you moved the three animals.
* Finally, empty both stacks.

Input:
```python
animal_stack.push('cat')
animal_stack.push('dog')
animal_stack.push('rabbit')
animal_stack.push('tiger')
animal_stack.push('lion')
animal_stack.push('elephant')
```

Output: 
```
Original stack:
['cat', 'dog', 'rabbit', 'tiger', 'lion', 'elephant']

Original stack:
['cat', 'dog', 'rabbit']

New stack:
['elephant', 'lion', 'tiger']
```

Extra Question: If you want to copy content of the stack to another stack how you can implement that?

## 04-02. Restaurant Queues

Goal: The task is to model the processing of orders in restaurant using a queue. 

Let's use Python's queue.Queue() data structure to manage orders. 
The adding and processing of restaurant's orders is simulated with separate functions.

Implement: 

* add_order() function that adds a new order to the queue, and each added order is printed.
* process_order() function that takes the order from the queue, processes it and prints the completed order (simulate processing time with a delay of two seconds). 
* Processing ends when all orders in queue have been processed.

## 04-03. Reflection task

* How do you implement priority for the orders?
* How orders can be prepared in parallel in the order of their arrival, but they have a separate completion time, i.e. the final order can be different.
* Can a data structure other than a queue be used to build the restaurant's ordering system?