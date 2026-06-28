"""
1. Odd or Even Counter

Given a list of numbers, count how many are odd and how many are even. Return both counts.

Input: [1, 2, 3, 4, 5, 6]
Output: odds = 3, evens = 3

"""

numbers = [6, 8, 10, 11]
evens = 0
odds = 0

for number in numbers:
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"evens: {evens}, odds: {odds}")