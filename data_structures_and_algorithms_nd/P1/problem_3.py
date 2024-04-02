# Huffman Coding

import sys
from heapq import heapify, heappop, heappush


# Priority queue using a min heap
class PriorityQueue:
    def __init__(self):
        self.minheap = []

    def insert(self, item):
        heappush(self.minheap, item)

    def remove(self):
        return heappop(self.minheap)

    def is_empty(self):
        return len(self.minheap) == 0


# Huffman tree
class TreeNode:
    def __init__(self, freq, char=' '):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

    def is_leaf_node(self):
        return self.left_child is None and self.right_child is None

    def __lt__(self, other):
        return self.freq < other.freq or (self.freq == other.freq and self.char < other.char)

class HuffmanTree(object):
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

def collect_codes(root):
    codemap = {}
    def traverse(node, bits):
        if node.is_leaf_node():
            codemap[node.char] = bits
            return
        traverse(node.left_child, bits + '0')
        traverse(node.right_child, bits + '1')
    traverse(root, '')
    return codemap

def huffman_encoding(data):
    if data == '':
        return '', HuffmanTree()
    # store into dict with frequency
    freq = {}
    for ch in data:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # create nodes and store into priority queue
    pq = PriorityQueue()
    for ch, cnt in freq.items():
        node = TreeNode(cnt, ch)
        pq.insert(node)

    # construct huffman tree
    tree = HuffmanTree()
    while not pq.is_empty():
        node1 = pq.remove()
        if pq.is_empty():
            tree.set_root(node1)
            break
        node2 = pq.remove()

        combined_freq = node1.freq + node2.freq
        parent = TreeNode(combined_freq, node1.char + node2.char)
        parent.set_left_child(node1)
        parent.set_right_child(node2)
        pq.insert(parent)

    # traverse tree & store dict of character --> binary code
    codemap = collect_codes(tree.root)
    print(codemap)
    # for data, generate binary code
    encoded_data = ''
    for ch in data:
        encoded_data += codemap[ch]

    return encoded_data, tree


def huffman_decoding(data, tree):
    decoded_data = ''
    curr = tree.root
    for bit in data:
        if bit == '0':
            curr = curr.left_child
        else:
            curr = curr.right_child
        if curr.is_leaf_node():
            decoded_data += curr.char
            curr = tree.root
    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    ## Test Case 1
    b_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(b_great_sentence)))
    print("The content of the data is: {}\n".format(b_great_sentence))

    encoded_data, tree = huffman_encoding(b_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    ## Test Case 2
    b_great_sentence = "Where is Jynn? :("

    print("The size of the data is: {}\n".format(sys.getsizeof(b_great_sentence)))
    print("The content of the data is: {}\n".format(b_great_sentence))

    encoded_data, tree = huffman_encoding(b_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    ## Test Case 3
    b_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(b_great_sentence)))
    print("The content of the data is: {}\n".format(b_great_sentence))

    encoded_data, tree = huffman_encoding(b_great_sentence)

    #print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))