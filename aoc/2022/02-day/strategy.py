def read_file(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]

def shape_score(letter):
    return ord(letter) - ord('A') + 1

def is_winning_choice(opponent, you):
    return ord(you) - ord('A')  == (ord(opponent) - ord('A') + 1) % 3

def draw(opponent):
    return 3 + shape_score(opponent)

def win(opponent):
    '''
        Let P be a circuluar array [ROCK, PAPER, SCISSORS]. For you to win, you have to chose the option immediately to
        the right of your oponent's choice. In our array, each option is represented with a letter A, B or C. Each letter
        corresponds to an index. Map the opponents letter to that index, add one, and map it back to a letter.
    '''
    letter_to_win = chr((ord(opponent) - ord('A') + 1) % 3 + ord('A'))
    return 6 + shape_score(letter_to_win)

def loss(opponent):
    letter_to_loose = chr((ord(opponent) - ord('A') - 1) % 3 + ord('A'))
    return shape_score(letter_to_loose)

def solve1(file):
    
    total_score = 0
    XYZ_to_ABC_map =    {   "X" : "A", 
                            "Y" : "B", 
                            "Z" : "C"  }

    for line in file:
        opponent_choice, _ , encoded_choice = line
        your_choice = XYZ_to_ABC_map[encoded_choice]

        score = shape_score(your_choice) 

        if your_choice == opponent_choice:
            score += 3
        elif is_winning_choice(opponent_choice, your_choice):
            score += 6
        
        total_score += score

    return total_score

def solve2(file):
    
    total_score = 0
    decision_to_action_map = {  "Z": win,
                                "X" : loss,
                                "Y" : draw  }

    for line in file:
        opponent, _, decision = line
        action = decision_to_action_map[decision]
        total_score += action(opponent)
    
    return total_score


''' DRIVER CODE '''

filname = "input"

file = read_file(filname)
solution1 = solve1(file)
solution2 = solve2(file)

print("SOLUTION 1 :", solution1)
print("SOLUTION 2 :", solution2)