'''746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

Source: https://leetcode.com/problems/min-cost-climbing-stairs/


'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cheapest_cost = [0 for _ in range(len(cost))]
        
        cheapest_cost[0] = cost[0]
        cheapest_cost[1] = cost[1]
        
        for i in range(2, len(cheapest_cost)):
            cheapest_cost[i] = cost[i] + min(cheapest_cost[i-1], cheapest_cost[i-2])
            
        return min(cheapest_cost[len(cheapest_cost) - 1], cheapest_cost[len(cheapest_cost) - 2])
         