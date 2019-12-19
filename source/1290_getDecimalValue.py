"""
Problem 1290: Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # curr = head
        # i = 0
        # end = 0
        # out = 0
        # while (curr != None):
        #     end += 1
        #     curr = curr.next
        # curr = head
        # while (curr != None):
        #     binVal = int(curr.val)
        #     if binVal == 1:
        #         outAdd = 2 ** (end - i - 1)
        #     else:
        #         outAdd = 0
        #     i += 1
        #     out += outAdd
        #     curr = curr.next
        # return out

        answer = 0
        while head:
            answer = 2*answer + head.val
            head = head.next
        return answer


        
