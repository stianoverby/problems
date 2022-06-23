import sys

lines = [line.split() for line in sys.stdin]
numbers = [int(x) for x in lines[0]]
numbers.sort() 
print(numbers[0], numbers[1])