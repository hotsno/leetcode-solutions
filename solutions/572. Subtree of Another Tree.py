# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        return self.isSame(root, subRoot) or self.isSame(root.left, subRoot) or self.isSame(root.right, subRoot)

    def isSame(self, t1, t2):
        if not t1 or not t2:
            return t1 == t2
        return t1.val == t2.val and self.isSame(t1.right, t2.right) and self.isSame(t1.left, t2.left)
