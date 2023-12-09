class Solution(object):
    def inorderTraversal(self, root):
        def dfs(root,result):
          if root != None:
            dfs(root.left,out)
            out.append(root.val)
            dfs(root.right,out)  
            
        out = []
        dfs(root,out)
        return out
        