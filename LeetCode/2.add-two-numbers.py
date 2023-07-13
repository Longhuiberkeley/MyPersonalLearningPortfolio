#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Note
# Use % to get the last digit
# 18 % 10 =8 

# Use // to get the 1 
# 16//10 = 1
# 9//10 = 0

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        output = ListNode(0) # To init the output
        residual = 0

        # we then push the next value
        while l1 != None or l2 != None or residual !=0:
            l1 

        if l1.next == None and l2.next == None:

        if l1.next != None:
            l1 = l1.next
        if l2.next != None:
            l2 = l2.next
            next_value = l1.val + l2.val + residual

            output.next = next_value % 10
            residual = next_value // 10
            
        return output
            

# @lc code=end
