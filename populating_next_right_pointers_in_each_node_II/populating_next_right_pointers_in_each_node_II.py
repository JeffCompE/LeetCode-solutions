"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def connect_nodes(node):
            l = node.left
            if not node.right:
                node = node.next
                while node and not node.left and not node.right:
                    node = node.next
                if not node:
                    return
                else:
                    r = node.left if node.left else node.right
            else:
                r = node.right

            while l and r:
                l.next = r

                l = l.right if l.right else l.left
                while r and not r.left and not r.right:
                    r = r.next
                if r:
                    r = r.left if r.left else r.right

        def dfs(node):
            if node.right:
                dfs(node.right)
            connect_nodes(node)
            if node.left:
                dfs(node.left)

        dfs(root)
        return root
