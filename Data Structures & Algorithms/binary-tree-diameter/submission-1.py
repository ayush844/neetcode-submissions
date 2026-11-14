# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = float('-inf')
        def getHeight(node):
            nonlocal maxDiameter
            if not node:
                return -1

            leftHt = getHeight(node.left)
            rightHt = getHeight(node.right)

            maxDiameter = max(leftHt + rightHt + 2, maxDiameter)

            return max(leftHt, rightHt) + 1

        getHeight(root)

        return maxDiameter