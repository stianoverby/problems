""" FIND PEAK ELEMENT

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

Source: https://leetcode.com/problems/find-peak-element/

"""


class Solution:

    # Driver code
    def find_peak_element(self, nums: List[int]) -> int:
        return binary_search(nums)


def binary_search(nums: List[int]) -> int:

    low = 0
    high = len(nums) - 1

    while low <= high:

        """
        We find the middle index by adding the range between high and low divided by two, to low.
        This method is not so important when using python, but in other languages, this would
        prevent overflow issues that could arise when working with very large indecies
        """

        mid = low + (high - low) // 2

        # Check if the middle element is less than the one to the right.
        # Go right if that is the case.
        if mid < high and nums[mid] < nums[mid + 1]:
            low = mid + 1

        # Check if the middle element is less than the on to the left.
        # Go left if that is the case.
        elif mid > low and nums[mid] < nums[mid - 1]:
            high = mid - 1

        # Else we are at the very definiton of a peak.
        else:
            return mid
