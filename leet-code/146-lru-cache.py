'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

'''
APPROACH : doubly linked list + Map/dictionay
'''

class LRUCache:
    # class to store the key value pair 
    # we use doubly linked list 
    class Node :
        def __init__ (self,key,value) :
            self.key = key
            self.value = value
            self.prev = None 
            self.next = None 

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {} # empty dictionary to map the key : value(pointer to node)
        
    # add at the starting (left)
    def addNode(self,newNode) :
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
    
    # delete at the end (right)
    def delNode(self,delNode) :
        prev = delNode.prev
        next = delNode.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.m :
            resNode = self.m[key] # get the result node
            ans = resNode.value
            del self.m[key]
            self.delNode(resNode) # delete from right
            self.addNode(resNode) # insert at left 
            self.m[key] = self.head.next # reset the key value pair in map
            return ans
        return -1 # if not found

    def put(self, key: int, value: int) -> None:
        if key in self.m :
            curr = self.m[key] # grab the key value pair
            del self.m[key]
            self.delNode(curr)
        
        if len(self.m) == self.cap :
            del self.m[self.tail.prev.key] # delete the most past used key
            self.delNode(self.tail.prev) # delete that node in dll
        # add the new node
        self.addNode(self.Node(key,value))
        self.m[key] = self.head.next # update the node pointer to head 
             


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)