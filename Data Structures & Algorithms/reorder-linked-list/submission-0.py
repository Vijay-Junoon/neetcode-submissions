# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        newList = ListNode(0)
        temp = newList

        t1 = head
        t2 = prev

        while t1 and t2:
            temp.next = t1
            t1 = t1.next
            temp = temp.next
            temp.next = t2
            t2 = t2.next
            temp = temp.next
            
        while t1:
            temp.next = t1
            t1 = t1.next
            temp = temp.next
        while t2:
            temp.next = t2
            t2 = t2.next
            temp = temp.next

        