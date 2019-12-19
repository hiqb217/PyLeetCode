"""
Problem 191: Number of 1 bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        out =0
        for i in range(32):
            if (n & 1):
                out +=1
            n=n >>1

        return out