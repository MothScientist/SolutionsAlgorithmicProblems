"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        def rec(root):
            if root:
                out.append(root.val)
                for i in root.children:
                    rec(i)
        out = []
        rec(root)
        return out