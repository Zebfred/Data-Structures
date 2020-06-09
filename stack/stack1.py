import sys
sys.path.append('../single_linkedlink')
from singly_linklist import LinkedList

class Stack:
    def __init__(self):
        self.size = 0


        self.sll = LinkedList()

    def push(self, value):
        if value != None:
            self.sll.add_to_tail(value)
            self.size += 1

    def pop(self):
        try:
            val = self.sll.tail.value
            self.sll.remove_from_tail()
            self.size -= 1
            return(val)
        except:
            print('There are no values')

    def len(self):
        return self.size
