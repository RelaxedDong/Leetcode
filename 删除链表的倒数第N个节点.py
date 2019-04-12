# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        mynode = ListNode(0)
        p = head
        mynode.next = p
        length = 0
        while head:
            length+=1
            head = head.next

        if n == length:
            return p.next

        for x in range(1,length-n+1):
            if x == length-n:
                p.next = p.next.next
            p = p.next
        return mynode.next


head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
a = Solution().removeNthFromEnd(head,7)

while a:
    print(a.val)
    a = a.next

