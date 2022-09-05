# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    # DFS with recursion
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # DFS with iteration
    def maxDepthV2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

    # BFS with iteration
    def maxDepthV3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            for i in range(len(q)):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            res += 1
        return res
