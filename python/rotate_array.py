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
        nums = rotate(nums, 0, len(nums)-1)
        nums = rotate(nums, 0, k - 1)
        nums = rotate(nums, k, len(nums)-1)
    
def rotate(nums: List[int], low: int, high:int) -> List[int]:
    while low < high:
        tmp = nums[low]
        nums[low] = nums[high]
        nums[high] = tmp
        low += 1
        high -= 1
    return nums
            
            
        
