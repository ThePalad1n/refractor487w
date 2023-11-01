# ### Doubly Linked List
# 
# The purpose of this assignment is to make you familiar with implementing a data structure in Python in an object oriented way.
# During lectures we implemented a few simple linear data structres: queue, list, deques, stacks. Now we expect you to implement one of these structures yourself.
# 
# You are provided with two classes: **Node** and **DoublyLinkedList**. The first one is already implemented (you don't need to modify it), the second one consist only a structure of empty methods defined. Your task is to come up with an implementation of these methods.
# 
# _Note_: If a list is doubly linked, each node contains a reference to the _previous_ node in the chain and a reference to the _next_ node.
# 
# You are expected to implement every function in DoublyLinkedList. Including the *next()* function, which is used by an iterator object in python. The *map(func)* function applies a function to every element in the list.
# All other functions are available in the PSADS book.

# ## Constructing a Doubly Linked List
# 
# The **Node** class implementation is already given:



class Node(object):
    """Doubly linked node which stores an object"""

    def __init__(self, element, next_node=None, previous_node=None):
        # The underscores are to prevent overwriting the variables if inherited and prevents access from outside of scope
        self.__element = element
        self.__next_node = next_node
        self.__previous_node = previous_node

    def get_element(self):
        """Returns the element stored in this node"""
        return self.__element

    def get_previous(self):
        """Returns the previous linked node"""
        return self.__previous_node

    def get_next(self):
        """Returns the next linked node"""
        return self.__next_node

    def set_element(self, element):
        """Sets the element stored in this node"""
        self.__element = element

    def set_previous(self, previous_node):
        """Sets the previous linked node"""
        self.__previous_node = previous_node

    def set_next(self, next_node):
        """Sets the next linked node"""
        self.__next_node = next_node
    
    def __repr__(self):
        return str((self.__element, self.get_next()))


# The following code snippet is a constructor provided by the **DoublyLinkedList** Python class for the creation of a new doubly linked list. **Extend the snippet below with your implementation of the DoublyLinkedList**. 




