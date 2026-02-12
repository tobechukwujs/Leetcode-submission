class Solution(object):
    def getHeight(self, node):
        if not node: return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def isBalanced(self, root):
        if not root:
            return True

        left_h = self.getHeight(root.left)
        right_h = self.getHeight(root.right)

        return abs(left_h - right_h) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)