"""
Given a string, return True if it reads the same forwards and backwards.

Input: "racecar"
Output: True

Input: "hello"
Output: False

use for loop, not ::-1
"""

def palindrome(text):
    text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return "False"
    return "True"

print(palindrome("rawr"))