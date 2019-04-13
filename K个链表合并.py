# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def mergeTwoLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nodelist = []
        for head in lists:
            while head:
                nodelist.append(head.val)
                head = head.next
        print(nodelist)
        nodelist = sorted(nodelist)

        head = ListNode(0)
        p = head
        for index in range(len(nodelist)):
            head.next = ListNode(nodelist[index])
            head = head.next
        return p.next


ListNode1 = ListNode(5)

ListNode2 = ListNode(1,ListNode(2,ListNode(4)))

ListNode3 = ListNode(3,ListNode(8,ListNode(9)))

result = Solution().mergeTwoLists([ListNode1,ListNode2,ListNode3])
while result:
    print(result.val)
    result = result.next