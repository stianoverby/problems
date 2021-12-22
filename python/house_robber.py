'''198. House Robber
You are a professional robber planning to rob houses 
along a street. Each house has a certain amount of 
money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses 
have security systems connected and it will automatically
contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount 
of money of each house, return the maximum amount of 
money you can rob tonight without alerting the police.

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if there is only one element, that has to be the answer
        if len(nums) == 1: return nums[0]
        
        amounts = [0 for _ in nums]
        
        
        amounts[0] = nums[0]
        amounts[1] = nums[1]
        
        # the largest prior element can never be adjecent to the current index.
        # Hence the first largest element, has to be the first.
        largest = amounts[0]
        
        for i in range(2, len(amounts)):
            amounts[i] = nums[i] + largest
            
            # Check if the the element before the current index is larger than the
            # current index. Update if true.
            largest = max(amounts[i-1], largest)
        
        return max(amounts[len(amounts) - 1], amounts[len(amounts) - 2])