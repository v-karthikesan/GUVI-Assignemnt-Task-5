#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A program that finds the most frequent characters and frequency from a given string
input_str = input("Enter a string: ")
input_str = input_str.replace(" ", "").lower()# To Remove spaces & convert to lowercase for case-insensitive comparison
char_frequency = {} # To Create a dictionary to store character frequencies
for char in input_str:
    if char.isalpha():  # consider only alphabetic characters
        char_frequency[char] = char_frequency.get(char, 0) + 1

# Find the character(s) with the maximum frequency
max_frequency = max(char_frequency.values())
most_frequent_chars = [char for char, freq in char_frequency.items() if freq == max_frequency]

print("Most frequent character(s):", most_frequent_chars)
print("Frequency:", max_frequency)

