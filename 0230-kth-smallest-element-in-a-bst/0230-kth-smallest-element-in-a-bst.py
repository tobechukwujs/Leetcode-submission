class Solution(object):
    def kthSmallest(self, root, k):
        result = []

        def traverse(node):
            if not node:
                return None
            
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return result[k-1]