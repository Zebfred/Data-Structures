import sys
sys.path.append('../singly_linklist')
from singly_linklist import LinkedList


class Queue:
    def __init__(self):
        self.size = 0


        self.sll = LinkedList()

    def enqueue(self, value):
        if value != None:
            self.sll.add_to_tail(value)
            self.size += 1

    def dequeue(self):
        try:
            val = self.sll.head.value
            self.sll.remove_from_head()
            self.size -= 1
            return(val)
        except:
            print('There are no values')

    def len(self):
        return self.size
