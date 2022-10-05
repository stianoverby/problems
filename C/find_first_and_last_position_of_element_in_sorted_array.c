/*  34. FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given     target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Note: The returned array must be malloced, assume caller calls free().
    
    Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
        nums is a non-decreasing array.
        -109 <= target <= 109
    
    Source: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 */

void binary_search(int* nums, int* output, int target, int left, int right);

int* searchRange(int* nums, int numbers_size, int target, int* return_size){
    
    int left, right;
    int *output;
    
    left = 0;
    right = numbers_size - 1;
        
    *return_size = 2;
    output = malloc(sizeof(int) * (*return_size));
    output[0] = output[1] = -1;
    
    binary_search(nums, output, target, left, right);
    
    return output;

}


void binary_search(int* nums, int* output, int target, int left, int right)
{
    if (right < left) return; 
    
    int mid = (left + right) / 2;
    if(nums[mid] == target)
    {
        if (-1 == output[0] || mid < output[0]) 
            output[0] = mid;
        
        if (-1 == output[1] || mid > output[1])
            output[1] = mid;
    }
    
    if(nums[mid] <= target) 
        binary_search(nums, output, target, mid + 1, right);
                                   
    if(nums[mid] >= target) 
        binary_search(nums, output, target, left, mid - 1);
}

