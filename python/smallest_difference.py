''' Smallest Difference

Write a function that takes in two non-empty arrays of integers,
finds the pair of nubers (one from each array) whose absolute
difference is closest to zero, and returns an array containing
these two numbers, with the number from the first array in the
first position.

Note that the absolute difference of two integers is the distance
between them on the real number line.

You can assume that there will only be one pair of numbers with the
smallest difference.

Source: algoexpert

'''


def smallestDifference(arrayOne, arrayTwo):

    # Sort the input arrays
    arrayOne.sort()
    arrayTwo.sort()

    # Let there be one ptr pointing at the highest index of each array
    p1 = len(arrayOne) - 1
    p2 = len(arrayTwo) - 1

    # Distance vector
    Distance = []

    # Continue calculating distance as long as indexes are positive
    while p1 >= 0 and p2 >= 0:

        # Calculate difference between the numbers; add the
        # distance and the number pair to the distance vector
        difference = abs(arrayOne[p1] - arrayTwo[p2])
        Distance.append((difference, [arrayOne[p1], arrayTwo[p2]]))

        # Decrease p1 if what is at position p2 is larger than what is at p2
        if arrayOne[p1] > arrayTwo[p2]:
            p1 -= 1

        # Value at p2 is larger or equal to what at p1
        else:
            p2 -= 1

    _, pair = min(Distance)
    return pair
