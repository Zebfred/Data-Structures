class Node:
    def __init__(me, value=None, next_node=None):
        # value at this linked list node
        me.value = value 
        #reference to the next node in the list
        me.next_node = next_node 

    def get_value(me):
        return me.value

    def get_next(me):
        return me.next_node

    def set_next(me, new_next):
        #set this node's next_node reference to the passed in node 
        me.next_node = new_next

class LinkedList:
    def __init__(me): 
        #reference to the head of the list
        me.head = None 
        #reference to the tail of the list 
        me.tail = None 

    def add_to_tail(me, value):
        #wrap the input value in a node
        new_node = Node(value, None)
        #check if there is no head (i.e., the list is empty?)               
        if not me.head:
            #if the list is initially empty, set both head and tail to the new node
            me.head = new_node
            me.tail = new_node
        #we have a non-empty list, add the new node to the tail
        else:
            #set the current tail's next reference to our new node 
            me.tail.set_next      
            #set the list's tail reference to the new node
            me.tail = new_node

    def remove_head(me):
        #return None if there is no head (i.e. the list is empty)
        if not me.head()
            return None
        #if head has no next, then we have a single element in our list
        if not me.head.get_next():
            #get a reference to the head
            head = me.head
            #delete the list's head reference
            me.head = None
            #also make sure the tail reference doesn't refer to anything 
            me.tail = None
            #return value
            head.get_value()
        #otherwise we have more than one element in our list
        value = me.head.get_value()
        #set the head reference to the current head's next node in the list
        me.head = me.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head 

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current 
        return value

    def contains(self, value):
        if not self.head:
            return False

            # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)

        #get a reference to the node we're currently at; update this as we traverse the list 
        current = self.head 
        #check to see if we're at a valide node
        while current:
            #return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        #if we've gotten here, then the target node isn't in our list 
        return False

    def get_max(self):
        if not self.head:
            return None

     #reference to the largest value we've seen so far
        max_value = self.head.get_value()
        #reference to our current node as we traverse the list
        current = self.head.get_next()
        #check to see if we're still as a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                #if so, update our max_calue cariable
                max_value = current.get_value()
               #update the current node to the next node in the list
               current = current.get_next() 
        return max_value        
                



