'''213. House Robber II
You are a professional robber planning to rob houses 
along a street. Each house has a certain amount of
money stashed. All houses at this place are arranged
in a circle. That means the first house is the neighbor
of the last one. Meanwhile, adjacent houses have a
security system connected, and it will automatically
contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of
money of each house, return the maximum amount of money
you can rob tonight without alerting the police.

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Helper function for finding highest possible profit
        def find_profit(amounts, nums):
            
            largest = amounts[0]
            
            for i in range(2, len(amounts)):
                amounts[i] = nums[i] + largest
                largest = max(amounts[i-1], largest)
                
            return max(amounts[len(amounts) - 1], amounts[len(amounts) - 2]) 
        
        # base cases that is not handled by later logic 
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # since house[0] and house[n-1] are adjecent, they
        # can not be robbed together. Dividing into to possible
        # section of houses.
        amount_left = [0 for _ in range(len(nums) - 1)]
        houses_left = nums[:-1] 
        
        amount_right = [0 for _ in range(len(nums) - 1)]
        houses_right = nums[1:]
        
        # initialize the two first houses' profit
        amount_left[0] = houses_left[0]
        amount_left[1] = houses_left[1]
        
        amount_right[0] = houses_right[0]
        amount_right[1] = houses_right[1]
        
        
        return max(find_profit(amount_left, houses_left), find_profit(amount_right, houses_right))