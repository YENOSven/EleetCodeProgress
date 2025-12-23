# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        s2 = ''
        c1 = l1
        c2 = l2
        while c1 is not None:
            s1 += str(c1.val)
            c1 = c1.next 
        while c2 is not None:
            s2 += str(c2.val)
            c2 = c2.next
        s3 = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        print(s3)
        h = ListNode(int(s3[0]))
        s3 = s3[1:]
        curr = h
        while s3 != '':
            curr.next = ListNode(int(s3[0]))
            s3 = s3[1:]
            curr = curr.next 
        return h
            
        