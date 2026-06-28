"""
Find the Two Largest Numbers

Given a list, find the two largest numbers.

Input: [4, 8, 1, 9, 3, 7]
Output: [9, 8]
"""

nums = [4, 8, 1, 9, 3, 7]
first = nums[0]
second = nums[1]

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

print(first, second)