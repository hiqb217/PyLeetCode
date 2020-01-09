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
        d = []
        x = 0
        while x**2 <= c:
            d.append(x**2)
            x += 1

        for i in range(len(d)):
            val = c - i**2
            if val in d:
                return True

        return False
