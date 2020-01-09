"""
Problem 633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: 3
Output: False
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lower = 0
        upper = floor(c**0.5)
        while lower <= upper:
            test = lower*lower + upper * upper
            if test < c:
                lower += 1
            elif test > c:
                upper -= 1
            else:
                return True
        return False
