# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0)
        temp = newList
        t1 = l1
        t2 = l2
        d,c = 0,0
        while t1 or t2 or c:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            t_sum = val1 + val2  + c
            c = t_sum//10
            d = t_sum%10
            temp.next = ListNode(d)
            temp = temp.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        return newList.next