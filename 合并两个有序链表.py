# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        nodelist = []
        while l1:
            nodelist.append(l1.val)
            l1 = l1.next
        while l2:
            nodelist.append(l2.val)
            l2 = l2.next
        nodelist = sorted(nodelist)

        head = ListNode(0)
        p = head
        for index in range(len(nodelist)):
            head.next = ListNode(nodelist[index])
            head = head.next
        return p.next



ListNode1 = ListNode(5)

ListNode2 = ListNode(1,ListNode(2,ListNode(4)))

result = Solution().mergeTwoLists(ListNode1,ListNode2)
while result:
    print(result.val)
    result = result.next