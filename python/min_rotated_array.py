""" Find minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return find_lowest(nums)


def find_lowest(nums: List[int]) -> int:

    low = 0
    high = len(nums) - 1
    first_element_in_array = nums[0]

    while nums[low] > nums[high]:

        mid = low + (high - low) // 2

        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
