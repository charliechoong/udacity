To achieve O(1) get and set operations, we can make use of 2 data structures: a doubly linked list and a hashmap.
- Double linked list: helps to keep track of the order of recent usage. Allows for efficient removing of nodes in middle
  of list.
- Hash map (dictionary in Python): allows efficient access of value given the key.

When an existing key/value is recently used, we need to remove it from its current position and append it to the front 
of DLL.
When a new key/value is newly set, we simply append it to front of DLL.