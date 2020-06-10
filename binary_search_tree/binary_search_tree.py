import sys
sys.path.append('../queue_and_stack')
from queue import Queue
from stack import Stack
#using those modules


"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print(self.value)
         if value >= self.value:
             if self.right is None:
                 self.right = BinarySearchTree(value)
                 return
             else:
                 self = self.right
                 return self.insert(value)
         else:
             value < self.value
             if self.left is None:
                 self.left = BinarySearchTree(value)
                 return
             else:
                 self = self.left
                 return self.insert(value)
        #pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return(True)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                self = self.right
                return self.contains(target)
        else:
            if self.left is None:
                return False
            else:
                self = self.left
                return self.contains(target)
    #    pass

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            self = self.right
            return self.get_max()
        #pass


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        cb(self.value)
        # if self.right and self.left:
        #     self.left.for_each(cb)
        #     self.right.for_each(cb)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
