#!/usr/bin/python
import bisect

def is_prime(num, found_primes = [2]):
    try:
        for i in found_primes:
            if num % i == 0:
                return False
            
        if len(found_primes) < 1:
            start = 2
        else:
            start = found_primes[len(found_primes) - 1]
            
        for i in xrange(start, num/2):
            if not is_prime(i):
                continue
            elif num % i == 0:
                return False
    except Exception:
        pass
    
    found_primes.append(num)
    return True


def bisect_exists(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False    

def bisect_index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

def bisect_diff(source, target):
    for ind, key in enumerate(target):
        index = bisect_index(source, key)
        if index > -1:
            del source[index]
    return source

class CustomData(object):
    """User Data object
    
    As simple as possible
    Created for a case if we want to extend user attributes
    """
    
    next_id = {}
    
    def __init__(self, email):
        self.email = email
        
    def __str__(self):
        return self.email
    
    def get_id(self):
        return self.email
    

class Clique(object):
    
    MIN_CLUSTER = 3
    
    def __init__(self):
        self.itemlist = {}
        self.clusters = []
        self.indexlist = {}
        
    def exists(self, item):
        """ Check if item already added
        """
        return item.get_id() in self.itemlist
    
    def wrapped(self, item):
        """ Check if CustomData item needs to me wrapped into CliqueItem
        """
        return isinstance(item, Clique.CliqueNode)
        
    def wrap(self, item):
        """ Wrap CustomData item into CliqueItem. 
        
        If item already exists - return existing item
        """
        if not self.wrapped(item):
            item = Clique.CliqueNode(item)
        return self.itemlist[item.get_id()] if self.exists(item) else item

    def add_item(self, item):
        """ Add new item to list
        """
        item = self.wrap(item)
        if not self.exists(item):
            self.itemlist[item.get_id()] = item
            #item.set_id(len(self.itemlist))
        return item
 
    def union(self, source, destination):
        source = self.add_item(source)
        destination = self.add_item(destination)
        if destination.get_id() != source.get_id():
            source.relate(destination)
    
    def item_index_sorter(self, key):
        return self.itemlist[key].get_index()
        
    def prepare_itemlist(self):
        
        #print repr(self.itemlist)
        
        oldlen = -1
        while oldlen != len(self.itemlist):
            oldlen = len(self.itemlist)
            self.indexlist = {}
            
            i = 0
            too_small = []
            for item in self.itemlist:
                if len(self.itemlist[item].relations) < Clique.MIN_CLUSTER - 1:
                    too_small.append(item)
                    continue
                self.indexlist[item] = i
                i += 1

            for item in too_small:
                del self.itemlist[item]

            for key in self.itemlist:
                self.itemlist[key].relations[:] = [relkey for relkey in \
                        self.itemlist[key].relations if relkey in self.itemlist]

        for item in self.indexlist:
            key = self.indexlist[item]
            self.itemlist[item].relations[:] = sorted([self.indexlist[relkey] \
                for relkey in self.itemlist[item].relations if relkey in self.indexlist])
            self.itemlist[key] = self.itemlist[item]
            del self.itemlist[item]
        
    def find_cliques(self):
        self.prepare_itemlist()

        for key in self.itemlist:
            #find and remove single-side relation
            for relkey in self.itemlist[key].relations:
                if not bisect_exists(self.itemlist[relkey].relations, key):
                    index = bisect_index(self.itemlist[key].relations, relkey)
                    del self.itemlist[key].relations[index]

            #remove items that already in clusters from checklist
            checklist = self.itemlist[key].relations[:]
            for cluster in self.clusters:
                if bisect_exists(cluster, key):
                    checklist = bisect_diff(checklist, cluster)

            #build cliques
            while len(checklist) > 0:
                cluster = [key, checklist[0]]
                for relkey in self.itemlist[key].relations:
                    if checklist[0] == relkey:
                        continue

                    add = True
                    for cluskey in cluster:
                        if not bisect_exists(self.itemlist[relkey].relations, cluskey):
                            add = False
                            break
                    if add:
                        cluster.append(relkey)

                if len(cluster) > 2:
                    cluster.sort()
                    self.clusters.append(cluster)
                checklist = bisect_diff(checklist, cluster)

    
    class CliqueNode(object):
        """ Wrapper of the CustomData object for Clique

        item - link to item
        weight - count of descendants
        parent - parent node, False of root
        """
        def __init__(self, item):
            self.item = item
            self.relations = []
            self.id = str(self.get_index())
            
        def __repr__(self):
            return str(self.relations)

        def relate(self, item):
            if not item.get_id() in self.relations:
                self.relations.append(item.get_id())

        def get_id(self):
            return self.id
        
        def set_id(self, id):
            self.id = id
            
        def get_index(self):    
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

    try:
        f = open(FILE_NAME, 'r')
        graph = Clique()
        for line in f:
            parts = line.strip().split(FIELD_SEPARATOR)
            if len(parts) < 3:
                continue
            sender, recipient = CustomData(parts[SENDER_INDEX].strip()), CustomData(parts[RECIPIENT_INDEX].strip())
            graph.union(sender, recipient)


        graph.find_cliques()
        clusters = []
        for nodes in graph.clusters:
            cluster = []
            for node in nodes:
                cluster.append(graph.itemlist[node].get_item())
            clusters.append(cluster)
                
        #clusters = [node.get_item() for node in cluster for cluster in graph.clusters]
        
        def clusters_sorter(key):
            return len(key)

        output = []
        for cluster in clusters:
            prepared = map(str, cluster)
            prepared.sort()
            output.append(PRINT_SEPARATOR.join(prepared))
        
        del clusters
        #output.sort(clusters_sorter)
        sorted(output, len)
        
        for line in output:
            print line
        
            
    except IOError:
        print "Error: cannot read input file '%s'" % FILE_NAME
        print WELCOME_TEXT

    
    
    

    
