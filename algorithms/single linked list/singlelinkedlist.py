class Node:
    def __init__(self, value):
        self.value = value      # data stored in node
        self.next = None        # pointer to next node


class SLinkedList:
    def __init__(self):
        self.head = None        # start of the list

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head  # point to current head
        self.head = new_node       # update head

    def add_to_back(self, value):
        if self.head is None:
            self.add_to_front(value)
            return

        mover = self.head
        new_node = Node(value)

        # traverse until last node
        while mover:
            if mover.next is None:
                mover.next = new_node
                break
            mover = mover.next

    def print_values(self):
        mover = self.head
        while mover:
            print(mover.value)
            mover = mover.next

    def remove_from_front(self):
        if self.head is None:
            return
        self.head = self.head.next  # move head forward

    def remove_from_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None  # only one node
            return

        mover = self.head

        # stop at second last node
        while mover.next.next:
            mover = mover.next
        mover.next = None

    def remove_val(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        mover = self.head

        # find node before target
        while mover.next:
            if mover.next.value == value:
                mover.next = mover.next.next  # skip node
                return
            mover = mover.next

    def insert_at(self, value, n):
        new_node = Node(value)

        if n == 0:
            self.add_to_front(value)
            return

        mover = self.head
        index = 0

        # move to (n-1) position
        while mover and index < n - 1:
            mover = mover.next
            index += 1

        if mover is None:
            return  # index out of range

        # insert node
        new_node.next = mover.next
        mover.next = new_node


# -------- Usage --------
myList = SLinkedList()
myList.add_to_front(4)
myList.add_to_front(3)
myList.add_to_front(1)

myList.remove_val(3)
myList.print_values()