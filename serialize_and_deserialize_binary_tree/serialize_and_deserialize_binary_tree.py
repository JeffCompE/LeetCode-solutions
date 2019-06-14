from collections import deque
# use deque for constant time cost on append and pop operation (to be used as a stack)

# Definition for a binary tree node.
# class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes_to_visit = deque()
        nodes_to_visit.append(root)
        data = deque()
        # pre order traverse
        while len(nodes_to_visit):
            node = nodes_to_visit.pop()
            if node:
                data.append(f'{node.val},')
                nodes_to_visit.append(node.right)
                nodes_to_visit.append(node.left)
            else:
                data.append(',')
        return ''.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        if vals[0] == '':
            return None
        root = TreeNode(int(vals[0]))
        nodes_to_create = deque()
        nodes_to_create.append(root)
        empty_node = TreeNode(0)
        for val in vals[1:-1]:
            parent = nodes_to_create[-1]
            if val == '':
                if parent.left is None:
                    parent.left = empty_node
                elif parent.left is empty_node:
                    parent.left = None
                    nodes_to_create.pop()
                else:
                    nodes_to_create.pop()
                continue
            node = TreeNode(int(val))
            if parent.left is None:
                parent.left = node
                nodes_to_create.append(node)
            else:
                if parent.left is empty_node:
                    parent.left = None
                parent.right = node
                nodes_to_create.pop()
                nodes_to_create.append(node)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
