class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
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
        if not index:
            index = self.length - 1

        if index >= self.length:
            return None, None
        
        current = self.head
        
        for _ in range(index):
            pre = current
            current = current.next

        return pre, current

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return False
        
        pre, current = self.__get_node()
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return current.value
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop_first(self):
        if self.length == 0:
            return False

        current = self.head
        self.head = current.next

        if not current.next:
            self.tail = None

        self.length -= 1
        return current.value

    def get_value (self, index):
        _, current = self.__get_node(index)

        if current:
            return current.value
        
        return current
    
    def set_value (self, index, value):
        _, current = self.__get_node(index)

        if current:
            current.value = value

    def insert_node(self, index, value):
        if index == 0:
            return self.prepend()

        if index == self.length - 1:
            return self.append()
        
        new_node = Node(value)
        pre, current = self.__get_node(index)

        if current:
            pre.next = new_node
            new_node.next = current

    def remove_node(self, index):
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre, current = self.__get_node(index)

        if current:
            pre.next = None
            self.tail = pre
            self.length -= 1
            return current.value
        
        return None
    
    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current

        pre = None
        next = current.next

        for _ in range(self.length):
            next = current.next
            current.next = pre
            pre = current
            current = next


