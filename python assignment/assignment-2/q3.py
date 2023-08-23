# 3. convert a number into binary and binary to number.

#numb into binary
n=int (input ("Enter a number: "))
i= []
while(n > 0):
    digit = n % 2
    i.append(digit)
    n = n//2
    
i.reverse()
print("binary value is: ")
for i in i:
    print(i)



# binary into numb.

p=int(input("enter a binary value: "))

value, i, a = 0, 0, 0

while(p != 0): 
        a = p % 10
        value = value + a * pow(2, i) 
        p = p//10
        i += 1
        
print(value)