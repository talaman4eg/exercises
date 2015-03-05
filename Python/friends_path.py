import sys


class Person(object):
    def __init__(self, name):
        self.friends = []
        self.name = name
        
    def add_fiend(self, friend):
        self.friends.append(friend)
        
    def get_friends(self):
        return self.friends
    
    def __str__(self):
        return self.name
    
    
users = [Person() for i in xrange(10)]

friend_matrix = [
        [1,2,3,4,5,7,8,9]
        [0,7,8]
        [0,2,4]
        [2,4,7,9]
        [2,3,4,7,8,9]
        [0, 9]
        [3,4,5,8,9]
        [0,1,2,3,4,5,7,9]
        [0,1,2,3,4,5,7]
        [7,8]
    ]
        
for j, flist in enumerate(firend_matrix):
    for i in flist:
        users[j].add_friend(users[i])
        
    print users[j].get_friends()


def is_person_checked(person, list = []):
    """
    this is cache list for already checked persons. we could cache it outside of 
    working memory if it grows abnormally. Also, I use here python’s first call 
    default parameter initialization list = []
    """
    if not person in list:
            list.append(person)
            return False
    return True

def find_path(person1, person2, max_depth = 10):
    
    if person1 == person2:
            return [person1]
    #we want to check if person1 and person2 are correct objects of the class we need
    if not check_correct_class_for_person(person1, person2):
        raise TypeError('Wrong person type')
    if not person1.get_list() or not person2.get_list():
            raise PersonDoesNotHaveAnyFriendError()
    if found_list == None:
        found_list = []

    #breadth-first approach. We need to check friends tree layer by layer, not branch by 
    #branch. Using queue (list_to_check) for that. add new frinds to end 
    #We migth need to cache it if it grows abnormally

    #initially fill list_to_check with person1, level = 0, initial path
    list_to_check = [(person1, 0, [person1])]
    
    while list_to_check:
        person_to_check, level, path = list_to_check.pop()
        for friend in person_to_check.get_friends():
            if is_person_checked(friend):
                continue;
            fpath = path[:] #make a copy of current path
            fpath.append(friend)
            if friend == person2:
                return fpath # Found!
            if level + 1 >= max_depth:
                list_to_check.append((friend, level+1, fpath))
        
    return False # all friends checked, no path found

		

sys.exit()

import heapq
search_string = 'a'
cursor.execute("SELECT text FROM table WHERE text LIKE %s", ("%%s%" % search_string))

#some content to test
#cursor = ['asasas', 'wewe', 'asadafaa', 'qa', 'qwerasdf']

heap = []

for text in cursor:
    count = text.count(search_string)
    #SPL provides only min heap queue. so we going to push negative value of count
    heapq.heappush(heap, (-count, text))
    
while len(heap) > 0:
    print heapq.heappop(heap)[1]


 
 #497 = CDXCVII

def roman_to_arabic(roman):
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    i = len(roman) - 1
    previous = False
    result = 0
    while i >= 0:
        if not roman[i] in symbols:
            raise ValueError('Incorrect roman sign')
        number = symbols[roman[i]]
        if previous == False:
                previous = number
        if number >= previous:
                result += number
        else:
                result -= number
        previous = number
        i -= 1
    return result
