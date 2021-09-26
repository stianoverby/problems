'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Source: https://leetcode.com/problems/move-zeroes/submissions/
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        sort_list(nums)

def sort_list(nums:List[int]):
    
    low = 0
    
    for index in range(len(nums)):
        # We found a non-zero number. Move it to the start of our array, left of any earlier moved non-zero number.
        if nums[index] != 0:
            swap(nums, low, index)
            low += 1
            
def swap(nums: List[int], low: int, non_zero_at):
    
    tmp = nums[low]
    nums[low] = nums[non_zero_at]
    nums[non_zero_at] = tmp
    
