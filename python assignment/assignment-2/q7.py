# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by using list comprehension

# dict ={"key1":1234, "k2":"bittu"}

# list= [1234,"bittu"]

dict={"key1":1234,"k2":"bittu"}
list=[1234,"bittu",1,2,3,4,"pitambar","bhadra"]
list1=[]
for key,value in dict.items():
    for p in list:
        if(value == p):
            list1.append(p)

print(list1)  

