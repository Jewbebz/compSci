#Dictionaries are Python's main mapping type. It maps hashable values to arbitrary
#objects. Dictionaries are like hashes in Ruby and Perl, and hash tables in C.
#
#You can create a dictionary with the {"key":"value"} syntax, using the dict
#constructor or even with the elp of the zip method that return tuples:
dictionary = {"first":"1st", "second":"2nd", "third":"3rd"}
dictionary1 = {"first":1, "second":2, "third":3}
dictionary2 = dict(first=1, second=2)
dictionary3 = dict(zip(["first", "Second"], [1, 2]))
dictionary4 = dict({"first":1, "second":2})

#You can use the iner function to get an iterator over the keys in the dictionary:
it = iter(dictionary1)
type(it)

for k in it: print(k)

#You counld also concantonate two dictionaries using update:
prefs = {"fruit":"apple", "Car":"Tesla"}
prefs2 = {"fruit":"orange"}
prefs.update(prefs2)
print(prefs)
#Be careful when using update, as a dictionary cannot have multiple entries with
#the same key.

#You can create a new dictionary using the elements in a sequence (seq below) as
#keys:
seq = ("one", "two")
newDict = dict.fromkeys(seq)
#new dict is {"one":"None", "two":"None"}
newDict = dict.fromkeys(seq,10)
print(newDict)
