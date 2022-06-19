""" PREPARE THE BUNNIES

You’re awfully close to destroying the LAMBCHOP doomsday device
and freeing Commander Lambda’s bunny prisoners, but once they’re
free of the prison blocks, the bunnies are going to need to
escape Lambda’s space station via the escape pods as quickly as
possible. Unfortunately, the halls of the space station are a
maze of corridors and dead ends that will be a deathtrap for
the escaping bunnies. Fortunately, Commander Lambda has put
you in charge of a remodeling project that will give you the
opportunity to make things a little easier for the bunnies.
Unfortunately (again), you can’t just remove all obstacles
between the bunnies and the escape pods - at most you can remove
one wall per escape pod path, both to maintain structural integrity
of the station and to avoid arousing Commander Lambda’s suspicions.

You have maps of parts of the space station, each starting at a
prison exit and ending at the door to an escape pod. The map is
represented as a matrix of 0s and 1s, where 0s are passable space
and 1s are impassable walls. The door out of the prison is at the
top left (0,0) and the door into an escape pod is at the bottom 
right (w-1,h-1).

Write a function solution(map) that generates the length of the
shortest path from the prison door to the escape pod, where you
are allowed to remove one wall as part of your remodeling plans.
The path length is the total number of nodes you pass through,
counting both the entrance and exit nodes. The starting and ending
positions are always passable (0). The map will always be solvable,
though you may or may not need to remove a wall. The height and
width of the map can be from 2 to 20. Moves can only be made in
cardinal directions; no diagonal moves are allowed.

Source: Google foobar challenge
"""

from collections import deque


def solution(map):

    height = len(map)
    width = len(map[0])

    start = 0, 0
    end = height - 1, width - 1

    # Generate a distance map using bfs from both start and end point
    D = bfs(start, map)
    E = bfs(end, map)

    dist = float("inf")
    for x in range(height):
        for y in range(width):

            # If both distance map cointains an entry for the point, check if
            # the sum of the two entries are the smallest value seen. The smallest
            # value is our solution.
            if D[x][y] and E[x][y]:
                dist = min(dist, (D[x][y] + E[x][y] - 1))

    return dist


def bfs(start, map):

    height = len(map)
    width = len(map[0])

    distance_map = [[False for _ in range(width)] for _ in range(height)]

    x, y = start
    distance_map[x][y] = 1

    # Initialize queue
    Q = deque()
    Q.append(start)

    while Q:
        cur_x, cur_y = Q.popleft()

        # Iterate over all possible moves
        for m, n in [(0, 1), (1, 0), (-1, 0), (0, -1)]:

            # Genarate new coordinates
            x, y = cur_x + m, cur_y + n

            # Update distance map if coordinates are in legal range, and they are
            # not in distance map
            if -1 < x < height and -1 < y < width and distance_map[x][y] is False:
                distance_map[x][y] = distance_map[cur_x][cur_y] + 1

                # Only add to queue if coordinate is empty space
                if map[x][y] == 0:
                    Q.append((x, y))

    return distance_map


# Should pass these minimal tests
assert solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
assert (
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    == 11
)
