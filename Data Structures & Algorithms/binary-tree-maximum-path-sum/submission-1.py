# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = float('-inf')
        
        def maxPath(node):
            nonlocal maxSum
            if not node:
                return 0

            leftGain = max(maxPath(node.left), 0)
            rightGain = max(maxPath(node.right), 0)

            pathSum = leftGain + rightGain + node.val

            maxSum = max(maxSum, pathSum)

            return max(leftGain, rightGain) + node.val

        maxPath(root)

        return maxSum