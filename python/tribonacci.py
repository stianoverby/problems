"""1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:
    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, 
    ie. answer <= 2^31 - 1.

Source: https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        trib_sequence = [0 for _ in range(n + 1)]
        trib_sequence[1] = trib_sequence[2] = 1

        for i in range(len(trib_sequence) - 3):
            trib_sequence[i + 3] = (
                trib_sequence[i] + trib_sequence[i + 1] + trib_sequence[i + 2]
            )

        return trib_sequence[n]
