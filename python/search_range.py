'''
FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY.

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''


class Solution:
    
    def search_range(self, nums: List[int], target: int) -> List[int]:
        
        ans = [-1] * 2 
        if len(nums) == 0: return ans
        
        # Do two binary searches to find the range of target
        ans [0] = find_lowest(nums, target)
        ans [1] = find_highest(nums, target)
        
        return ans

    
def find_lowest(nums: List[int], target:int):
    
    low = 0
    high = len(nums) - 1
    
    lowest = -1 
    
    while low <= high:
        
        mid = low + (high-low) // 2
        
        # If we have found the target, check to the left if we have a lower
        # index with the target value
        if nums[mid] == target:
            lowest = mid
            high = mid - 1
            
        # If target is less than the current value, move to the left
        elif nums[mid] > target:
            high = mid - 1
        
        # If the target is larger then the current value, move to the right
        else:
            low = mid + 1
    
    return lowest


def find_highest(nums: List[int], target:int):
    
    low = 0
    high = len(nums) - 1
    
    highest = -1 
    
    while low <= high:
        
        mid = low + (high-low) // 2
        
        # If we have found the target, check to the right if we have a higher
        # index with the target value
        if nums[mid] == target:
            highest = mid
            low = mid + 1 
        
        # If target is less than the current value, move to the left
        elif nums[mid] > target:
            high = mid - 1
        
        # If target is larger than the current value, move to the right
        else: 
            low = mid + 1
        
    return highest
