# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:09:01 2023

@author: sjnam
"""
# 4/16

#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
 
a = Solution()                
print(a.twoSum([2,7,11,15], 9))

