# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = dict()

        def inorder_traverse(node, x, y):
            if node.left:
                inorder_traverse(node.left, x-1, y-1)
            if x not in nodes:
                nodes[x] = dict()
            if y not in nodes[x]:
                nodes[x][y] = list()
            nodes[x][y].append(node.val)
            if node.right:
                inorder_traverse(node.right, x+1, y-1)

        inorder_traverse(root, 0, 0)
        ans = list()
        for x in sorted(nodes.keys()):
            line = nodes[x]
            line_res = list()
            for y in sorted(line.keys(), reverse=True):
                line_res.extend(sorted(line[y]))
            ans.append(line_res)

        return ans
