""" DON'T GET VOLUNTEERED!

As a henchman on Commander Lambda's space station, you're expected to be resourceful,
smart, and a quick thinker. It's not easy building a doomsday device and capturing
bunnies at the same time, after all! 
In order to make sure that everyone working for her is sufficiently quick-witted,
Commander Lambda has installed new flooring outside the henchman dormitories.
It looks like a chessboard, and every morning and evening you have to solve a new
movement puzzle in order to cross the floor. That would be fine if you got to be the
rook or the queen, but instead, you have to be the knight. Worse, if you take too much
time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP
doomsday device!

To help yourself get to and from your bunk every day, write a function called 
answer(src, dest) which takes in two parameters: the source square, on which 
you start, and the destination square, which is where you need to land to solve
the puzzle.  The function should return an integer representing the smallest 
number of moves it will take for you to travel from the source square to the
destination square using a chess knight's moves (that is, two squares in any
direction immediately followed by one square perpendicular to that direction,
or vice versa, in an "L" shape).  Both the source and destination squares will
be an integer between 0 and 63, inclusive, and are numbered like the example
chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Source: Google foobar challenge
"""

from collections import defaultdict, deque


def solution(src, dst):

    # The board is a grid.
    # Calculate the cooresponding coordinates.
    start = src // 8, src % 8
    destination = dst // 8, dst % 8

    # Initialize visited map, and queue used for traversing the grid
    visited = defaultdict(lambda: False)
    Q = deque()

    # Add the start coordinate to the queue; marks as visited
    visited[start] = True
    Q.append((start, 0))

    # Standard bfs
    while Q:
        current, depth = Q.popleft()

        if current == destination:
            return depth

        for coordinate in legal_moves(current):

            # Add coordinate to queue if not already visited; set the depth of the
            # coordinate to be depth + 1
            if not visited[coordinate]:

                visited[coordinate] = True
                Q.append((coordinate, depth + 1))


def legal_moves(coordinate):

    row, col = coordinate

    moves = [
        (row - 1, col - 2),
        (row - 1, col + 2),
        (row + 1, col - 2),
        (row + 1, col + 2),
        (row - 2, col - 1),
        (row - 2, col + 1),
        (row + 2, col - 1),
        (row + 2, col + 1),
    ]

    # Generate list that has only coordinates with valid range
    return [(x, y) for (x, y) in moves if x > -1 and x < 8 and y > -1 and y < 8]


assert solution(0, 1) == 3
assert solution(19, 36) == 1
