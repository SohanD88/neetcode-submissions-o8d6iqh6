# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        temp = curr
        end = curr.next

        while curr.next and curr.next.next:
            while end and end.next:
                temp = end
                end = end.next


            end.next = curr.next
            curr.next = end
            temp.next = None
            
            curr = end.next
            temp = curr