class DoublyLinkedList(object):
    """Doubly linked node data structure"""

    def __init__(self):
        self.__size = 0
        self.__header = Node('Header')
        self.__trailer = Node('Trailer')
        self.__header.set_next(self.__trailer)
        self.__trailer.set_previous(self.__header)
        self.__current = None

    def __repr__(self):
        return str(self.get_first())
    def __iter__(self):
        self.__current = None
        return self

    def __next__(self):
        """Standard python iterator method"""
        if self.is_empty() or self.__current == self.__trailer:
            raise StopIteration()
        elif self.__current is None:
            self.__current = self.__header
        self.__current = self.__current.get_next()
        if self.__current != self.__trailer:
            return self.__current
        else: 
            raise StopIteration()

    def map(self, function):
        """Run function on every element in the list"""
        for node in self:
            if node != self.__trailer and node != self.__header:
                node.set_element(function(node.get_element()))

    def size(self):
        """Returns the number of elements in the list"""
        return self.__size

    def is_empty(self):
        """Returns the number of elements in the list"""
        return self.__size == 0

    def get_first(self):
        """Get the first element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__header.get_next()

    def get_last(self):
        """Get the last element of the list"""
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__trailer.get_previous()

    def get_previous(self, node):
        """Returns the node before the given node"""
        if node == self.__header:
            raise Exception("Cannot get the element before the header of this list")
        else:
            return node.get_previous()

    def get_next(self, node):
        """Returns the node after the given node"""
        if node == self.__trailer:
            raise Exception("Cannot get the element after the trailer of this list")
        else:
            return node.get_next()

    def add_before(self, new, existing):
        """Insert the new before existing"""
        previous_existing = self.get_previous(existing)
        new.set_previous(previous_existing)
        new.set_next(existing)
        existing.set_previous(new)
        previous_existing.set_next(new)
        self.__size += 1

    def add_after(self, new, existing):
        """Insert the new after existing"""
        next_existing = self.get_next(existing)
        new.set_previous(existing)
        new.set_next(next_existing)
        existing.set_next(new)
        next_existing.set_previous(new)
        self.__size += 1

    def add_first(self, new):
        """Insert the node at the head of the list"""
        self.add_after(new, self.__header)

    def add_last(self, new):
        """Insert the node at the tail of the list"""
        self.add_before(new, self.__trailer)

    def remove(self, node):
        """Removes the given node from the list"""
        before = self.get_previous(node)
        after = self.get_next(node)
        before.set_next(after)
        after.set_previous(before)
        node.set_next(None)
        node.set_previous(None)
        self.__size -= 1


# **Task 1 (5 points)**: Using the constructor from the **DoublyLinkedList**, create a new doubly linked list of random integers between 1 and 10.

# In[3]:


dL = DoublyLinkedList()

for i in range(4):
    dL.add_last(Node(i))

print(dL)

assert str(dL) == f"(0, (1, (2, (3, ('Trailer', None)))))"


# ## Using a Doubly Linked List
# 
# The given **DoublyLinkedList** Python class
# contains helpful methods for using a doubly linked list.
# Answer the following questions while implementing
# the methods of the **DoublyLinkedList** class.
# 
# **Task 2 (10 points)**: Implement the `size` method that returns the size of a doubly linked list.
# 
# ```python
# def size(self):
#   """Returns the number of elements in the list."""
#   pass 
# ```

# In[4]:


#Test your implementation here
print(dL.size())
assert dL.size() == 4


# **Task 3 (5 points)**: Implement the `is_empty` method that checks
# whether a doubly linked list is empty.
# 
# ```python
# def is_empty(self):
#   """Returns the number of elements in the list"""
#   pass
# ```

# In[5]:


#Test your implementation here
print(dL.is_empty())

dL2 = DoublyLinkedList()
print(dL2.is_empty())


assert dL.is_empty() == False
assert dL2.is_empty() == True
del dL2


# **T4 (10 points)**: Implement the methods `get_first` and `get_last`
# to get the first and the last element of the list, respectively.
# 
# _Hint_: Return an exception in case the list is empty.
# 
# ```python
# def get_first(self):
#   """Get the first element of the list"""
#   pass
# 
# def get_last(self):
#   """Get the last element of the list"""
#   pass
# ```

# In[6]:


#Test your implementation here
print(dL.get_first())
print(dL.get_last())

assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"
assert str(dL.get_last()) == f"(3, ('Trailer', None))"


# **Task 5 (10 points)**: Implement the methods `get_previous` and `get_next`
# to get the previous and the next node of the list, respectively.
# 
# _Hint_: Return an exception in case the list is empty.
# 
# ```python
# def get_previous(self, node):
#   """Returns the node before the given node"""
#   pass      
# 
# def get_next(self, node):
#   """Returns the node after the given node"""
#   pass
# ```

# In[7]:


#Test your implementation here
print(dL.get_last().get_previous())
print(dL.get_first().get_next())

assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"
assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"


# **Task 6(10 points)**: Implement the methods `add_before` and `add_after`
# to respectively insert new elements before and after a node of the list.
# 
# ```python
# def add_before(self, new, existing):
#   """Insert the new before existing"""
#   pass
# 
# def add_after(self, new, existing):
#   """Insert the new after existing"""
#   pass
# ```

# In[8]:


#Test your implementation here
dL.add_after(Node(42),dL.get_first())
dL.add_before(Node(34),dL.get_last())

print(dL)
assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"


# **Task 7 (10 points)**: Implement the methods `add_first` and `add_last`
# to respectively insert new nodes in the beginning and in the end of a list.
# 
# ```python
# def add_first(self, new):
#   """Insert the node at the head of the list"""
#   pass
# 
# def add_last(self, new):
#   """Insert the node at the tail of the list"""
#   pass
# ```

# In[17]:


#Test your implementation here
dL.add_first(Node(7))
dL.add_last(Node(-1))
print(dL)
assert str(dL) == "(7, (0, (42, (1, (2, (34, (3, (-1, ('Trailer', None)))))))))"


# **Task 8 (10 points)**: Implement the method `remove` to remove
# a node from a list.
# 
# ```python
# def remove(self, node):
#   """Removes the given node from the list"""
#   pass
# ```

# In[16]:


#Test your implementation here
dL.remove(dL.get_first())
print(dL.get_first())

assert dL.get_first().get_element() == 0


# **Task 9 (10 points)**: Implement the method `map` to apply a function on
# each element of a list.
# 
# ```python
# def map(self, function):
#   """Run function on every element in the list"""
#   pass
# ```

# In[15]:


#Test your implementation here
dL.map(lambda x: x**2)

print(dL)

assert str(dL) == "(0, (1764, (1, (4, (1156, (9, (1, ('Trailer', None))))))))"


# **Task 10 (10 points)**: Implement the method `next` to iterate the elements
# of a list.
# 
# ```python
# """Standard methods for Python iterator"""
# def __iter__(self):
#   pass
# 
# def __next__(self):
#   pass
# ```

# In[13]:


#Test your implementation here


for node in dL: 
    print(node.get_element() == dn.__next__().get_element())
    print(dn)


dL


# 
# ## Applying methods of the DoublyLinkedList and Node classes
# 
# Answer the following questions by using
# the implemented methods from the Node and DoublyLinkedList classes.
# Apply your operations on the list you created in T1.

# **Task 11 (5 points)**: Add 2 to each element of the list.
# 
# _Hint_: Use the methods `map`.

 


def twenties():
    LL = DoublyLinkedList()
    for t in range(20,30):
        LL.add_last(Node(t))
    return LL

doubleDigits = twenties()

doubleDigits.map(lambda x: x+10)

print(doubleDigits)
assert str(doubleDigits) =="(30, (31, (32, (33, (34, (35, (36, (37, (38, (39, ('Trailer', None)))))))))))"


# 
# **Task 12 (5 points)**: Multiply each element of the list by 5.
# 
# _Hint_: Use the methods `map`, `get_previous`, and `set_element`.

 


doubleDigits = twenties()
def mult_five(x):
    return x*5
doubleDigits.map(mult_five)
str(doubleDigits)

for d in doubleDigits: 
    if d and d.get_element() %4 ==0: 
            doubleDigits.remove(d)
str(doubleDigits)


# 
# **Task 13 (5 points)**: Remove elements that are multiples of 3.
# 
# _Hint_: Use the methods `next` and `remove`.

 


current = doubleDigits.get_first()
while(current != doubleDigits.get_last().get_next()):
    next = current.get_next()
    if (current.get_element() % 4 == 0):
        doubleDigits.remove(current)
        
    current = next
    print(current)

str(doubleDigits)


# 
# **Task 14 (5 points)**: Remove elements from the list that are odd numbers. 
# 
# _Hint_: Use the methods `get_previous` and `remove`.

 


current = doubleDigits.get_first()
while(current != doubleDigits.get_last().get_next()):
    next = current.get_next()
    if (current.get_element() % 2 == 1):
        doubleDigits.remove(current)
        
    current = next

str(doubleDigits)


