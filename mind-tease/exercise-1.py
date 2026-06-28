"""
Problem: Given a list of integers nums and a target integer target,
return the indices of the two numbers that add up to target.
Assume exactly one solution exists, and you can't use the same element twice.

Example:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
"""

nums = [0, 1, 7, 8, 10]
target = 9

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and nums[i] + nums[j] == target:
            print(i, j)