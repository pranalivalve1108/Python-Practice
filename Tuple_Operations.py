#!/usr/bin/env python
# coding: utf-8

# # Creating Tuple

# In[1]:


t=()  #Empty tuple print
print(t)


# In[2]:


print(type (t)) #print class


# In[5]:


city="Pune", #print class and "," is important
print(type(city))


# # Concatenation

# In[6]:


t1=1,2,3,4,
t2='a','b','c','d',
print(t1+t2)


# In[7]:


print(type (t1))


# In[8]:


print(type (t2))


# # Nesting

# In[9]:


nest=t1,t2
print(nest)


# # Repetition

# In[11]:


rep=("Python ")*5
rep


# In[13]:


rep=("Python ")
print(rep*10)


# In[14]:


print("I'm Pranali")


# In[15]:


print('I\'m Pranali')


# # Slicing in tuple

# In[16]:


print(t1)


# In[17]:


t1[1:] #Print 1st index to end


# In[18]:


t1[::-1] #Print reverse order


# # Unpacking

# In[19]:


print(t1)


# In[21]:


a,b,c,d=t1
print(a,b,c,d)


# In[22]:


a,*b,c=t1
print(a,b,c)


# # Delete tuple

# In[23]:


del t1


# In[24]:


print(t1)


# # Built-in Functions in tuple

# In[25]:


t1=(3,5,2,2,2,2,6,5,8)
print(t1)


# In[26]:


#1. count()= count repeated element
t1.count(2)


# In[27]:


#2. sum()= Addition of whole tuple
sum(t1)


# In[28]:


#3. len()= Define length
len(t1)


# In[29]:


#4. min()= Find minimum value
min(t1)


# In[30]:


#5. max()= Find maximum value
max(t1)


# # Converting list to tuple   *Do not convert tuple to list

# In[31]:


l1=[1,2,3,4]
t1=tuple(l1)
print(type(t1))


# # Nesting list within tuples

# In[32]:


t1=(['a','b','c'],['d','e','f'])
print(t1)


# In[33]:


#Append in list within tuple
t1[0].append('z')
print(t1)


# In[34]:


t1[0].remove('z')
print(t1)


# In[36]:


a=10
def A():
    print(a)
A()


# In[2]:


from collections import Counter
t=(1,2,3,1,2,3,1,2,3)
print(Counter(t))


# In[4]:


import operator as op
d=op.countOf(t,1)
d


# In[5]:


import pandas as pd
t=(1,2,3,1,2,3,1,2,3)
count=pd.Series(t).value_counts()
print(count)


# In[ ]:




