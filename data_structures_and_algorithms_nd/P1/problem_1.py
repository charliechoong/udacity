# Least Recently Used Cache

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current_capacity = 0
        # Doubly linked list to order in terms of recent access (ie. front means most recently access)
        self.dll = DoublyLinkedList()
        # Hashmap maps each key to list node
        self.hm = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hm:
            print(-1)
            return -1

        node = self.hm[key]
        # If not already first, remove from current position and add to front of DLL
        self.dll.remove(node)
        self.dll.append_front(key, node.data)
        print(node.data)
        return node.data

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # if capacity is set to 0, do nothing
        if self.capacity <= 0:
            return
        # If key is already present in cache, simply update the value of node in DLL
        if key in self.hm:
            self.hm[key].data = value
            return
        # if cache at max capacity, remove oldest node and update hashmap
        if self.current_capacity == self.capacity:
            del self.hm[self.dll.tail.key]
            self.dll.remove_back()
            self.current_capacity -= 1
        # Append new item to front and update hashmap
        self.dll.append_front(key, value)
        self.hm[key] = self.dll.head
        self.current_capacity += 1

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_front(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.head, self.tail = node, node
            return
        if self.head.key == key:
            return
        node.next = self.head
        self.head = node
        node.next.prev = self.head

    def remove(self, node):
        # if this is tail node, update tail to prev node.
        if node.key == self.tail.key:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next

    def remove_back(self):
        curr = self.head
        # if 0 or 1 nodes currently, result after removing is empty list.
        if not curr or not curr.next:
            self.head, self.tail = None, None
            return
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            if curr.next:
                print(' -> ', end=' ')
            curr = curr.next
        print()


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
# our_cache.dll.print()
# print(our_cache.hm)

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
# our_cache.dll.print()
# print(our_cache.hm)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
our_cache = LRU_Cache(1)
our_cache.set(1, "a")
our_cache.get(1)    # returns 'a'

## Test Case 2
our_cache = LRU_Cache(0)
our_cache.get(1)    # returns -1
our_cache.set(1, 1)
our_cache.get(1)    # returns -1

## Test Case 3
our_cache = LRU_Cache(4)
our_cache.set(1, None)
our_cache.get(1)    # returns None