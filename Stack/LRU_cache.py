class LRUCache:
    class Node:
        def __init__(self,key,value ,prev=None,nxt=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.nxt = nxt
    def __init__(self, capacity: int):
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.tail.prev=self.head
        self.head.nxt= self.tail
        self.size = capacity
        self.m = {}
    def addNode(self,node):
        temp = self.head.nxt
        node.nxt = temp
        node.prev=self.head
        self.head.nxt = node
        temp.prev=node
        
    def delNode(self,node):
        prevv = node.prev
        nxtt = node.nxt
        prevv.nxt = nxtt
        nxtt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.m:
            res = self.m[key]
            del self.m[key]
            self.delNode(res)
            self.addNode(res)
            self.m[key] = self.head.nxt
            return res.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            cur = self.m[key]
            del self.m[key]
            self.delNode(cur)
        if len(self.m) == self.size :
            del self.m[self.tail.prev.key]
            self.delNode(self.tail.prev)
        self.addNode(self.Node(key,value))
        self.m[key]= self.head.nxt
