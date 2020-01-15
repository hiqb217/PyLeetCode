"""
Problem 20: Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '{': [0, 0],
            '[': [0, 1],
            '(': [0, 2],
            '}': [1, 0],
            ']': [1, 1],
            ')': [1, 2]
        }
        open_list = []  # store list of open parenthesis in order

        if not s:  # edge case input ''
            return True

        for i in range(len(s)):
            if dict[s[i]][0] == 0:  # if open bracket
                open_list.append(dict[s[i]][1])

            # first closed bracket must be last element of open list
            elif open_list and dict[s[i]][1] == open_list[-1]:
                open_list.pop(-1)

            else:
                return False

        if not open_list:  # if open list not empty then there is unclosed open brackets
            return True

        return False
