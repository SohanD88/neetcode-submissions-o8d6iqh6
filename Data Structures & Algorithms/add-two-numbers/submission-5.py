# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, None)
        dumCur = dummy
        curr1 = l1
        curr2 = l2

        carryOver = 0

        while curr1 or curr2:
            if not curr1:
                cursum = curr2.val + carryOver
                if cursum >= 10:
                    cursum = cursum - 10
                    carryOver = 1
                else:
                    carryOver = 0
                dumCur.next = ListNode(cursum, None)
                dumCur = dumCur.next
                curr2 = curr2.next

            elif not curr2:
                cursum = curr1.val + carryOver
                if cursum >= 10:
                    cursum = cursum - 10
                    carryOver = 1
                else:
                    carryOver = 0
                dumCur.next = ListNode(cursum, None)
                dumCur = dumCur.next
                curr1 = curr1.next

            else:
                cursum = curr1.val + curr2.val + carryOver
                if cursum >= 10:
                    cursum = cursum - 10
                    carryOver = 1
                else:
                    carryOver = 0
                dumCur.next = ListNode(cursum, None)
                dumCur = dumCur.next

                curr1 = curr1.next
                curr2 = curr2.next

        if carryOver > 0:
            dumCur.next = ListNode(carryOver, None)

        return dummy.next

