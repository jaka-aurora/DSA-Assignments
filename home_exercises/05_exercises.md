## 05-01. Filtering Environment Variables

Implement a program that filters and displays certain keys with values from the environment variables of the
computer.

The program retrieves the environment variables and filters certain keys from them.
Filtered key values are limited to a maximum of 80 characters. `os.environ` retrieves environment variables from the system.

Filter only specific keys (eg `'OS', 'PATH', 'USERPROFILE', 'HOMEPATH', 'NUMBER_OF_PROCESSORS'`) from the environment
variables if the keys are found on your system.

## 05-02. Dictionary Program

Implement a dictionary program that translates Finnish words into English using Python's dictionary (`dict`) data
structure.
In Data Structure term it's called as associative array.

Program overview:

* Define a dictionary that contains Finnish words and their English equivalents.
* The program asks the user for a Finnish word and returns the corresponding English translation or "Word not found.".
* If the word is not found in the dictionary, the program informs the user.
* The user can end the program by typing "exit".

Step-by-step instructions:

Input for associative array:

```
kissa: cat
koira: dog
maa: country
kieli: language
aikasarja: time series
tila: status
tuote: product
palvelin: server
salasana: password
```

Output:

```
Give a Finnish Word> kissa
cat
Give a Finnish Word> koira
dog
Give a Finnish Word> auto
Word not found.
Give a Finnish Word> exit
Exit.
```

Extra: Generate also support to English-Finnish dictionary based on the given program.

## 05-03. Dictionaries in List

In this task, personal information is created by combining first names, last names, and programming languages.
The steps of the task are as follows:

1. Define lists of first names, last names and programming languages which they originally developed.

```python
first_names = ['Linux', 'Anders', 'Larry', 'Guido', 'Rasmus', 'Pekka', 'Grace', 'Dennis', 'Bjarne']
last_names = ['Torvalds', 'Hejlsberg', 'Wall', 'Von Rossum', 'Lerdorf', 'Klärck', 'Hopper', 'Ritchie', 'Stroustrup']
langs = ['Linux', 'C#', 'Perl', 'Python', 'PHP', 'Robot Framework', 'COBOL', 'C', 'C++']
```

2. Combine first and last names and programming languages to form personal records as dictionaries.

3. Sort the information:

* a) Sort the personal data according to the programming language and print the result.
* b) Sort the data by name in reverse order and print this result.

Output

```
Sorted by language: [{'name': 'Ritchie, Dennis', 'language': 'C'}, {'name': 'Hejlsberg, Anders', 'language': 'C#'}, {'name': 'Stroustrup, Bjarne', 'language': 'C++'}, {'name': 'Hopper, Grace', 'language': 'COBOL'}, {'name': 'Torvalds, Linux', 'language': 'Linux'}, {'name': 'Lerdorf, Rasmus', 'language': 'PHP'}, {'name': 'Wall, Larry', 'language': 'Perl'}, {'name': 'Von Rossum, Guido', 'language': 'Python'}, {'name': 'Klärck, Pekka', 'language': 'Robot Framework'}]
Reversed by name: [{'name': 'Wall, Larry', 'language': 'Perl'}, {'name': 'Von Rossum, Guido', 'language': 'Python'}, {'name': 'Torvalds, Linux', 'language': 'Linux'}, {'name': 'Stroustrup, Bjarne', 'language': 'C++'}, {'name': 'Ritchie, Dennis', 'language': 'C'}, {'name': 'Lerdorf, Rasmus', 'language': 'PHP'}, {'name': 'Klärck, Pekka', 'language': 'Robot Framework'}, {'name': 'Hopper, Grace', 'language': 'COBOL'}, {'name': 'Hejlsberg, Anders', 'language': 'C#'}]
```