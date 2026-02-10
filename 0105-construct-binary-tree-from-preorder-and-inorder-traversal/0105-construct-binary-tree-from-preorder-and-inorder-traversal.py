
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None

        root_val = preorder[0]   
        root = TreeNode(preorder[0])

        mid = inorder.index(root_val) 

        root.left = self.buildTree(preorder[1 : mid+1] + inorder[:mid])
        root.right = self.buildTree(preorder[mid+1 :] + inorder[mid+1 :])

        return root


