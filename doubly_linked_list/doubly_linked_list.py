"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    """Wrap the given value in a ListNode 
    and insert it after this node. This node already 
    points to the next node"""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode 
    and insert it before this node.This node could 
    already have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Reannages this ListNode's previous and next pointers 
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next:
            self.next.prev = self.prev



            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        self.length += 1
        if not self.head and not self.tail:
            #empthy list
            self.head = self.tail = ListNode(value)
        else:
            #the list is populated
            self.head.insert_before(value)
            self.head = self.head.prev    
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        value = self.head.value
        self.delete(self.head)
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
        self.length += 1 
        if not self.head and not self.tail:
            #empty list
            self.head = self.tail = ListNode(value)
        else:
            #list is populated 
            self.tail.insert_after(value)
            self.tail = self.tail.next

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #if LL is empty
        if not self.head and not self.tail:
            print("Error: Attemted to delete node not in list")
            return
        #if node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        #if node is head    
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        #if node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()

        #if node is in middle 
        else:
             node.delete()
        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #loop through nodes via node.next
        #if node.value is higher, update max
        #return max
        maxx = self.head
        curs = self.head
        for i in range(self.length):
            if curs.value > maxx.value:
                maxx = curs
            curs = curs.next
        return maxx.value
