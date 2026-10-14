# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode()
        cur=dummyNode
        carry=0
        while (l1  or l2 ) or carry:
            tot=0
            if l1:
                tot+=l1.val
                l1=l1.next
            if l2:
                tot+=l2.val
                l2=l2.next
            tot+=carry
            carry=tot//10
            node=ListNode(tot%10)
            cur.next=node
            cur=cur.next
        return dummyNode.next

        