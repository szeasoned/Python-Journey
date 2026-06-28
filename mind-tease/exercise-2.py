"""
Problem: Given a list of numbers, find the biggest one — without using max().

Input: [3, 7, 2, 9, 4]
Output: 9

"""

def get_highest(nums):
    highest = nums[0]

    for num in nums:
        if num > highest:
            highest = num
    return highest

print(get_highest([61, 67, 1, 4, 6, 10]))

