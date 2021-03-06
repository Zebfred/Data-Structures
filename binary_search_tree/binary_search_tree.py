#import sys
#sys.path.append('../queue')
#sys.path.append('../stack')
#from queue import Queue
#from stack import Stack
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
import sys
sys.path.append('../stack')

from stack import Stack


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
                 self.right = BSTNode(value)
                 return
             else:
                 self = self.right
                 return self.insert(value)
         else:
             value < self.value
             if self.left is None:
                 self.left = BSTNode(value)
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
        fn(self.value)
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
        if node:
            if node.left:
                node.in_order_print(node.left)


            print(node.value)

            if node.right:
                node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        stack = [node]

        while stack != []:
            look = stack[0]

            if look.right:
                stack.append(look.right)
            if look.left:
                stack.append(look.left)

            print(look.value)
            stack = stack[1:]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]

        while stack != []:

            look = stack[-1]
            print(look.value)
            stack = stack[0:-1]
            if look.left is not None:
                stack.append(look.left)
                print()

            if look.right is not None:
                stack.append(look.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(1) 
bst.insert(8) 
bst.insert(5)
bst.insert(7) 
bst.insert(6) 
bst.insert(3) 
bst.insert(4) 
bst.insert(2)
bst.bft_print(bst) 
print("_______") 
bst.dft_print(bst) 
print("elegant methods") 
print("pre order") 
bst.pre_order_dft() 
print("in order")
bst.in_order_print() 
print("post order") 
bst.post_order_dft() 
print()