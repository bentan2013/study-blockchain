#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_block, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_block = previous_block
        self.previous_hash = previous_hash

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode())
        return sha.hexdigest()


import datetime as date


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", None, "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey ! I am block" + str(this_index)
    this_hash = last_block.hash_block()
    return Block(this_index, this_timestamp, this_data, last_block, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_block_to_add = 10

for i in range(0, num_of_block_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash:\t{}\n".format(block_to_add.hash_block()))


from hashlib import sha256 as sha


def chunks(l, n):
    for i in range(0, len(l), n):
        yield(l[i:i + n])


def m_tree(transactions):
    sub_t = []
    for i in chunks(transactions, 2):
        if len(i) == 2:
            hash = sha(str(i[0] + i[1]).encode()).hexdigest()
        else:
            hash = sha(str(i[0] + i[0]).encode()).hexdigest()
        sub_t.append(hash)
    print(sub_t)

    if (len(sub_t)) == 1:
        return sub_t[0]
    else:
        return m_tree(sub_t)

m_tree(['a', 'b', 'c', 'd', 'e'])




