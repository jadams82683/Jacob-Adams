for x in range (1, 151):
    print(x)

for x in range (5, 1001, 5):
    print(x)

for x in range (1, 101):
    if (x % 5 == 0) and (x % 10 != 0):
        print("Coding")
    if x % 10 == 0: 
        print ("Coding Dojo")
    else:
        print(x)

sum = 0
for x in range(1, 500001, 2):
    sum = sum + x
print(sum)

for x in range(2018, -1, -4):
    print(x)

lowNum = 7
highNum = 127
mult = 7

for x in range(lowNum, highNum, mult):
    print(x)
        