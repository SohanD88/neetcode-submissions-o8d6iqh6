# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        count = 0
        dumCur = dummy
        while curr:
            curr = curr.next
            count += 1

        count = count - n
        while count > 0:
            dumCur = dumCur.next
            count -= 1

        dumCur.next = dumCur.next.next

        return dummy.next




            

        