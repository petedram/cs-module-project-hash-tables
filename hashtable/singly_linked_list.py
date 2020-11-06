class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value) #create new node
        if self.head is None:
            #update head and tail attributes
            self.head = new_node
            self.tail = new_node #when only one node, it is both head and tail
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        # create new node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            #update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
        #2. LL is not empty
            #update next_node of our tail
            self.tail.set_next_node(new_node)
            #update self.tail
            self.tail = new_node

    def remove_head(self):
        # check if head
        if self.head is None:
            return None
        # non-empty list, return the value of the old head.
        else:
            ret_value = self.head.get_value()
            #list of one thing
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # if empty list return none
        if self.tail is None:
            return None
        else:
        #list with one element
            ret_value = self.tail.get_value()
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                cur_node = self.head
                #list with 2 elements
                if cur_node.get_next_node() is self.tail:
                    self.tail = cur_node
                    self.tail.set_next_node(None) #point to None
                else:
                #list with 2+ elements
                #create function to store previous node - get_prev_node?
                #create while loop to cycle through storing the value until reaching tail then -1?
                    while cur_node.get_next_node() is not self.tail:
                        cur_node = cur_node.get_next_node()
                        self.tail = cur_node
                        self.tail.set_next_node(None) #point to None
            return ret_value

    def contains(self, value):
        # loop LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            #if we find value, then return true
            if cur_node.get_value() == value:
                return True
        # if get to end and not found, return False
        return False

    def get_max(self):
        # TODO time permitting    
        pass


        #middle - search contains and insertion