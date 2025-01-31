# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(root, node, depth=1):
            if root is None:
                return -1
            if node == root:
                return depth

            left = get_depth(root.left, node, depth + 1)
            if left != -1:
                return left

            return get_depth(root.right, node, depth + 1)

        if not root:
            return 0
        stack = []
        stack.append(root)
        max_depth = 1
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.right and not node.left:
                depth = get_depth(root, node)
                # print(node.val, depth)
                max_depth = max(max_depth, depth)
        return max_depth
