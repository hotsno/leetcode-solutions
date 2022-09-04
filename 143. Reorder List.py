# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node_arr = []
        cur = head
        while cur:
            node_arr.append(cur)
            cur = cur.next
        l, r = 0, len(node_arr) - 1
        cur = ListNode()
        while l < r:
            cur.next = node_arr[l]
            cur = cur.next
            cur.next = node_arr[r]
            cur = cur.next
            l += 1
            r -= 1
        if l == r:
            cur.next = node_arr[l]
            cur = cur.next
        cur.next = None

