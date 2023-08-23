# 6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.


list = ["hello","1",2,7,4,5,95,"bittu","bhadra"]
list1 = ["andhra",1,6,3,"i","kolkata",1,88,77,"car","mysore"]

def fun(list,x):
    list2 = []
    for i in range(len(list)):
        if(i%2!=0):
            list2.append(list[i])
    for z in range(len(x)):
        if(z%2==0):
            list2.append(x[z])
    return list2



print(fun(list,list1))
