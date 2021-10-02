"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

source: https://leetcode.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k % len(nums)
        # reverse nums.
        nums = reverse_placement(nums, 0, len(nums)-1)
        
        # reverse the position of the first k-1 elements.
        nums = reverse_placement(nums, 0, k - 1)
        
        # reverse the remaining elements of the list.
        nums = reverse_placement(nums, k, len(nums)-1)
        """
        Nums have now been shifted k places to the right through this cool algorithm.
        If you do not understand it, draw elements on pieces of paper and 
        do it manually. This is really cool.
        """
    
def reverse_placement(nums: List[int], low: int, high:int) -> List[int]:
    while low < high:
        tmp = nums[low]
        nums[low] = nums[high]
        nums[high] = tmp
        low += 1
        high -= 1
    return nums
            
            
        
