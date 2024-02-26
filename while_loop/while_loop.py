############################ While Loop #######################

'''count = 1   #### iterator
while count <= 5:
    print("nasim")
    count += 1   ### iteration
print(count)'''

'''iterator = 10

while iterator >= 1:
    print(iterator)
    iterator -= 1'''

############# print 1 to 100 ################

'''iterator = 1

while iterator <= 100:
    print(iterator)
    iterator += 1'''
    

############# print 100 to 1 ################


'''i = 100

while i >= 1:
    print(i)
    i -= 1'''


############# multiple table ################

'''n = int(input("Enter the number: "))

i = 1

while i <= 10:
    print(n* i)
    i += 1 '''


#############  traverse numbers  ################

'''li = [1,2,4,9,16,25,36,49,64,81,100]

idx = 0

while idx < len(li):
    print(li[idx])
    idx += 1 '''


#############   numbers finding ################

'''li = (1,2,4,9,16,25,36,49,64,81,100,49)

num = 49

idx = 0 #initinalize

while idx < len(li):
    if (li[idx] == num):
        print("found num in idx:",idx)
    else:
        print("founding...")

    idx += 1'''


#############   loop method ################

'''count = 1

while count <= 5:
    print(count)
    if (count == 3):
        break
    count += 1'''


'''tup = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter the number: "))

idx = 0

while idx < len(tup):
    if (num == tup[idx]):
        print("found number in idx : ")
        break
    else:
        print("not found")

    idx += 1

print("end loop")'''


'''i = 1

while i <= 5:
    if (i== 3):
        i += 1
        continue
    print(i)
    i += 1'''

'''i = 1

while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1'''

i = 1

while i <= 10:
    if (i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1
        





















