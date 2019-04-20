# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x ,next=None):
        self.val = x
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        for index in range(len(node_list)):
            print()
Solution().swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
