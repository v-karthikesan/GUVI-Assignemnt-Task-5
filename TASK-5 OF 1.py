#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1.Python program to calculate total number of vowels and number of each vowel A,E,I,O,U in a given string
str= "Guvi Geeks Network Private Limited"
count_a,count_e,count_i,count_o,count_u=0,0,0,0,0
for x in str:
    if x=='a':
        count_a+=1
    elif x=='e':
        count_e+=1
    elif x=='i':
        count_i+=1
    elif x=='o':
        count_o+=1
    elif x=='u':
        count_u+=1
        
vowelcount=count_a+count_e+count_i+count_o+count_u 
print("Total Number of Vowels count is:", vowelcount)
print("Count of 'A' Vowel is :",count_a)
print("Count of 'E' Vowel is :",count_e)
print("Count of 'I' Vowel is :",count_i)
print("Count of 'O' Vowel is :",count_o)
print("Count of 'U' Vowel is :",count_u)


# In[ ]:




