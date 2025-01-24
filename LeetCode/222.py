class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        n = [0]
        def count(node):
            if node is None:
                return
            if node.left:
                n[0] +=1
                count(node.left)
            if node.right:
                n[0] += 1
                count(node.right)
        count(root)
        return n[0] if root is None else n[0]+1
