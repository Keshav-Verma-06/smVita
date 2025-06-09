myset = {1, 2, 3, 4, 5, True, False, "Hello", "World"}
print(myset)  # Output: {1, 2, 3, 4, 5}
print(type(myset))  # Output: <class 'set'>
myset.add(6)  # Adding an element   
print(myset.value())  # Output: {1, 2, 3, 4, 5, 6}
myset.remove(3)  # Removing an element
print(myset.pop())  # Output: 1 (removes and returns an arbitrary element)
print(myset)  # Output: {2, 4, 5, 6} (3 is removed)     
myset.clear()  # Clearing the set
print(myset)  # Output: set() (empty set)
myset = {1, 2, 3, 4, 5} 
print(myset)  # Output: {1, 2, 3, 4, 5}
myset.update([6, 7, 8])  # Adding multiple elements
print(myset)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}        
myset.discard(2)  # Discarding an element (does not raise an error if not found)
print(myset)  # Output: {1, 3, 4, 5, 6, 7, 8}
myset = {1, 2, 3, 4, 5}
print(myset)  # Output: {1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8}
print(myset2)  # Output: {4, 5, 6, 7, 8}
print(myset.union(myset2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8} (union of two sets)
print(myset.intersection(myset2))  # Output: {4, 5} (intersection of two sets)
print(myset.difference(myset2))  # Output: {1, 2, 3} (elements in myset not in myset2)
print(myset2.difference(myset))  # Output: {6, 7, 8} (elements in myset2 not in myset)
print(myset.issubset(myset2))  # Output: False (myset is not a subset of myset2)
print(myset2.issubset(myset))  # Output: False (myset2 is not a subset of myset)    
print(myset.issuperset(myset2))  # Output: False (myset is not a superset of myset2)
print(myset2.issuperset(myset))  # Output: False (myset2 is not a superset of myset)
print(myset.isdisjoint(myset2))  # Output: False (myset and myset2 have common elements)
print(myset2.isdisjoint({9, 10}))  # Output: True (myset2 has no common elements with {9, 10})
myset = {1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8}        
print(myset.symmetric_difference(myset2))  # Output: {1, 2, 3, 6, 7, 8} (elements in either set but not both)
print(myset.symmetric_difference_update(myset2))  # Updates myset to {1, 2, 3, 6, 7, 8} 
print(myset)  # Output: {1, 2, 3, 6, 7, 8} (myset is now updated)
# Note: The `value()` method does not exist for sets in Python.
# The correct method to view the contents of a set is to simply print it.
# The `pop()` method removes and returns an arbitrary element from the set.
# If you want to see the contents of the set after popping an element, you can print it again.
# The `update()` method adds multiple elements to the set.
# The `discard()` method removes an element from the set if it exists, without raising an error if it does not.
# The `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`, and `isdisjoint()` methods are used to perform set operations. 
# The `symmetric_difference()` method returns a new set with elements in either set but not both.
# The `symmetric_difference_update()` method updates the set to contain the symmetric difference.
# The `clear()` method removes all elements from the set, resulting in an empty set.
# The `add()` method adds a single element to the set.
# The `remove()` method removes a specific element from the set, raising an error if the element is not found.
# The `pop()` method removes and returns an arbitrary element from the set.
# The `discard()` method removes an element from the set if it exists, without raising an error if it does not.
# The `update()` method adds multiple elements to the set.
# The `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`, and `isdisjoint()` methods are used to perform set operations.
# The `symmetric_difference()` method returns a new set with elements in either set but not both.
# The `symmetric_difference_update()` method updates the set to contain the symmetric difference.
# The `clear()` method removes all elements from the set, resulting in an empty set.
# The `value()` method does not exist for sets in Python.
# The correct way to view the contents of a set is to simply print it.
# The `pop()` method removes and returns an arbitrary element from the set.
# The `update()` method adds multiple elements to the set.
# The `discard()` method removes an element from the set if it exists, without raising an error if it does not.
# The `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`, and `isdisjoint()` methods are used to perform set operations.