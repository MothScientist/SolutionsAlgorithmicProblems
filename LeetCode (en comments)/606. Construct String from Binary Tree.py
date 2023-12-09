# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        res = str(root.val)

        left_tree = self.tree2str(root.left)
        right_tree = self.tree2str(root.right)

        if not left_tree and not right_tree:
            return res
        elif not left_tree:
            return res + "()" + "(" + right_tree + ")"
        elif not right_tree:
            return res + "(" + left_tree + ")"

        return res + "(" + left_tree + ")" + "(" + right_tree + ")"

# 2
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        res = str(root.val)

        if root.left or root.right:
            res += f"({self.tree2str(root.left)})"
        if root.right:
            res += f"({self.tree2str(root.right)})"
        return res