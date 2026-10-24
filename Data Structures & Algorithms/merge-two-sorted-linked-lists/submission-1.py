# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 != None and list2.val < list1.val:
            tmp = list1
            list1 = list2
            list2 = tmp
        
        head = list1

        while list2 is not None:
            if list2.val >= list1.val:
                tmp = list1.next
                list1.next = list2
                list1 = list1.next
                list2 = tmp
        
        return head
            