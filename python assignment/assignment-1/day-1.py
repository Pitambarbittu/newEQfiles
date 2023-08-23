#1. print prime nos

lower = 0
upper = 30

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num)




#  2. even odd program
a = int(input("Enter a Number : "))
if (a % 2 == 0):
    print("Even")
else:
    print("Odd")




# 3.  create a list with duplicate values and make it unique
list = [5,8,9,8,9,6,10,6,7,10,1,1,2,3,3,4,5,5]

b = set(list)
print("My list : ", list)
print("Non Duplicated Set", b)




#4. create a complex dictionary and traverse through it

c = {1: {"Company": "Cloudeq", "Location": "Mohali"},
     2: {"Company": "Hp", "Location": "Bangalore"},
     3: "hello world"}

for z in c:
    if type(c[z]) is dict:
        for k in c[z]:
            print(k, "=", c[z][k])
    else:
        print(z, "=", c[z])


