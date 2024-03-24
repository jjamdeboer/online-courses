# SORT DOES NOT RETURN ANYTHING, PERFORMS ACTION ON ORIGINAL LISTS
# CAN MERGE AND SPLIT LISTS, LIKE STRINGS

lizt = ["Hello", "World", "I", 4, 5.6, 4.6]
print("Length of list is " + str(len(lizt)) + ", with second element being " + str(lizt[1]))
lizzy = [3, 5555555, "DUUU"]
print(lizt)
print(lizzy)
print(lizt + lizzy)
print(lizt.pop(4))
lizt.reverse()
print(lizt)
unsorted_lizzy = [1,3,1,32,3,2,3,3,12,1,213,12,112,3123,123,1231,3]
unsorted_lizzy.sort()
print(unsorted_lizzy)
print(unsorted_lizzy[3::2])