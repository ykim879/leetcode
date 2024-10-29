class Node:
    def __init__(self, key = 0, value = 0, nxt = None, prev = None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {} # keep track of where the node is
        self.head = Node() # dummpy in front
        self.tail = Node() # dummpy in tail
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    def __remove_node(self, node):
        prev = node.prev
        node.prev.nxt = node.nxt
        node.nxt.prev = prev
    def __append_head(self, node):
        # append node to the head
        node.nxt = self.head.nxt
        self.head.nxt.prev = node
        node.prev = self.head
        self.head.nxt = node
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        # search dictionary: Node: previous and next value
        node = self.dict[key]
        # we are going to pop this Node and 
        self.__remove_node(node)
        self.__append_head(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.__remove_node(self.dict[key])
        node = Node(key, value, self.head.nxt, self.head)
        self.head.nxt.prev = node
        self.head.nxt = node
        self.dict[key] = node
        # eviction (when capacity exceeds)
        if len(self.dict) > self.capacity:
            ## pop this tail and remove from dictionary
            prev = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.nxt = self.tail
            self.dict.pop(prev.key)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
