# Exercises 01 - Algorithms

These are the so-called lesson exercises, and they can also be done during the lesson.

* If you complete two exercise out of three (2/3) by the given time limit, you can mark yourself one point from the lesson exercises. 
* If you complete one exercise out of two (1/2) by the given time limit, you can mark yourself one point from the lesson exercises.

An almost correct answer is enough, i.e. there is no need to aim for perfection but attempting the exercises is the most important thing because improving your skills requires continuous practice.

* Exercises must be returned to the GitLab repository before the next lecture
* There are no model solutions for the exercises, but the solutions for some of the exercises can be reviewed in the lesson.

## 01-01. Byte, Kilobyte, Megabyte, Gigabyte converter

Implement a program that calculates the kB/MB/GB based on the input bytes.

You give bytes as in input and then your program calculates bytes in a kilobyte, megabyte and gigabyte.
For counting, you must use real megabyte, gigabyte and terabyte definitions (so for example 2^20 or 2^30).
Use 6 decimal for precision.
See information [How to calculate Bytes](http://www.whatsabyte.com/).

An Example of Program Execution:

```
Give your input in bytes>5206000
bytes 		 5206000 B
Kilobytes	 5083.984375 KB
Megabytes	 4.964828 MB
Gigabytes	 0.004848 GB
```

## 01-02. Grade calculator

Make a program that calculates the grade based on the exam and assignment points.

Ask the user for two points:

* exam points  (0-24) and
* assignment points (0-12)

Then calculate the total grade between 0-5 based on the following table:

```
limit
[32,36] 	5
[28,32) 	4
[24,28) 	3
[18,22) 	2
[15,18) 	1
[0,15)   	0
```

An Example of Program Execution:

```
How many exam points did you get (0-24)?15
How many assignment points did you get (0-12)?11
With total points 26, the final grade was 3
```

Extra Question: How to handle errors (negative numbers and not numbers) in input?

## 01-03. Create Study Algorithm

Create an algorithm for your own study process for this course.

* Also, think about how you limit the algorithm?

See there five properties of algorithm:

* Finiteness: the algorithm must always end with a finite number of steps. The amount can be large, but still limited.
* Precision: each step of the algorithm must be precisely defined. Actions must be described without many interpretations for each case.
* Inputs: the algorithm has zero or more inputs, i.e. initial values or values are deduced dynamically during execution.
* Outputs: the algorithm has one or more outputs, i.e. values related to the inputs.
* Efficiency: the algorithm is expected to be efficient in that its operations are simple and in principle can be performed in a limited amount of time using pen and paper.

Source: https://fi.wikipedia.org/wiki/Algoritmi or same in english.