# Blockchain

# A Blockchain(opens in a new tab) is a sequential chain of records, similar to a linked list. Each block contains
# some information and how it is connected related to the other blocks in the chain. Each block contains a
# cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a
# SHA-256(opens in a new tab) hash, the Greenwich Mean Time(opens in a new tab) when the block was created,
# and text strings as the data.
#
# Use your knowledge of linked lists and hashing to create a blockchain implementation.

import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        sha.update(self.timestamp.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.head = None

    def append(self, block):
        if self.head is None:
            self.head = block
            return
        curr = self.head
        while curr.next_block:
            curr = curr.next_block
        curr.next_block = block

    def print_chain(self):
        curr = self.head
        while curr:
            print(curr.data, end='')
            if curr.next_block:
                print(' -> ', end='')
            else:
                print()
            curr = curr.next_block

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
block1 = Block('5Feb 12:00', 123, '')
block2 = Block('5Feb 12:10', 456, block1.calc_hash())
blockchain = Blockchain()
blockchain.append(block1)
blockchain.append(block2)
blockchain.print_chain()

## Test Case 2
block1 = Block('5Feb 12:00', 123, '')
block2 = Block('5Feb 12:10', 456, block1.calc_hash())
block3 = Block('6Feb 10:10', 'abc', block2.calc_hash())
blockchain = Blockchain()
blockchain.append(block1)
blockchain.append(block2)
blockchain.append(block3)
blockchain.print_chain()

## Test Case 3
blockchain = Blockchain()
blockchain.print_chain()