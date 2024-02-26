############## for loop ######################

'''li = [1,2,3,4,5]

for i in li:
    print(i)'''

'''li = ['nasim', 'rasel', 'sakib']

for i in li:
    print(i)'''

'''str = "nasimUddin"

for i in str:
    if (i == 'U'):
        print("found U")
        break
    print(i)

print("End")'''


'''str = "nasimUddin"

for i in str:
    if (i == 'U'):
        print("found U")
        break
    print(i)
else:
    print("End")'''




###################### pactice #####################

'''li = [1,4,9,16,25,36,49,64,81,100]

for i in li:
    print(i)'''


'''li = (1,4,9,16,25,36,49,64,81,100,49)

num = 49
idx = 0

for i in li:
    if (i == num):
        print("number is found in idx: ",idx)
        break

    idx += 1'''
    

###################### use range #####################

#print(range(5))

'''sqr = range(5)

print(sqr[0])
print(sqr[1])  # print idx
print(sqr[2])
print(sqr[3])'''



'''sqr = range(10)

for i in sqr:
    print(i)'''

'''for i in range(15):  # stop
    print(i)'''

'''for i in range(2,10): # start, stop
    print(i)'''

'''for i in range(2,10,2): # start, stop, step
    print(i)'''

'''for i in range(2,100,2):
    print(i)'''

'''for i in range(1,100,2):
    print(i)'''


###################### pactices /qs/ #####################

'''for i in range(1,100):
    print(i)'''

'''for i in range(100,1, -1):
    print(i)'''

'''num = int(input("Enter the number: "))

for i in range(1,11):
    print(num*i)'''



###################### pass method #####################


'''for i in range(5):
    pass

print("pass method")'''


###################### pactices /qs/ #####################


'''n = int(input("enter the number: "))

sum = 0

for i in range(1,n+1):
    sum += i
print(sum)'''


'''n = int(input("enter the number: "))

sum = 0

i = 1

while i <= n:
    sum += i
    i += 1

print(sum)'''

'''n = int(input("enter the number: "))

fac = 1

i = 1

while i <= n:
    fac *= i
    i += 1
print(fac)'''

n = int(input("enter the number: "))

fac = 1

for i in range(1,n+1):
    fac *= i
print(fac)

















