"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
def __init__(self):
    self.size = 0
    # self.storage = ?
    self.storage = LinkedList()    

def __len__(self):
    pass
    count = 0
    head = self.storage.head
    tail = self.storage.tail
    done = False 
    while done is False:
        if count == 0 and head is None:
            done = True 
        elif count == 0 and head.get_next is None:
            count += 1
            done = True 
        elif head is not tail:
            head.get_next()
            count += 1
        elif:
            count += 1
            done = True
    return count                    



def push(self, value):
    pass
    self.storage.add_to_tail(value)

def pop(self):
    pass
    return self.storage.remove_tail()



