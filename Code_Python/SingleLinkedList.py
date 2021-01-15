"""
Single-Linked List and Single-Linked Node Data Structures

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Single-linked list class implementation using a single-list node class.
- The search method returns always only the first occurrence (from the
  list head) of any duplicate data.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by
  Miller and Ranum.
- get_node_list() is an helper function that returns a list with the content
  of all connected nodes starting from a given node.


SLnode Class
------------
data            Content of the node.
next_node       Linked next node.
__init__()      Initializes the node.
__repr__()      Returns the string representation of the node.
set_data()      Set/replaces the content of the node.
get_data()      Returns the content of the node.
set_next()      Sets/replaces the linked next node.
get_next()      Returns the linked next node.


SLL Class
---------
head            Node at the front of the SLL.
size            Length of the SLL.
__init__()      Initializes the SLL.
__repr__()      Returns the string representation of the SLL.
is_empty()      Checks if the SLL is empty or not.
nodes()         Returns a list with all items contained in the SLL.
add_front()     Adds a new item to the front of the SLL.
add_back()      Adds a new item to the back of the SLL.
add_before()    Adds a new item before a specified item of the SLL.
add_after()     Adds a new item after a specified item of the SLL.
change()        Changes a specified item of the SLL to another.
switch()        Switches two items of the SLL.
search()        Searches the SLL for a specified item.
remove()        Removes a specified item from the SLL.
pop()           Removes the node at the front of the SLL and returns its content.
peek()          Returns the content of the node at the front of the SLL.
reverse()       Reverses the SLL.
clear()         Removes all items from the SLL.
"""


def get_node_list(current_node):
    """
    Returns a list with the content of all connected nodes starting from
    <current_node>. Returns <None> if the node does not exist.

    Note: depending on the way the nodes are linked, some nodes may not be
          returned or there may be an infinite loop.
    """
    # Check if it a valid node
    if (current_node is None):
        return None

    # Add the content of the current node
    node_list = [current_node.get_data()]

    # Loop until the end of the node chain
    current_node = current_node.get_next()
    while (current_node is not None):

        # Append the content of the current node and move to the next node
        node_list.append(current_node.get_data())
        current_node = current_node.get_next()

    return node_list


class SLnode:
    """
    Single-linked node class
    """
    def __init__(self, data, next_node=None):
        """
        Initializes the node content and (if specified) the linked next node.
        """
        self.data = data
        self.next = next_node

    def __repr__(self):
        """
        Returns the string representation of the node.
        """
        return ("SLnode object with data = {}".format(self.data))

    def set_data(self, new_data):
        """
        Set/replaces the content of the node.
        """
        self.data = new_data

    def get_data(self):
        """
        Returns the content of the node.
        """
        return self.data

    def set_next(self, new_next):
        """
        Sets/replaces the linked next node.
        """
        self.next = new_next

    def get_next(self):
        """
        Returns the linked next node.
        """
        return self.next


