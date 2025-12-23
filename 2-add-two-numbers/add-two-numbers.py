# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        lnode = ListNode(0, None)
        d = lnode

        d1 = []
        d2 = []

        carry = 0

        while (l1 != None or l2 != None):
            if (l1 == None):
                d1.append(0)
            else:
                d1.append(l1.val)
            if (l1 != None):
                l1 = l1.next

            if (l2 == None):
                d2.append(0)
            else:
                d2.append(l2.val)
            if (l2 != None):
                l2 = l2.next

            if (d1[count] + d2[count] + carry >= 10):
                lnode.val = (d1[count]+d2[count]+carry)%10
                carry = 1
            else:

                lnode.val = d1[count]+d2[count]+carry
                carry = 0

            count += 1

            if (l1 != None or l2 != None or carry == 1):
                lnode.next = ListNode(0,None)
                if (carry == 1):
                    lnode.next.val = 1
                lnode = lnode.next

        return d
            
        