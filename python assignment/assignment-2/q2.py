# 2. get the occurence of all vowels and consonent from the large given string.


str1 = input ("Enter Strpng : ")
vowels = 0
consonants = 0

for p in str1:
    if(p == 'a' or p == 'e' or p == 'p' or p == 'o' or p == 'u'
       or p == 'A' or p == 'E' or p == 'p' or p == 'O' or p == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Vowels =", vowels)
print("Consonants =", consonants)


