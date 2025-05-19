'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # edge case 1 : empty list 
        if not nums or len(nums) == 0:
            return 
        # edge case 2 : list with single element
        if len(nums) == 1:
            return nums[0]
        
        # first two indices < ensure O(1) space complexity
        i,j = 0,1

        while j < len(nums):
            if nums[i] != nums[j]:
                return nums[i]
            i += 2 #< ensures O(logn)
            j += 2

        # edge case 3: last element is single non-duplicate
        return nums[i]
