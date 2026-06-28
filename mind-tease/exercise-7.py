"""
4. Remove Duplicates From a List

Given a list, return a new list with duplicates removed — but keep the original ORDER of first appearances.

Input: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
Output: [3, 1, 4, 5, 9, 2, 6]

"""

def remove_dup(nums):
    new_nums = []
    for num  in nums:
        if num not in new_nums:
            new_nums.append(num)
    return new_nums

print(remove_dup([1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 4, 3, 2, 8]))