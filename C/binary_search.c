/*
* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
* You must write an algorithm with O(log n) runtime complexity.
*
* Constraints:
*
* 1 <= nums.length <= 104
* -104 < nums[i], target < 104
* All the integers in nums are unique.
* nums is sorted in ascending order.
*
* Source: https://leetcode.com/problems/binary-search/
*/

int binary_search(int* nums, int low, int high, int target)
{
    /*
    Base case, the target can not be this array
    */
    if (low > high)
        return -1;
    
    /*
    We want to look at the middle element
    */
    int middle = (low + high )  / 2;
    
    /*
    If the middle element is our target. We are finnished. 
    If not, move the low and high index accordingly.
    */
    if (nums[middle] == target)
        return middle;
    else if (nums[middle] < target)
        low = ++middle;
    else if (nums[middle] > target)
        high = --middle;
    
    return binary_search(nums, low, high, target);
}

/*
Driver code 
*/
int search(int* nums, int nums_size, int target)
{
    int low, high;
    
    low = 0;
    high = nums_size - 1;
    
    return binary_search(nums, low, high, target);
}
