# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        self.preorder_index = 0
        self.inorder_map = {}
        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i
        return self.helper(0, len(preorder) - 1)

    def helper(self, start, end):
        if start > end:
            return None
        root = TreeNode(self.preorder[self.preorder_index])
        inorder_index = self.inorder_map[self.preorder[self.preorder_index]]
        self.preorder_index += 1
        root.left = self.helper(start, inorder_index - 1)
        root.right = self.helper(inorder_index + 1, end)
        return root

