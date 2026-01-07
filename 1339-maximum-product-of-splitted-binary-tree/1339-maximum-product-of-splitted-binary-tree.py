# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def tree_sum(node):
            if not node:
                return 0
            return node.val + tree_sum(node.left) + tree_sum(node.right)

        total = tree_sum(root) 
        best = 0

        def subtree_sum(node):
            nonlocal best
            if not node:
                return 0
            # postorder traversal
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            sub = node.val + left_sum + right_sum
            
            # cut the edge above this subtree
            best = max(best, sub*(total - sub)) 
            
            return sub

        subtree_sum(root)
        return best % MOD
            
            