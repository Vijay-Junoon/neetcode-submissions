# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0)
        temp = newList
        t1 = list1
        t2 = list2

        while t1 and t2:
            if t1.val <= t2.val:
                temp.next = t1
                t1 = t1.next
            else:
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

        return newList.next