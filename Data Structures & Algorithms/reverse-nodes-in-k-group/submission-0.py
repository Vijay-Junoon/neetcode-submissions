# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prevGroup = dummy
        while True:
            kth = prevGroup
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            nextGroup = kth.next
            prev = nextGroup
            curr = prevGroup.next
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp


            