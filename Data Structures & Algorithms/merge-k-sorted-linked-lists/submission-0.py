# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        pq = []
        for i in lists:
            temp = i
            while temp:
                heapq.heappush(pq,temp.val)
                temp = temp.next
        
        newList = ListNode(0)
        temp = newList
        while pq != []:
            temp.next = ListNode(heapq.heappop(pq))
            temp = temp.next
        return newList.next

