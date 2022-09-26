class Node:
    """
    An object for storing a single node of a linked-list

    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"

class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
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
        Adds a new node containing data at the head of the node
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def insert(self, data, index):
        """
        Insert a new node containing data at the given position

        Takes O(1) time but finding insertion point takes O(n) time

        Overall takes O(n) time
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1

            prev = current
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes node containing key as the data value
        Returns the node or None if key doesn't exist

        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


    def search(self, key):
        """
        Returns first node containing data that matches the key
        Returns the node or 'None' if key is not found
        
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

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
        Returns the string representation of the linked list
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
        
        return '-> '.join(nodes)
