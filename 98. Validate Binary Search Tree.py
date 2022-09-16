# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]

    def helper(self, node):
        lvalid, rvalid = True, True
        lmin, rmin, lmax, rmax = float("inf"), float("inf"), float("-inf"), float("-inf")
        if node.left:
            lvalid, lmin, lmax = self.helper(node.left)
        if node.right:
            rvalid, rmin, rmax = self.helper(node.right)
        if not (lvalid and rvalid):
            return (False, 0, 0)
        if lmax >= node.val or rmin <= node.val:
            return (False, 0, 0)
        return (True, min(node.val, lmin, rmin), max(node.val, lmax, rmax))

    def isValidBST_v2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper2(root, float("-inf"), float("inf"))

    def helper_v2(self, root, small, big):
        if not root:
            return True
        if root.val <= small or root.val >= big:
            return False
        return self.helper2(root.left, small, root.val) and self.helper2(root.right, root.val, big)

