"""
1. Count Vowels ⭐ (Easy)

Count how many vowels are in a string.

Example

Input: "computer"
Output: 3

"""

def count_vowels(text):
    text.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

print(count_vowels("computer"))