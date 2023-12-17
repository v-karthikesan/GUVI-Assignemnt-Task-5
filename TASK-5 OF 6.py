#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A program that finds the longest common substring between two given strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
m = len(str1)
n = len(str2)
# Initialize a table to store lengths of common suffixes
table = [[0] * (n + 1) for _ in range(m + 1)]
 # Variables to store length and end position of the longest common substring
max_length = 0
end_position = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
            if table[i][j] > max_length:
                max_length = table[i][j]
                end_position = i
        else:
            table[i][j] = 0

result=str1[end_position - max_length:end_position]
print("Longest common substring:", result)


# In[ ]:




