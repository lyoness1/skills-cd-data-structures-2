# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if not my_list:
        return
    print my_list[0]
    print_item(my_list[1:])


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    print tree.data
    for child in tree.children:
        print_all_tree_data(child)

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    if not my_list:
        return 0
    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.
nodes = []
def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> four = Node(4)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> two.add_child(four)
        >>> num_nodes(one)
        4
    """

    # nodes.append(tree.data)
    # if tree.children:
    #     for child in tree.children:
    #         num_nodes(child)
    # return len(nodes)

# I spent three hours on this one... it's super easy to use a list or counter
# globally, but I can't, for the life of me, figure out how to do this without
# the global variable :(

    count = 1
    for child in tree.children:
        count += num_nodes(child)
    return count

# UPDATE: After I wrote lines 86-94, I came up with lines 96-99 in about 10 min
# I've never felt such a love-hate relationship with anyone or anything as I do
# with recursion!!

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
