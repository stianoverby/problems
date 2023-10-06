/* Binary search
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


int search(int *nums, int nums_size, int target);
int binary_search(int *nums, int low, int high, int target);

int search(int *nums, int nums_size, int target)
{
    int low, high;

    low = 0;
    high = nums_size - 1;

    return binary_search(nums, low, high, target);
}

int binary_search(int *nums, int low, int high, int target)
{
    if (low > high)
        return -1;

    int middle = (low + high) / 2;

    if (nums[middle] == target)
        return middle;
    else if (nums[middle] < target)
        low = ++middle;
    else if (nums[middle] > target)
        high = --middle;

    return binary_search(nums, low, high, target);
}
