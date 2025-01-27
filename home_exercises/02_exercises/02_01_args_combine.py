## Your answers 

## Update your home exercises in this directory when you have completed the given exercises.

## * Return tasks as source code (.py) or text file (.txt), depending on the exercise

import sys

def main():
    args = sys.argv[1:]
    result = ",".join(args)
    print(result)

if __name__ == '__main__':
    main()