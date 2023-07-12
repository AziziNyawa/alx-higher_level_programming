#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references of class list

    Arguments:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the list in sorted form """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
