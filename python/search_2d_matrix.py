"""
SEARCH A 2D MATRIX
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


source: https://leetcode.com/problems/search-a-2d-matrix/

"""


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find list in matrix with correct range
        index_in_matrix = find_row_to_search(matrix, target)

        # If minus one, none of the arrays has the wanted range. Else
        # we binary search through the correct list.
        if index_in_matrix != -1:
            return binary_search(matrix[index_in_matrix], target)

        return False


def find_row_to_search(matrix: List[List[int]], target):

    low = 0
    high = len(matrix) - 1
    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if matrix[mid][0] <= target:
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    return ans


def binary_search(numbers: List[int], target) -> bool:

    low = 0
    high = len(numbers) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if numbers[mid] == target:
            return True

        elif numbers[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return False
