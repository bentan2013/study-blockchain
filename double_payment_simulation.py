#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import random
import matplotlib.pyplot as plt


class Node:
    def __init__(self, name, latest_block, is_good=True):
        self.name = name
        self.latest_block = latest_block
        self.is_good = is_good

    def create_block(self, wait_time=False):
        new_block = None
        if wait_time is True :
            new_block = Block(uuid.uuid1(), self.latest_block, True)
        elif self.is_good is not True or self.latest_block.in_good_chain is not True:
            new_block = Block(uuid.uuid1(), self.latest_block, False)
        else:
            new_block = Block(uuid.uuid1(), self.latest_block, True)
        return new_block

    def update_latest_block(self, block):
        self.latest_block = block


class Block:
    def __init__(self, id, pre_block, in_good_chain=True):
        self.id = id
        self.pre_block = pre_block
        self.in_good_chain = in_good_chain


class System:
    def __init__(self):
        self.genesis_block = System.create_genesis_block()
        self.latest_node = self.genesis_block

    @staticmethod
    def create_genesis_block():
        genesis_block = Block('0', None)
        return genesis_block

    @staticmethod
    def boardcast_latest_block(latest_blocks, nodes):
        max_length = 0
        max_length_block = None

        for b in latest_blocks:
            l = System.length_of_chain(b)
            if l > max_length:
                max_length_block = b
                max_length = l

        for n in nodes:
            n.update_latest_block(max_length_block)

    def latest_node(self):
        return self.latest_node

    @staticmethod
    def length_of_chain(block):
        length = 1
        while block.pre_block is not None:
            length += 1
            block = block.pre_block
        return length

    # infact, each trans will be boardcast, and nodes will create blocks,
    # then a random node will success create a block than others
    def select_node(self, nodes):
        import time
        # time.sleep(0.5)
        index =  random.randrange(0, len(nodes)-1)
        return nodes[index]


if __name__ == '__main__':
    bitcoin = System()

    # init good nodes and evil nodes
    total_node_num = 100
    good_node_num = 55
    evil_node_num = total_node_num - good_node_num

    name_index = 1
    good_nodes = []
    evil_nodes = []
    total_nodes = []
    for i in range(good_node_num):
        g = Node(str(name_index), bitcoin.latest_node)
        name_index += 1
        good_nodes.append(g)
        total_nodes.append(g)

    for j in range(evil_node_num):
        e = Node(str(name_index), bitcoin.latest_node, False)
        name_index += 1
        evil_nodes.append(e)
        total_nodes.append(e)

    random.shuffle(total_nodes)

    # the evil node will backup a node for fork-attacking
    fork_block = bitcoin.latest_node
    good_latest_block = bitcoin.latest_node
    evil_latest_block = bitcoin.latest_node

    attack_delay_block_num = 6

    # before attack the good nodes and evil nodes will work for the right things
    for i in range(attack_delay_block_num):
        the_node = bitcoin.select_node(total_nodes)
        latest_block = the_node.create_block(wait_time=True)
        latest_blocks = [latest_block, ]
        System.boardcast_latest_block(latest_blocks, nodes=total_nodes)
        good_latest_block = latest_block

    # now, the evil nodes start to attack
    evil_latest_blocks = [fork_block]
    System.boardcast_latest_block(evil_latest_blocks, evil_nodes)

    choose_good_node_times = 0
    choose_evil_node_times = 0

    good_chain_length_records = []
    evil_chain_length_records = []
    index_records = []
    max_times = 500
    b_first_show = True
    plt.figure()
    plt.xlim(0, max_times)
    plt.ylim(0, max_times / 2)

    for i in range(max_times):
        the_node = bitcoin.select_node(total_nodes)
        if the_node.is_good is False:
            choose_evil_node_times += 1
            print("Choose a evil node. good/evil ratio is {}".format(choose_good_node_times / choose_evil_node_times))
        else:
            choose_good_node_times += 1
        latest_block = the_node.create_block()
        if latest_block.in_good_chain is False:
            evil_latest_block = latest_block
            # evil nodes only admit the chain contains evil block
            System.boardcast_latest_block([evil_latest_block, ], evil_nodes)
        else:
            good_latest_block = latest_block

        System.boardcast_latest_block([good_latest_block, evil_latest_block], good_nodes)

        good_chain_length = System.length_of_chain(good_latest_block)
        evil_chain_length = System.length_of_chain(evil_latest_block)
        good_chain_length_records.append(good_chain_length)
        evil_chain_length_records.append(evil_chain_length)
        index_records.append(i)
        print("Iteration number:\t{}".format(i))
        print("good chain length is {}".format(good_chain_length))
        print("evil chain length is {}".format(evil_chain_length))
        if good_chain_length > evil_chain_length:
            print("Evil can never prevail over good")
        else:
            print("While the priest climbs a foot, the devil climbs ten")

        if i % 10 == 0:
            plt.plot(index_records, good_chain_length_records, "b", label="length of good chain")
            plt.plot(index_records, evil_chain_length_records, "r", label="length of evil chain")

            if b_first_show is True:
                b_first_show = False
                plt.legend()

            plt.pause(1)











