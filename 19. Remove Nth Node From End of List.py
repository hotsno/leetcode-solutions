# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if n == len(nodes):
            return nodes[1]
        index_to_change = len(nodes) - n - 1
        nodes[index_to_change].next = nodes[index_to_change].next.next
        return head
