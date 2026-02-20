class Solution(object):
    def pathSum(self, root, targetSum):
        allPaths = []  
        
        def dfs(node, current_target, current_path):
            if not node:
                return 
            current_path.append(node.val)
            if not node.left and not node.right and current_target == node.val:
                allPaths.append(current_path[:])    
            
            dfs(node.left, current_target - node.val, current_path)
            dfs(node.right, current_target - node.val, current_path)
            current_path.pop(-1) 
            
        dfs(root, targetSum, [])
        return allPaths