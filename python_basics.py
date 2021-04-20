
# This is a comment

# Python Types
this_is_a_string = "this is a string"
this_is_a_list = ["list_item_1", "list_item_2"]
this_is_a_dictionary = {"key_1": "value_1", "key_2": this_is_a_list}

# Conditional Statements
if "list_item_1" in this_is_a_list:
    print("Found list_item_1 in this_is_a_list!")

# Loops
for _ in this_is_a_list:
    print(_) # Prints "list_item_1\n", "list_item_2\n"

# Enum
# A class in python for creating enumerations, which are a set of symbolic names (members).
# Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
# Because Enums are used to represent constants use UPPER_CASE names for enum members.

import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# print the enum member as a string
print ("The enum member as a string is : ",end="")
print (Days.Mon)

# print the enum member as a repr
print ("he enum member as a repr is : ",end="")
print (repr(Days.Sun))

# Check type of enum member
print ("The type of enum member is : ",end ="")
print (type(Days.Mon))

# print name of enum member
print ("The name of enum member is : ",end ="")
print (Days.Tue.name)