class SLL:
    """
    Single-linked list class
    """
    def __init__(self, init_list=None):
        """
        Initializes the single-linked list.
        """
        self.head = None
        self.size = 0

        # Initialize to the initial list
        if (init_list is not None):
            for data in init_list:
                self.add_back(data)

    def __repr__(self):
        """
        Returns the string representation of the list.
        """
        return ("SLL object with head pointing to {}".format(self.head))

    def is_empty(self):
        """
        Returns <True> if the list is empty and <False> if it is not.
        """
        return not self.size

    def nodes(self):
        """
        Returns a list with all items contained in the SLL.
        """
        node_list = []
        current_node = self.head

        # Loop until the end of the list
        while (current_node is not None):

            # Append the content of the current node and move to the next node
            node_list.append(current_node.get_data())
            current_node = current_node.get_next()

        return node_list

    def add_front(self, new_data):
        """
        Adds a new item to the front of the list and returns the new node
        object. Works also with an empty list.
        """
        # Create the new node and link it to the current list head
        new_node = SLnode(new_data, next_node=self.head)

        # Set the new node as the new list head
        self.head = new_node

        # Increase the list size
        self.size += 1

        return new_node

    def add_back(self, new_data):
        """
        Adds a new item to the back of the list and returns the new node
        object. Works also with an empty list.
        """
        # Traverse the list to reach the back
        current_node = self.head
        previous_node = None
        while (current_node is not None):
            previous_node = current_node
            current_node = current_node.get_next()

        # Create the new node
        new_node = SLnode(new_data)

        # If the list is empty
        if (self.size == 0):

            # Set the new node as the new list head
            self.head = new_node

        # If the list is not empty
        else:

            # Link the old last node to the new last node
            previous_node.set_next(new_node)

        # Increase the list size
        self.size += 1

        return new_node

    def add_before(self, new_data, ref_data):
        """
        Adds a new item before a specified item of the list and returns the new
        node object. Returns <None> if the specified item is not in the list.

        Note: if the specified item is at the front of the list the result is
              equivalent to a call to method <add_front>.
        """
        current_node = self.head
        previous_node = None

        # Search the list for <ref_data>
        while (current_node is not None):

            # If found, insert the new node between the previous node and the
            # current node
            if (current_node.get_data() == ref_data):

                # Create the new node and link it to the current node
                new_node = SLnode(new_data, next_node=current_node)

                # If the current node is at the front of the list
                if (previous_node is None):

                    # Set the new node as the new list head
                    self.head = new_node

                # If the current node is not at the front of the list
                else:

                    # Link the previous node to the new node
                    previous_node.set_next(new_node)

                # Increase the list size
                self.size += 1

                return new_node

            # If not found, move to the nex node in the list
            else:

                previous_node = current_node
                current_node = current_node.get_next()

        # If <ref_data> is not found
        return None

    def add_after(self, new_data, ref_data):
        """
        Adds a new item after a specified item of the list and returns the new
        node object. Returns <None> if the specified item is not in the list.

        Note: if the specified item is at the back of the list the result is
              equivalent to a call to method <add_back>.
        """
        # Search the list for <ref_data>
        current_node = self.search(ref_data)

        # Insert the new node between the current node and the next node
        if (current_node is not None):

            next_node = current_node.get_next()

            # Create the new node and link it to the next node
            new_node = SLnode(new_data, next_node=next_node)

            # Link the current node to the new node
            current_node.set_next(new_node)

            # Increase the list size
            self.size += 1

            return new_node

        # If <ref_data> is not found
        return None

    def change(self, new_data, ref_data):
        """
        Changes a specified item of the list to another and returns the node
        object. Returns <None> if the specified item is not in the list.
        """
        # Search the list for <ref_data>
        current_node = self.search(ref_data)

        # Change the node content
        if (current_node is not None):

            current_node.set_data(new_data)

        return current_node

    def switch(self, data1, data2):
        """
        Switches two values of the list and returns <True>. Returns <False>
        if either of the items is not in the list.
        """
        # Search the list for <data1> and <data2>
        node1 = self.search(data1)
        node2 = self.search(data2)

        # Switches the content of the two nodes
        if (node1 is not None and node2 is not None):

            node1.set_data(data2)
            node2.set_data(data1)

            return True

        # If either of the data is not found
        return False

    def search(self, data):
        """
        Searches the list for a specified item and returns the corrisponding
        node object. Returns <None> if the specified item is not in the list.
        """
        current_node = self.head

        # Search the list for <data>
        while (current_node is not None):

            # If found, return the current node
            if (current_node.get_data() == data):

                return current_node

            # If not found, move to the successive node in the list
            else:

                current_node = current_node.get_next()

        # If <data> is not found
        return None

    def remove(self, data):
        """
        Removes a specified item from the list and returns <True>. Returns
        <False> if the specified item is not in the list.
        """
        current_node = self.head
        previous_node = None

        # Search the list for <data>
        while (current_node is not None):

            next_node = current_node.get_next()

            # If found, remove the current node from the list
            if (current_node.get_data() == data):

                # If <data> is at the front of the list
                if (previous_node is None):

                    # Set the next node as the new list head
                    self.head = next_node

                # If <data> is not at the front of the list
                else:

                    # Link the previous node to the next node
                    previous_node.set_next(next_node)

                # Decrease the list size
                self.size -= 1

                return True

            # If not found, move to the successive node in the list
            else:

                previous_node = current_node
                current_node = next_node

        # If <data> is not found
        return False

    def pop(self):
        """
        Removes the node at the front of the list and returns its content.
        Returns <None> if the list is empty.
        """
        # Check if the list is empty
        if (self.size == 0):
            return None

        # Value at the front of the list
        data = self.head.get_data()

        # Set the next node as the new list head
        self.head = self.head.get_next()

        # Decrease the list size
        self.size -= 1

        return data

    def peek(self):
        """
        Returns the content of the node at the front of the list without
        removing it. Returns <None> if the list is empty.
        """
        # Check if the list is empty
        if (self.size == 0):
            return None

        # Value at the front of the list
        else:
            return self.head.get_data()

    def reverse(self):
        """
        Reverses the SLL.
        """
        # If the SLL is empty
        if (self.size == 0):
            return

        # If the SLL is not empty
        previous_node = None
        current_node = self.head

        # Loop until the end of the list
        while (current_node is not None):

            # Save the next node link of the current node
            next_node = current_node.get_next()

            # Link the current node to the previous node
            current_node.set_next(previous_node)

            # Move to the successive node in the list
            previous_node = current_node
            current_node = next_node

        # Set the new list head
        self.head = previous_node

    def clear(self):
        """
        Removes all items from the list.
        """
        self.head = None
        self.size = 0


