"""
Find the Third Smallest Number

Without sorting.

Input: [10, 4, 8, 1, 9, 3, 7]
Output: 4
"""

nums = [100, 200, 300, 1, 2, 3]
first = nums[0]
second = nums[1]
third = nums[2]

for num in nums:
    if num < first:
        third = second
        second = first
        first = num
    elif num < second:
        third = second
        second = num
    elif num < third:
        third = num

print(third)