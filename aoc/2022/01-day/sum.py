def create_elfs(file):

    elfs = []
    elf = []

    for line in file:

        # Remove white space like new lines 
        line = line.rstrip()

        # If the string is not empty, add it the current elf
        if line:
            elf.append(int(line))
            continue
        
        # String is empty, add current elf, and create new elf
        elfs.append(elf)
        elf = []
    
    return elfs


filename = "input"

# In a list represent each elf as a list of integers
with open(filename) as file:
    elfs = create_elfs(file)

# Map each elf to the sum of their content, and sort the new list
sums = sorted(map(sum, elfs))

# The elf at the end of the list is the one with the most amount of calories. The
# two previous are the following with the most amount of calories, since the list is ordered
# ascendingly
solution_1 = sums[-1]
solution_2 = sum(sums[-3 : ])

print("Solution question 1 :", solution_1)
print("Solution question 2 :", solution_2)


