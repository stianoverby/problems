'''80. Climbing stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Constraints:
    1 <= n <= 45

Source: https://leetcode.com/problems/climbing-stairs/
'''

int climbStairs(int n){
     
    if (n == 1 || n == 2) return n;
    
    int steps[n+1];
        
    steps[1] = 1; 
    steps[2] = 2;
    
    for(int i = 3; i <= n; i++)
        steps[i] = steps[i-1] + steps[i-2];
    
    return steps[n];
}