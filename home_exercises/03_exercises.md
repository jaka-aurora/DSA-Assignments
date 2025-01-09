## 03-01. Multiplication Table

Goal of the exercise is to create a program that generates and prints a multiplication table of the numbers 1-n, where n is a number defined by the user. 

Create function `generate_multiplication_table(n)`, which takes the number n as a parameter and creates a 2D list (multiplication table).

The output of the program should be well formatted so that it is easy to read. 

Example Output:

```
    1    2    3    4    5    6    7    8    9   10
    2    4    6    8   10   12   14   16   18   20
    3    6    9   12   15   18   21   24   27   30
    4    8   12   16   20   24   28   32   36   40
    5   10   15   20   25   30   35   40   45   50
    6   12   18   24   30   36   42   48   54   60
    7   14   21   28   35   42   49   56   63   70
    8   16   24   32   40   48   56   64   72   80
    9   18   27   36   45   54   63   72   81   90
   10   20   30   40   50   60   70   80   90  100
```

More to think about: Is it possible to save results in 1D list and still get the same output?

## 03-02. Search Algorithm Comparison

In this task you will learn how important it is to evaluate the performance of algorithms.

Goal: The purpose of the exercise is to learn how to search values from a list using two different algorithms called linear search and binary search.

Task Description

Linear Search: 

* Implement a function that searches the list for the given value linearly. 
* the function goes through each value in the list one 
* it can stop until it finds the value it's looking for or the entire list is gone through.
* The function calculates and prints how many loops are needed to find the value or to go through the list.

Binary search:

* Implement a function that searches for a given value in a list using a binary search. 
* it requires the list to be sorted beforehand. 
* The function splits the list in half and compares the middle value with the value to be searched for, and it then continues searching the right or left part of the list.
* The function calculates and prints how many loops are needed to find the value or to go through the list.

Input

```python
unsorted_list = [34, 7, 10, 17, 21, 5, 16, 75, 23, 32, 5, 62]
```

Output when searched with value `23`: 

```
Number of loops: 9
Linear search: The value 23 is found in the index 8.

Number of loops: 3
Binary search: The value 23 is found in index 7.
```

Note that in binary search there is different index because the list is sorted before the search algorithm is called. 

Extra Question: How many iteration does the binary or linear search take at most with lists of different sizes? How you can test that quickly? 


## 03-03. Search with Card Deck

Take out a deck of cards. You are free to shuffle the deck and then start practicing the operation of the search algorithms.

Implement search algorithms using a deck of cards. 
Both the number value of the card and the suit affect the order. 
So you have to decide in advance what the order of the suits is (otherwise you can apply binary search algorithm).

See more info standard 52-card deck: https://en.wikipedia.org/wiki/Standard_52-card_deck