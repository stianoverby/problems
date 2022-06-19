"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

source : https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:

        target_color = image[sr][sc]

        # if the color of our start pixel already is the new color, then we do not have to do anything
        if target_color == new_color:
            return image

        # stack for our DFS
        stack = list()

        # range of x, y coordinates
        image_width = range(0, len(image))
        image_height = range(0, len(image[0]))

        # put coordinate on our stack
        stack.append((sr, sc))

        while len(stack):

            # take the coordinate from the top of our stack, and set it to the new color
            x, y = stack.pop()
            image[x][y] = new_color

            # Check if horizontal neighboors are valid and have target color
            for i in range(x - 1, x + 2):

                if i in image_width and image[i][y] == target_color:

                    stack.append((i, y))

            # Check if vertical neighboors are valid and have target color
            for i in range(y - 1, y + 2):

                if i in image_height and image[x][i] == target_color:

                    stack.append((x, i))

        return image
