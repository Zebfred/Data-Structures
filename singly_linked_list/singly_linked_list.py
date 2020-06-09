class Node:
    def __init__(self, value, next_node = None):
        self.value     = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # fill
    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # append
    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # pop (Always hated that method name, it doesn't describe what it's doing at all)
    # You can't remove this. You can't remove anything with the way they're doing this because you can't actually delete anything.
    # It's trying to get some value popped out, and when it does that after removing something it - for some reason - gets None when it should be getting some value.
    # So instead of using it like a regular list and getting some value from the end - because it's there - I can't.
    # It's just magically invisible.
    # Even though I tell it to go to the next.
    # But the current one is None, because it's deleted. You can't get the next one because the current one is lost.
    # But where is it? There's still a tail!
    # All of this is way too much abstraction, I can't just fucking look at it like a regular list and I can't just print out everything
    # Just use a list and accept the loss in efficiency, it's not worth the sacrifice in legibility.
    def remove_head(self):
        if not self.head:
            return None
        else:
            value     = self.head.get_value()
            self.head = self.head.get_next()

            return value

    # max
    def get_max(self):
        if not self.head and not self.tail:
            return None
        current = self.head
        maximum = current.value

        while current != None:
            if current.value > maximum:
                maximum = current.value
            current = current.get_next()
        return maximum

    # has
    def contains(self, value):
        current = self.head

        while current != None:
            if current.value == value:
                return True
            else:
                current = current.get_next()
        return False


# ll = LinkedList()
# ll.add_to_tail(3)
# ll.add_to_tail(5)
# ll.add_to_tail(9)
# ll.add_to_tail(11)
# print(ll.head.get_value())
# print(ll.remove_head())
# print(ll.head.get_value())
