class Node:
    """
    An object for storing a single Node in a 
    doubly-linked-list

    Models three attributes: The data of the node and the link 
    to the previous and next node in the list
    """
    data = None
    prev_node = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"

class DoublyLinkedList:
    """
    Doubly-Linked-List
    """

    def __init__(self) -> None:
       self.head = None


    def is_empty(self) -> bool:
        return self.head == None

    def size(self) -> int:
        """
        Returns the number of nodes in the linked list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node containing data to the head of the list

        Takes O(1) time
        """ 
        new_node = Node(data)
        new_node.next_node = self.head
        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at the given index

        Takes O(1) time but finding insertion point takes O(n) time

        Overall takes O(n) time
        """
        
        if index == 0:
            self.add(data)
        
        if index > 0:
            new_node = Node(data)
            
            position = index
            current = self.head

            while position > 1:
                current = new_node.next_node
                position -= 1
            
            prev = current
            next_node = current.next_node

            prev.next_node = new_node
            new_node.prev_node = prev
            new_node.next_node = next_node

    
    def remove(self, key):
        """
        Removes node containing key as the data value
        Returns the node or None if key doesn't exist

        Takes O(n) time
        """
        current = self.head
        previous = None
        next_node = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                self.head.prev_node = None
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                next_node.prev_node = previous
            else:
                previous = current
                current = current.next_node
                next_node = current.next_node
                
        return current
    
    def get_node(self, index):
        """
        Returns the node at the given index
        """
        
        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position +=1

        return current

    def __repr__(self) -> str:
        """
        Returns the string representation of the 
        Doubly-Linked-List

        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '<->'.join(nodes)

    