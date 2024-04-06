# Request Routing in a Web Server with a Trie
import collections

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, not_found_handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root_handler = RouteTrieNode(handler)
        self.not_found_handler = not_found_handler

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        def _insert_path(node, path_parts, handler, i):
            current_part = path_parts[i]
            if i == len(path_parts)-1:
                node.insert(current_part, handler, True)
                return
            node.insert(current_part, self.not_found_handler, False)
            return _insert_path(node.children[current_part], path_parts, handler, i+1)

        return _insert_path(self.root_handler, path_parts, handler, 0)

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root_handler
        for part in path_parts:
            if part not in curr.children:
                return self.not_found_handler
            curr = curr.children[part]
        return curr.handler


## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None, is_leaf=False):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict()
        self.handler = handler
        self.is_leaf = is_leaf

    def insert(self, path_part, handler, is_leaf):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode(handler, is_leaf)


## The Router class will wrap the Trie and handler
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.routes.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path[0] != '/':
            return
        path_parts = self.split_path(path)
        return self.routes.find(path_parts)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if path.strip() == '/':
            return []
        if path[-1] == '/':
            path = path[:-1]
        parts = path[1:].split('/')
        return parts


## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one