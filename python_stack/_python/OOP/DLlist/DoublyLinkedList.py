class Node:
    # Each node holds a value and pointers to next and previous nodes
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        # Head points to the first node in the list
        self.head = None

    # -------------------- ADD AT BEGINNING --------------------
    def add_begin(self, data):
        new_node = Node(data)

        # If list is not empty, link current head to new node
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        # Move head to new node
        self.head = new_node

    # -------------------- ADD AT END --------------------
    def add_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        current = self.head
        while current.next:
            current = current.next

        # Link last node with new node
        current.next = new_node
        new_node.prev = current

    # -------------------- REMOVE NODE --------------------
    def remove(self, value):
        if self.head is None:
            return

        current = self.head

        while current:
            if current.value == value:

                # Case 1: removing head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    # Case 2: middle or last node
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev

                return

            current = current.next

    # -------------------- ADD AT POSITION --------------------
    def add_between(self, value, position):
        # Insert at beginning
        if position == 0:
            self.add_begin(value)
            return

        current = self.head
        index = 0

        # Move to position - 1
        while current and index < position - 1:
            current = current.next
            index += 1

        # If position is invalid
        if current is None:
            print("Position out of range")
            return

        new_node = Node(value)

        # Connect new node
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    # -------------------- PRINT LIST FORWARD --------------------
    def print_forward(self):
        current = self.head

        while current:
            print(current.value, end=" ⇄ ")
            current = current.next

        print("None")

dll = DoublyLinkedList()

dll.add_begin(10)
dll.add_end(20)
dll.add_between(15, 1)

dll.print_forward()

dll.remove(15)
dll.print_forward()