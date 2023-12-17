#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 2. Pyramid of numbers from 1 to 20 using for loop
num = 20
# Loop for each level
for i in range(1, num + 1):
    # Print leading spaces for each level
    for j in range(num - i):
        print(" ", end=" ")

    # Print numbers in ascending order
    for k in range(1, i + 1):
        print(k, end=" ")

    # Print numbers in descending order
    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    # Move to the next line for the next level
    print()


# In[ ]:




