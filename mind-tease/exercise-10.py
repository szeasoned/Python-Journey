"""
7. Find the Two Smallest Numbers

Given a list, find the two smallest numbers WITHOUT sorting the list and WITHOUT using min() or sorted().

Input: [4, 8, 1, 9, 3, 7]
Output: [1, 3]
"""
nums = [4, 8, 1, 9, 3, 7]
first = nums[0]
second = nums[1]

for num in nums:
    if num < first:
        second = first
        first = num
    elif num < second:
        second = num

print(first, second)