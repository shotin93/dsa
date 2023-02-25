class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        current = self.head
        while (current):
            print(current.value)
            current = current.next

    def __get_node(self, index=None):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            current = self.head
            for _ in range(index):
                current = current.next

        else:
            current = self.tail
            index = self.length - 1 - index
            for _ in range(index):
                current = current.previous

        return current

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            current_tail = self.tail
            current_tail.next = new_node
            new_node.previous = current_tail
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        current_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.previous
            self.tail.next = None
            current_tail.previous = None

        self.length -= 1
        return current_tail.value
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            current_head = self.head
            current_head.previous = new_node
            new_node.next = current_head
            self.head = new_node
        
        self.length += 1

    def pop_first(self):
        current_head = self.head

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = current_head.next
            current_head.next = None
            self.head.previous = None

        self.length -= 1
        return current_head.value
    
    def get_value(self, index):
        current = self.__get_node(index)

        if current:
            return current.value
        
        return current

    def set_value(self, index, value):
        new_node = Node(value)
        current = self.__get_node(index)

        if current:
            current.value = value
            return current.value
        
        return current

    def insert_node(self, index, value):
        if index == 0:
            return self.prepend()

        if index == self.length - 1:
            return self.append()
        
        new_node = Node(value)
        current = self.__get_node(index)

        if current:
            new_node.previous = current.previous
            current.previous.next = new_node
            new_node.next = current
            current.previous = new_node
            self.length += 1
            return current.value
        
        return current

    def remove_node(self, index):
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        current = self.__get_node(index)

        if current:
            current.previous.next = current.next
            current.next.previous = current.previous
            current.next = None
            current.previous = None
            self.length -= 1

            return current.value
        
        return None