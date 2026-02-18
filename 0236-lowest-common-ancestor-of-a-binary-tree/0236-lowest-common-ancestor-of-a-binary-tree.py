class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root, p, q)
        right = self.lowestCommonAncestor(root, p, q) 

        if left and right:
            return root   
        return left if left else right    