# print("daily_participants---------")
# daily_participants(participants_list) # ['Desmond', 'Krish', 'Sam']
# print("one_time_participants---------")
# one_time_participants(participants_list)# ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
# print("first_day_only_participants----------------")
# first_day_only_participants(participants_list) #  ['John', 'Joan']


from collections import Counter
def daily_participants(pp_list):
    dicty = {}
    list = []
    answer = []
    for p in range(len(pp_list)):
        list.append(0)
    for p in range(len(pp_list)):
        for i in range(len(pp_list[p])):
            if pp_list[p][i] not in dicty:
                dicty[pp_list[p][i]] = 0

    for name in dicty:
        flag = 0
        for p in range(len(pp_list)):
            if name not in pp_list[p]:
                flag = 1
        if flag is 0:
            answer.append(name)

    return answer

'''
dict = {
  "sam": 6,
  "jhobn": 1
}
pp_list = [
    ['Sam','John', 'Emma', 'Joan', 'Krish',  'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]'''


def one_time_participants(pp_list):
  all=pp_list[0:]
  z=[]
  pb=[]
  for list in pp_list[0:]:
    for element in list:
      z.append(element)
  
  dictElements = dict(Counter(z))

  dictElements = { key:value for key, value in dictElements.items() if value== 1}
  for key, value in dictElements.items():

    final=[]
    final.append(key)
    print(final,end="")


def first_day_only_participants(pp_list):

    z=[]
    pb=[]

    for list in pp_list[:1]:


      for element in list:
        z.append(element)
    for list in pp_list[1:]:


      for element in list:
        pb.append(element)    

    for i in range(0,len(z)):
      if z[i] not in pb:
        
        bittu=[]
        bittu.append(z[i])
        print(bittu,end=" ")
        
       
      

pp_list = [
    ['Sam','John', 'Emma', 'Joan', 'Krish',  'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]

print("All the Daily participants:")

print(daily_participants(pp_list))
print('\n')
print("All the One time participants:")
one_time_participants(pp_list)
print('\n')
print("All the First Day participants:")
first_day_only_participants(pp_list)
