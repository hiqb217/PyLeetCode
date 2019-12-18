#Problem 1
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    dict1 = {}  #dictionary magic
    for i in range(len(nums)):
        if nums[i] in dict1:
            return [dict1[nums[i]], i]
        else:
            dict1[target-nums[i]] = i


# Test case
nums = (4, 1, 2, 4, 3, 2)
target = 8

print(twoSum(nums, target))
