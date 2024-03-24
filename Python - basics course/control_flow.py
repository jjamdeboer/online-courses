if 1==1:
    print("YES")
elif 2==2:
    print("YEEEEEEEEEEEEEEEES")
else:
    print("NOOOO")

lizt = [1, "Hello", ["World,", {5,6,1,"DURK"}],4.0]

for item in lizt:
    print(item)

for letter in "DURK":
    print(letter)

for tup in (2,1,3,4,1,24,14,1):
    print(tup)

# TUPLE UNPACKING

lizzy = [(1,2),(3,4),(2,3),(2,4)]

for (s,d) in lizzy:
    print(s,d)

# CAN ALSO BE USED FOR DICTIONAIRIES

dic = {'k':3,'l':"NOOOOOOOOOOOOOOOOOOOOOO",'m':1}

for (h,i) in dic.items():
    print(i)

while i<5:
    print(i)
    i += 1

# BREAK, CONTINUE, PASS

# PASS DOES NOTHING, PREVENTS YOUR LOOPS FROM BREAKING DOWN WHEN YOU DON'T FILL IN SOMETHING
for tup in (2,1,3,4,1,24,14,1):
    pass

# CONTINUE RETURNS TO ENCAPSULATING LOOP ASAP
for tup in (2,1,3,"GAAAWD"):
    if tup == 2 or tup == 1 or tup == 3:
        continue
    print(tup)

# BREAK STOPS ENCAPSULATING LOOP
while True:
    print(i)
    i += 2
    if i > 20:
        break

# ENUMERATE RETURNS TUPLES
for durk,durkudurk in enumerate('DURKDURKUDURK'):
    print(durk, durkudurk)

# ZIP 'ZIPS' MULTIPLE LISTS TOGETHER, RETURNS TUPLES
print(list(zip(lizzy,lizt)))

# IN CHECKS IF VARIABLE IS IN LIST, TUPLE, DICTIONAIRY
print('k' in dic,3 in dic.values())

print(min((2,1,3,4,1,24,14,1)),max((2,1,3,4,1,24,14,1)))

hasdhasdh = input('WHAT WHAT WHAT: ')
# INPUT RETURNS A STRING
print(hasdhasdh)

# LIST COMPREHENSIONS
WHAAAAAT = [xxx*3 for xxx in "WHAAAAAT" if xxx != 'H']
print(WHAAAAAT)