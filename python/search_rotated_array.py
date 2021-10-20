'''
SEARCH IN ROTATED SORTED ARRAY

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104


source: https://leetcode.com/problems/search-in-rotated-sorted-array/

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0: 
          return -1
        
        return binary_search(nums, target)
      

def binary_search(nums: List[int], target: int) -> int:
    
    low = 0
    high = len(nums) - 1
    
    first = nums[0]
    
    while low <= high:
        
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        
        # Mid elem is larger than first elem, and target is greater than first elem
        # OR 
        # Mid elem is less than first elem, and target is less than first elem
        if (nums[mid] >= first) == (target >= first):
            
            if nums[mid]< target:
                low = mid + 1
            else:
                high = mid - 1
                
        # Mid elem is larger than first element, and target is less than first elem
        # OR
        # Mid elem is less than first elem, and target is greater than first elem
        else:
            if nums[mid] >= first:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1        
