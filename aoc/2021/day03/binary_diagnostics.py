with open("input.txt") as f:
    content = f.readlines()
    
content = [line.strip() for line in content]


def solve1(content):
    most_common = ""
    
    for i in range(len(content[0])):
        
        zeros = ones = 0
        
        
        for number in content:
            if number[i] == '0':
                zeros += 1
            else:
                ones += 1

        most_common += "0" if zeros > ones else "1"

    most_common = int(most_common, 2)
    least_common = ~most_common + 2**12 # to convert to unsigned 12 bits integer
    
    return most_common * least_common


def solve2(content):

    def filter_pred(content, pred):
        
        remaining_numbers = content
        length_bitstring = len(content[0])

        for i in range(length_bitstring):

            zeros = list() 
            ones = list()

            if len(remaining_numbers)== 1: break

            for line in remaining_numbers:
                zeros.append(line) if line[i] == '0' else ones.append(line)

            remaining_numbers = ones if pred(ones, zeros) else zeros
                
        solution = int(remaining_numbers[0], 2)
        return solution

    most_common = filter_pred(content, lambda x,y: len(x) >= len(y))
    least_common = filter_pred(content, lambda x,y: len(x) < len (y))


    return most_common * least_common

print("Solution 1 : ", solve1(content))
print("Solution 2 :", solve2(content))
