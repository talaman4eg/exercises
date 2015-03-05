#!/usr/bin/python

class CustomData(object):
    """User Data object
    
    As simple as possible
    Created for a case if we want to extend user attributes
    """
    def __init__(self, email):
        self.email = email
        
    def __str__(self):
        return self.email
    
    def get_id(self):
        """QuickUF rely on this method
        
        Objects with same id assumed as same
        """
        return self.email

class QuickUF(object):
    def __init__(self):
        self.itemlist = {}
        
    def exists(self, item):
        """ Check if item already added
        """
        return item.get_id() in self.itemlist
    
    def wrapped(self, item):
        """ Check if CustomData item needs to me wrapped into QuickUFItem
        """
        return isinstance(item, QuickUF.QuickUFNode)
        
    def wrap(self, item):
        """ Wrap CustomData item into QuickUFItem. 
        
        If item already exists - return existing item
        """
        if not self.wrapped(item):
            item = QuickUF.QuickUFNode(item)
        return self.itemlist[item.get_id()] if self.exists(item) else item

    def add_item(self, item, parent = False):
        """ Add new item to list
        """
        item = self.wrap(item)
        if parent != False and not self.wrapped(parent):
            parent = self.wrap(parent)
        if not self.exists(item):
            self.itemlist[item.get_id()] = item
            if(parent):
                item.set_parent(parent)
 
    def union(self, item1, item2):
        """ Union two items and their childs into one set
        """
        item1, item2 = self.wrap(item1), self.wrap(item2)
        if not self.exists(item1):
            if not self.exists(item2):
                self.add_item(item1)
                self.add_item(item2, item1)
            else:
                root = self.find_root(item2)
                self.add_item(item1, root)
        elif not self.exists(item2):
            root = self.find_root(item1)
            self.add_item(item2, root)
        else:
            root1, root2 = self.find_root(item1), self.find_root(item2)
            if root1.get_id() == root2.get_id():
                pass
            else:
                if root1.weight < root2.weight:
                    item1.set_parent(root2)
                else:
                    item2.set_parent(root1)
                

    def find_root(self, node):
        """ Find root of the node
        """
        node = self.wrap(node)
        if not self.exists(node):
            self.add_item(node)
            return node
        elif not node.has_parent():
            return node
        else:
            return self.find_root(node.parent)

    def find(self, item1, item2):
        """ Finds if items are connected
        
        Don't need this method for current task, but it is part of Union-Find algorythm
        """
        return self.find_root(item1).get_id() == self.find_root(item2).get_id()
    
    class QuickUFNode(object):
        """ Wrapper of the CustomData object for QuickUF

        item - link to item
        weight - count of descendants
        parent - parent node, False of root
        """
        def __init__(self, item):
            self.item = item
            self.weight = 1
            self.parent = False

        def has_parent(self):
            return self.parent and self.parent.get_id()

        def set_parent(self, parent):
            self.parent = parent
            parent.weight += self.weight

        def get_id(self):
            return self.item.get_id()

        def get_item(self):
            return self.item


if __name__ == "__main__": 
    """
    
    """
    
    import sys

    DATE_INDEX = 0
    SENDER_INDEX = 1
    RECIPIENT_INDEX = 2
    FIELD_SEPARATOR = "\t";
    CLUSTER_MIN_LENGTH = 3

    PRINT_SEPARATOR = ', '
    FILE_NAME = ''

    

    if len(sys.argv) > 1:
        FILE_NAME = sys.argv[1]
    
    WELCOME_TEXT = "Activity Parser\n\
    USAGE: \n\
    activity_parser.py INPUT_FILE"
    
    if not FILE_NAME:
        print WELCOME_TEXT
        sys.exit()

    clusters = {}

    try:
        f = open(FILE_NAME, 'r')
        quick_uf = QuickUF()
        for line in f:
            parts = line.strip().split(FIELD_SEPARATOR)
            if len(parts) < 3:
                continue
            sender, recipient = CustomData(parts[SENDER_INDEX].strip()), CustomData(parts[RECIPIENT_INDEX].strip())
            quick_uf.union(sender, recipient)

        for id, node in quick_uf.itemlist.iteritems():
            root = quick_uf.find_root(node)
            if root:
                if not root.get_id() in clusters:
                    clusters[root.get_id()] = []
                clusters[root.get_id()].append(node.get_item())

        for root in clusters:
            if len(clusters[root]) < CLUSTER_MIN_LENGTH:
                continue
            clusters[root].sort()
            print PRINT_SEPARATOR.join(map(str, clusters[root]))
    except IOError:
        print "Error: cannot read input file '%s'" % FILE_NAME
        print WELCOME_TEXT

    
    
    

    
