# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        cur = res_head
        a , b = l1 , l2
        carry = 0

        while a or b or carry:
            x = a.val if a else 0
            y = b.val if b else 0
            ans = x + y + carry

            carry = ans // 10 
            dig = ans % 10

            cur.next = ListNode(dig)

            cur = cur.next
            if a :
                a = a.next
            if b :
                b = b.next
        return res_head.next
