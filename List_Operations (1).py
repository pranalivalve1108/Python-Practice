#!/usr/bin/env python
# coding: utf-8

# # Creating List

# In[7]:


num=[1,2,3,4]  #Numbers print
print(num)


# In[3]:


letter=['a','b','c','d']  #Letters print
print(letter)


# In[4]:


char=["Hii","Pranali","How","are","u"]  #Characters print
print(char)


# In[5]:


mix=[1,'a',"Hii",2,'b',"Pranali"]   #Combine (Numbers,Letters,Characters) print
print(mix)


# In[6]:


matrix=[[1,2],['a','b'],["Hii","Pranali"]]   #Nested List print
print(matrix)


# In[50]:


list=[]
print(list)


# # Accessing List Elements

# In[9]:


print(mix)


# In[10]:


mix[2] #Print 2nd location value


# In[12]:


mix[-2] #Print 2nd location value from the end


# In[13]:


mix[:2] #Print value from first index to that particular index(2) and not print 2nd location value


# In[15]:


mix[3:] #Print value from that particular index(3) to end of the list and print 3rd location value also


# In[17]:


mix[2:5] #Print value from 1st particular index(2) to 2nd particular index(5) & print only 1st index value not 2nd 


# In[18]:


mix[::2] #Skip 1 value and then print


# In[19]:


mix[::3] #Skip 2 values and then print


# In[23]:


mix[1::2] #Skip elements till first particular index and then skip 1 value and then print


# In[24]:


mix[2::3] #Skip elements till first particular index and then skip 2 values and then print


# In[25]:


mix[::-1] #Print list in reverse order


# # Operations on List

# In[27]:


#Print "0" 100 times without using any loop
z=[0]*100
print(z)


# In[30]:


#Concatenate 2 Lists
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=l1+l2
print(l3)


# In[29]:


#Print 1 by 1 letter in ' ' code
var=list("Pranali")
print(var)


# In[31]:


print(l1)


# In[32]:


#Print 1 in diff. list and others element in diff. list
one, *other=l1
print(one)
print(other)


# In[33]:


#Print 1 & 2 in diff. list and others element in diff. list
one, two, *other=l1
print(one)
print(two)
print(other)


# # Methods in List

# In[35]:


#1. append()= Add elements at end of the list
l1.append(6)
print(l1)


# In[36]:


l1.append(7)
print(l1)


# In[37]:


#2. extend()= Add another list at end of the list
l1.extend(l2)
print(l1)


# In[38]:


#3. insert()= Add element to particular index that u define
l1.insert(1,10) #Add first location to 10
print(l1)


# In[39]:


#4. remove()= Remove element that u define
l1.remove(5)
print(l1)


# In[41]:


l1.remove(6)
print(l1)


# In[42]:


#5. sort()= Sort elements in ascending order
a=[5,4,3,7,1,2]
a.sort()
print(a)


# In[43]:


b=['e','d','c','b','a']
b.sort()
print(b)


# # Built-in functions in list

# In[44]:


#1. len()= Define length of list
x=[9,17,14,4,90,55]
len(x)


# In[45]:


#2. min()= Define Minimum value
min(x)


# In[46]:


#3. max()= Define Maximum value
max(x)


# In[47]:


#4. sum()= Summation/Addition of all numbers in list
sum(x)


# In[48]:


#5 Calculate average
sum(x)/len(x)


# In[1]:


l=[1,2,3]
print(l)


# In[2]:


print(l[1])


# In[3]:


a=[0]*100
print(a)


# In[5]:


print(0*100)


# In[6]:


one,*other=l
print(one,other)


# In[7]:


l.append(4)


# In[8]:


l


# In[9]:


l1=[5,6,7,8]
l.extend(l1)


# In[10]:


l


# In[11]:


t=(1,2,3)
print(type(t))


# In[12]:


l=list(t)


# In[13]:


l


# In[14]:


print(type(l))


# In[15]:


l.append(4)
print(l)


# In[16]:


t=tuple(l)


# In[17]:


t


# In[18]:


print(type(t))


# In[19]:


d={1:'a',2:'b',3:'c'}
d


# In[20]:


d.values()


# In[21]:


keys={1,2,3,4,5}
value=6
dict.fromkeys(keys,value)


# In[22]:


s=set([1,2,3,4])
print(type(s))


# In[23]:


s={1,2,3,4}
print(type(s))


# In[24]:


s.add(5)


# In[25]:


s


# In[26]:


s.add('a')
s


# In[28]:


s1={1,2,3,4,5}
s2={3,4,5,6,7}
s1.union(s2)


# In[29]:


s1.difference(s2)


# In[30]:


s1.intersection(s2)


# In[32]:


from array import *
arr=array('i',[1,2,3,4,5])
print(arr)


# In[33]:


print(arr.buffer_info())


# In[34]:


for a in arr:
    print(a)


# In[35]:


for a in arr:
    print(a,end=" ")


# In[37]:


for pnt in range(5):
    print(pnt,arr[pnt])


# In[39]:


print(arr.reverse())


# In[40]:


arr


# In[41]:


def a(*b):
    print(b)
a(1,2,3,4)


# In[42]:


import pandas as pd


# In[43]:


print(pd.__version__)


# In[44]:


s=[1,2,3,4,5]
print(pd.Series(s))


# In[45]:


order=['A','B','C','D','E']
print(pd.Series(s,index=order))


# In[46]:


import numpy as np
n=np.random.randn(5)
order=['A','B','C','D','E']
print(pd.Series(n,index=order))


# In[47]:


d=[10,20,30,40,50]
print(pd.DataFrame(d))


# In[55]:


d=[10,20,30,40,50]
df=pd.DataFrame(d,index=order,columns=['A'])
df


# In[57]:


df.head(3)


# In[58]:


df.tail(3)


# In[59]:


df.index


# In[60]:


df.columns


# In[62]:


df.columns


# In[63]:


df.isnull()


# In[64]:


df.loc['A','A']=100


# In[65]:


df


# In[66]:


df.describe()


# In[67]:


df.sum()


# In[68]:


df.min()


# In[69]:


df.max()


# In[ ]:




