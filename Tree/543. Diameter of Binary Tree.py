# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def get_depth(root):
            if not root:
                return 0

            left = get_depth(root.left)
            right = get_depth(root.right)

            max_diameter[0] = max(max_diameter[0], left + right)

            return 1 + max(left, right)

        get_depth(root)
        return max_diameter[0]
