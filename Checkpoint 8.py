#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
f = open("python.txt")
f.read()


# In[2]:


#2
f = open("python.txt")
f.readline()


# In[3]:


#3
f = open("python.txt")
f.readlines()[-1]


# In[4]:


#4
count = 0
text = input("Enter the file name 'exemple.txt'")
f = open(text, "r")
for line in f:  
    #Splits each line into words  
    words = line.split(" ");  
    #Counts each word  
    count = count + len(words);  
   
print("Number of words present in given file: " + str(count))


# In[5]:


#5
f = open("python.txt")
f.readlines()[-1]


# In[ ]:




