# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        myList = ListNode(0)
        myList.next = head
        temp = myList
        fast =  temp
        i = 0
        while i < n:
            fast = fast.next
            i+=1
        slow = temp
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return temp.next