"""
Problem 1108. Defanging an IP Address
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

"""
class Solution:
    def defangIPaddr(self,address: str) -> str:
        def find(s, ch):
            return [i for i, ltr in enumerate(s) if ltr == ch]

        inds = find('.',address)
        out_address = ''
        start = 0
        end = inds[0]
        for i in range(len(inds)-1):
            out_address += address[start:end] + '[.]'
            start = inds[i] +1
            end = inds[i+1]
        return out_address
