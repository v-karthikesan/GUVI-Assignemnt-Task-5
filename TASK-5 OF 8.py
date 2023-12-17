#!/usr/bin/env python
# coding: utf-8

# In[16]:


# A program to find two given strings are anagram or not 
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
# Remove spaces and convert to lowercase for case-insensitive comparison
cleaned_str1 = ''.join(str1.split()).lower()
cleaned_str2 = ''.join(str2.split()).lower()
# Check if the sorted characters of both strings are the same
if (sorted(cleaned_str1) == sorted(cleaned_str2)):
    print("Are the strings anagrams? True")
else:
    print("Are the strings anagrams? False")



# In[ ]:




