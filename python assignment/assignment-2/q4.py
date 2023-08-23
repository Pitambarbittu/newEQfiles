# 4.Reverse the list by using negative index and apply logic also.

# Reverse the list
p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(p[::-1])


# using logic with hey how are you.
def fun(ab):
    
    x = len(ab)
    list = []
    for i in range(x-1, -1, -1):
        list.append(ab[i])
    return list

x = ["you?","are","how","hey"]
print(fun(x))
