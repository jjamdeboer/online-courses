# KEYS CANNOT BE DICTONAIRIES OR LISTS THEMSELVES, ONLY THE VALUES
# DENOTED BIJ {} LIKE SETS INSTEAD OF [] LIKE LISTS OR () LIKE TUPLES

dic = {1:"HULLLO","HULO":2,3:6,"SWAT":"SWUT",5.555:[1,0,5,4],4:{4:2}}
print(dic)
print(str(dic[3] ) + " " + dic[1])
print(dic[5.555][1])
print(dic[4][4])
dic[4] = "DURP"
print(dic)
print(dic.keys(),dic.values())