if __name__ == '__main__':
    """
    Test the SLnode and SLL classes.
    """
    print('\nCreate the SLL with an initial list')
    sll = SLL([3, (6.4, 3.3), True, 'hello'])
    print('- SLL:', sll.nodes())            # [3, (6.4, 3.3), True, 'hello']
    print('- size:', sll.size)              # 4

    print('\nClear the SLL and check if empty')
    sll.clear()
    print('- SLL:', sll.nodes())            # []
    print('- empty?', sll.is_empty())       # True

    print('\nAdd items')
    sll.add_front(1.5)
    sll.add_front('2')
    sll.add_back(-5)
    sll.add_back('world')
    sll.add_before(-10, -5)
    sll.add_before(111, '2')
    print('- add 1 before 3:', sll.add_before(1, 3))        # None
    sll.add_after(0, '2')
    sll.add_after('hello', 'world')
    print('- add 1 after 3:', sll.add_after(1, 3))          # None
    print('- SLL:', sll.nodes())    # [111, '2', 0, 1.5, -10, -5, 'world', 'hello']

    print('\nChange and switch items')
    sll.change(10, -10)
    sll.change('Charlie', 'world')
    print('- change 3 with 0.2:', sll.change(0.2, 3))       # None
    sll.switch(111, 'hello')
    sll.switch('2', -5)
    print('- switch 3 with 0.2:', sll.switch(0.2, 3))       # False
    print('- SLL:', sll.nodes())    # ['hello', -5, 0, 1.5, 10, '2', 'Charlie', 111]

    print('\nRemove items')
    sll.remove('hello')
    sll.remove(111)
    sll.remove('Charlie')
    print('- remove 3:', sll.remove(3))         # False
    print('- SLL:', sll.nodes())                # [-5, 0, 1.5, 10, '2']

    print('\nSearch items')
    print('-', sll.search(-5))              # SLnode object with data = -5
    print('-', sll.search(1.5))             # SLnode object with data = 1.5
    print('- search 3:', sll.search(3))     # None

    print('\nExamples using <get_node_list>')
    node = sll.search(1.5)
    print('- from 1.5:', get_node_list(node))   # [1.5, 10, '2']
    node = sll.search(-5)
    print('- from -5:', get_node_list(node))    # [-5, 0, 1.5, 10, '2']

    print('\nReverse and pop all items plus one')
    sll.reverse()
    print('- reversed SLL:', sll.nodes())       # ['2', 10, 1.5, 0, -5]
    print('- item returned:', sll.pop())        # '2'
    print('- item returned:', sll.pop())        # 10
    print('- item returned:', sll.pop())        # 1.5
    print('- item returned:', sll.pop())        # 0
    print('- item returned:', sll.pop())        # -5
    print('- item returned:', sll.pop())        # None
    print('- SLL:', sll.nodes())                # []
    print('- size:', sll.size)                  # 0
