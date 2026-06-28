"""
6. Flatten a Nested List (one level deep)

Given a list of lists, return a single flat list with all the values.

Input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]

Constraint: no libraries, no list comprehension tricks — just loops.

"""

lists = [[1, 2], [3, 4], [5, 6]]
new_list = []
for list in lists:
    for num in list:
        new_list.append(num)
print(new_list)