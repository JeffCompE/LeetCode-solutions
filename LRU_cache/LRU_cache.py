class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = dict()
        self.capacity = capacity
        self.size = 0
        self.head = Node()  # head sentinel node
        self.tail = Node()  # tail sentinel node
        self.connect(self.head, self.tail)

    @staticmethod
    def connect(node_1, node_2):
        node_1.next = node_2
        node_2.prev = node_1

    def get(self, key: int) -> int:
        node = self.hashmap.get(key, None)
        if not node:
            return -1
        self.connect(node.prev, node.next)
        self.connect(node, self.head.next)
        self.connect(self.head, node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hashmap.get(key, None)
        if node:
            node.val = value
            self.connect(node.prev, node.next)
            self.connect(node, self.head.next)
            self.connect(self.head, node)
        else:
            # if key does not exist
            # pop the least recent used if the capacity is fulled
            if self.size == self.capacity:
                del_node = self.tail.prev
                self.connect(del_node.prev, self.tail)
                self.hashmap.pop(del_node.key)
                self.size -= 1

            new_node = Node(key, value)
            self.hashmap[key] = new_node
            self.connect(new_node, self.head.next)
            self.connect(self.head, new_node)
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
