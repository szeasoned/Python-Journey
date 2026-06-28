"""
2. Sum of Digits

Given an integer, add up all its digits and return the total.

Input: 1234
Output: 10  (1+2+3+4)

Input: 9901
Output: 19
"""

def sum_digits(nums):
    nums = str(nums)
    total = 0
    for num in nums:
        num = int(num)
        total += num
    return total
print(sum_digits(1234))