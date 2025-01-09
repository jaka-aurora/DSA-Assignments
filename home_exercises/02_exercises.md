# Exercises 02 - Arrays

## 02-01. Command Line Arguments

Target of the exercise is handle command line arguments (`sys.argv`) and use lists in Python. 
The task is to create a program that combines the arguments given as input into a string separated by commas.

* The program takes command line arguments and concatenates them into a string.
* Each argument is appended consecutively, separated by a comma.
* Finally, the program prints the generated string.

How to run with output:

```
python 02_01_args_combine.py 1 5 10 aa bee cee
1,5,10,aa,bee,cee
```

## 02-02. Combine Multiple Lists

The objective of the task is to combine three lists into one list (without using any external libraries), and print the result.

* Go through all the three input lists given.
* Then each element of the list is added to the new combined list.

Input 

```python 
list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 10]
list_3 = [None, 'a', 'b', 'c', 'd']
```

Output:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 'a', 'b', 'c', 'd']
```

Extra question: how do you collect only unique values in a list?

## 02-03. Compare different Arrays

Python has several ways to store and manipulate data in array format where items are located sequentially in order. 

Do a comparison of three common data types: 

1. `list`, 
2. `array`, and 
3. `tuple`.

More to think about:

* Is there a real practical difference between these? 
* What use cases did you come up with for these?
