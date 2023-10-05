#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello Shahu")


# In[2]:


str = "Shahu!!!!"
print(str)


# In[3]:


print(str)


# In[1]:


print(str)


# In[2]:


print(str)


# In[5]:


name = input("Enter your name:")
print("hi",name)


# In[6]:


print("Hope you are good")

this is a title
# this is a title

# this is a title
# #this is a title

# this is a title
# #this is a bigger title

# In[7]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,2,3,4])
plt.show()


# # Welcome to my simple Graph

# In[8]:


plt.plot([1,2,3,4], [1,2,3,4])
plt.show()


# In[1]:


x=10


# In[2]:


type(x)


# In[3]:


print(x)


# In[5]:


x=10*10
print(x)


# In[6]:


x=10*10
type(x)


# In[7]:


y=10.20
type(y)


# In[8]:


print(y)


# In[9]:


z="Hello Shahu"
type(z)


# In[10]:


print(z)


# # List

# In[11]:


x=[1,2,3]
print(x)


# In[12]:


type(x)


# In[13]:


print(x[2])


# In[14]:


x[1]=0
print(x)


# # Tuple

# In[15]:


t=("A","B","c")
print(t)


# In[16]:


type(t)


# In[17]:


print(t[0])


# In[19]:


t[2]="D"
print(t)


# In[20]:


t[2]="D"
print(t)


# In[21]:


(x,y,z)=10,20,30
print(x)
print(y)
print(z)


# In[22]:


x=y=z=1
print(x,y,z)


# # Conversions
# 

# In[1]:


a="192"
type(a)


# In[2]:


int(a)


# In[3]:


a=int(a)
type(a)


# In[4]:


a=float(a)
type(a)


# In[5]:


print(a)


# In[6]:


a=complex(a)
type(a)


# In[7]:


print(a)


# In[8]:


print(complex(2,6))


# In[9]:


x=-7.5
print(abs(x))


# In[10]:


x=7.5
print(abs(x))


# In[11]:


import math
x=10
print(math.exp(x))


# In[12]:


math.e


# In[13]:


print(math.sqrt(2))


# In[14]:


print(math.sqrt(4))


# In[15]:


min(1,567,90,34456,378)


# In[16]:


max(1,567,90,34456,378)


# # Creating List

# In[17]:


num= [1,2,3,4,5]
print(num)


# In[18]:


letters = ['a','b','c','d','e']
print(letters)


# In[19]:


strg = ["Hello","Shahu","How","are","you"]
print(strg)


# In[20]:


mixtype = [1,2,'a','b',"Hello","Shahu"]
print(mixtype)


# In[21]:


mat=[[1,2,3],['a','b','c']]
print(mat)


# # Accessing elements in list

# In[22]:


print(mixtype)


# In[23]:


mixtype[4]


# In[24]:


mixtype[-2]


# In[25]:


mixtype[:3]


# In[26]:


mixtype[3:]


# In[27]:


mixtype[1:4]


# In[28]:


mixtype[::3]


# In[29]:


mixtype[::5]


# In[30]:


mixtype[::-1]


# # Operations perform on list

# In[31]:


x=["Shahu"]*10
print(x)


# In[32]:


x=["Shahu"]*100
print(x)


# In[33]:


print(letters)


# In[34]:


print(strg)


# In[35]:


print(letters+strg)


# In[36]:


var=list("Hello Shahu")
print(var)


# In[37]:


print(num)


# In[38]:


one, *other=num
print(one)
print(other)


# In[40]:


two, *other=num
print(two)
print(other)


# In[41]:


two, *other=num
print(two)
print(other)


# # Methods in list

# In[47]:


print(num)


# In[48]:


print(num)


# In[49]:


num.append(7)


# In[50]:


print(num)


# In[51]:


num.extend(letters)
print(num)


# In[52]:


num.insert(2,"Shahu")
print(num)


# In[53]:


num.remove("Shahu")
print(num)


# In[54]:


num.remove(6)
print(num)


# In[55]:


var1=[3,2,1]
var1.sort()
print(var1)


# # Built in Functions in list

# In[56]:


x = [10,30,50,20,40]
print(x)


# In[57]:


len(x)


# In[58]:


min(x)


# In[59]:


max(x)


# In[60]:


sum(x)


# In[61]:


sum(x)/len(x)


# # Creating tuple

# In[62]:


t=()
type(t)


# In[63]:


t=()
print(type(t))


# In[64]:


print(t)


# In[65]:


city="Nashik",


# In[66]:


print(city)


# In[67]:


print(type(city))


# In[68]:


num=(1,2,3,4)
print(num)


# In[69]:


a,b,c,d=num
print(a,b,c,d)


# # Built in functions in tuple

# In[70]:


t=(1,2,1,2,1,2,3,2,6,8)
print(t)


# In[71]:


t.count(2)


# In[72]:


sum(t)


# # Converting list into tuple

# In[73]:


lst=[1,2,3,4]
print(type(lst))


# In[74]:


tpl=tuple(lst)
print(tpl)


# In[75]:


type(tpl)


# # Nested tuples in list

# In[1]:


lst = [(1,2,3),('a','b','c')]
print(lst)


# In[2]:


lst.append(("Hello","Shahu"))
print(lst)


# # Nesting list within tuples

# In[3]:


tpl = (['a','b','c'],['d','e','f'])
print(tpl)


# In[4]:


tpl[0].append('z')
print(tpl)


# In[5]:


tpl[0].remove('z')
print(tpl)


# # Strings

# In[6]:


str = "Welcome"
print(str)


# In[7]:


print(str[0:3])


# In[8]:


print(str[:5])


# In[9]:


print(str[5:])


# In[10]:


print(str[1:6])


# # Inbuilt methods

# In[11]:


str1 = "Welcome to World"
print(str1)


# In[12]:


print(str1.upper())


# In[13]:


print(str1.lower())


# In[14]:


print(str1.find("W"))


# In[15]:


print(str1.index("W"))


# In[19]:


print(str1.split(" "))


# In[20]:


print(str1.replace("World","Shahu"))


# In[21]:


print(str1.rpartition(" to "))


# In[23]:


str2 = "hey"
str3 = "there"
str4 = "how"
str5 = "r u"
stg = "{}! {}, {} {}?".format(str2,str3,str4,str5)
print(stg)


# # Creating Dictionaries

# In[6]:


d = {}
print(d)
print(type(d))


# In[7]:


d1 = {1:"hii",2:"Shahu"}
print(d1)


# # Adding elements

# In[8]:


d2={}
d2[0]="Hello"
print(d2)


# In[9]:


d2[1]="Shahu"
print(d2)


# In[10]:


d1[1]


# # Built in Functions

# In[11]:


d1.values()


# In[12]:


keys={'a','b','c','d'}
value=1
dict.fromkeys(keys,value)


# # Sets

# In[17]:


s=set([1,2,3,4])
print(s)
type(s)


# In[18]:


s.add(5)


# In[19]:


print(s)


# In[20]:


fs=frozenset([1,2,3,4])
print(fs)


# In[21]:


fs.add(5)


# In[22]:


s1=set([1,3,7,2])
s2=set([3,2,8,9])


# In[23]:


s1.union(s2)


# In[24]:


s1.difference(s2)


# # Simple If Loop

# In[25]:


a=20
if a>10 :
    print("This is the inside of If loop")
print("This is the outside of If loop")


# In[26]:


a=20
if a<10 :
    print("This is the inside of If loop")
print("This is the outside of If loop")


# # If-Else Loop

# In[ ]:


b=10
if b<5 :
    print("True")
else :
    print("False")


# In[ ]:


b=10
if b>5 :
    print("True")
else :
    print("False")
    


# In[ ]:


var="z"
if var=='a' :
    print("This is a vowel a")
elif var=='e' :
    print("This is a vowel e")
elif var=='i' :
    print("This is a vowel i")
if var=='o' :
    print("This is a vowel o")
elif var=='u' :
    print("This is a vowel u")
else :
    print("This is a Consonant")


# # While loop

# In[1]:


a=5
while (a<10):
    print("Hello Shahu")
    a=a+1


# # For loop

# In[7]:


x=[1,2,3,"Shahu"]
for i in x :
    print(i,end=" ")


# In[8]:


x="Shahu"
for i in x :
    print(i,end=" ")


# In[ ]:


for i in range(20):
    print(i)


# In[ ]:


for i in range(0,20,2):
    print(i)


# In[ ]:


sum=0
for i in range(0,21):
    if i%2==0 :
        sum=sum+i
print(sum)


# In[ ]:


n=int(input("Enter a number:"))
for i in range(1,n+1) :
    for j in range(1,i+1) :
        print(j,end=" ")
    print()


# In[ ]:





# In[ ]:





# # Break Statement

# In[11]:


a="Hey there! How are u"
for i in a :
    if i== "!" :
        break
    print(i,end="")


# In[10]:


a="Hey there! How are u"
for i in a :
    if i== " " :
        break
    print(i,end=" ")


# # Continue Statement

# In[ ]:


for i in range(9) :
    if i==3 :
        continue
    print(i)


# # Array

# In[ ]:


from array import *


# In[ ]:


arr=array('i',[1,2,3,4])
print(arr)


# In[ ]:


print(arr.buffer_info())


# In[ ]:


print(arr[2])


# In[ ]:


for i in arr:
    print(i)


# In[ ]:


for pnt in range(4):
    print(pnt,arr[pnt])


# In[ ]:


arr.reverse()
print(arr)


# In[ ]:


arr.append(10)
print(arr)


# In[ ]:


arr.remove(2)
print(arr)


# # Functions

# In[1]:


def my_fun() :
    print("Hello World")
my_fun()


# In[3]:


def add(x,y):
    c=x+y
    print("Addition is:",c)
add(10,20)


# # Threading

# In[2]:


from threading import *
def show() :
    print("This is a Child thread")
t=Thread(target=show())
t.start()
print("This is a parent thread")


# In[5]:


class MyThread(Thread) :
    def run(self):
        for i in range(5):
            print("\nThis is a child class")
t=MyThread()
t.start()
for i in range(5):
    print("\nThis is the main thread")


# In[7]:


class demo :
    def show(self):
        for i in range(5):
            print("\nThis is the child thread")
obj=demo()
t=Thread(target=obj.show())
obj.show()
for i in range(5):
    print("\nThis is the parent thread")


# # Python Scripting

# In[1]:


import os
def current_directory():
    cwd=os.getcwd()
    print(cwd)
current_directory()


# In[2]:


def file_path(filename):
    path=os.path.abspath((filename))
    print(path)
filename="sample.txt"
file_path(filename)


# In[3]:


import time
a=time.time()
print(a)


# In[4]:


localtime=time.localtime(a)
print(localtime)


# In[5]:


print(localtime.tm_year)


# In[6]:


print(localtime.tm_hour)


# In[7]:


print(time.ctime(a))


# # SMTP

# In[23]:


import smtplib
smtp_obj=smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('pranalivalve2001@gmail.com','Pr@n@li12345')
smtp_obj.sendmail("pranalivalve112001@gmail.com",'Subject:SMTP check \n This is a test email')
smtp_obj.quit()


# In[22]:


from os import path

def createFile(dest):
    if not(path.isFile(dest)):
        f=open(dest,'w')
        f.write("Welcome to Python Scripting")
        f.close()
dest=r"C:\Users\DELL\Practice_Programs\sample.txt"
createFile(dest)
print("File created")


# In[ ]:





# In[25]:


import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")


# In[26]:


def func1(*args):
    for i in args:
        print(i)
func1(10,20,30,40,50)


# In[28]:


def func1(*args,**kwargs):
    for i in kwargs.items:
        print(i)
func1(a=10,b=20,c=30)


# In[1]:


def func1():
    x=10
    def func2(x):
        return x+1
    return func2(x)

result=func1()
print(result)


# In[2]:


def func1(called_func):
    print("This is the first function")
    def nested_function(called_func):
        print("This is the nested function")
        called_func()
    return nested_function(called_func)
def outer_function():
    print("This is the outer function")
    
obj=func1(outer_function)


# In[3]:


B=type("Baseclass",(object,),{})
c1=type("c1",(B,),{'val':5})
c2=type("c2",(B,),{'val':10})

def ClassCreator(bool):
    if bool:
        return c1()
    else:
        return c2()
print(ClassCreator(True).val)
print(ClassCreator(False).val)


# In[1]:


import numpy as np
a=np.array([1,2,3])
print(type(a))


# In[2]:


print(a.shape)


# In[5]:


b=np.arange(12)
b


# In[6]:


b.reshape(3,4)


# In[7]:


from scipy import constants
print(constants.h)


# In[8]:


print(constants.c)


# In[9]:


print(constants.N_A)


# In[10]:


import pandas as pd
df=pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'))
df


# In[12]:


df.describe()


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


np.random.seed(10)


# In[15]:


N=30
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)


# In[22]:


area=(30*np.random.rand(N))**2


# In[23]:


plt.scatter(x,y,s=area,c=colors,alpha=0.4)
plt.show()


# In[24]:


from matplotlib import style
style.use('ggplot')

x=[2,4,6]
y=[12,14,16]

x2=[3,3,4]
y2=[7,14,5]


# In[25]:


plt.bar(x,y,color='r',align='center')
plt.bar(x2,y2,color='b',align='center')

plt.title('Info')
plt.ylabel('Y Axis')
plt.xlabel('x Axis')
plt.show()


# # Numpy Library

# In[26]:


import numpy as np


# In[28]:


a=np.array([1,2,3])
a


# In[29]:


a=np.array([1,2,3])
print(a)


# In[30]:


a[0]


# In[4]:


import numpy as np
import time
import sys


# In[2]:


b=range(1000)
print(sys.getsizeof(5)* len(b))


# In[5]:


c=np.arange(1000)
print(c.size*c.itemsize)


# In[6]:


size=100000


# In[7]:


L1=range(size)
L2=range(size)
A1=np.arange(size)
A2=np.arange(size)


# In[8]:


start=time.time()
result=[(x+y) for x,y in zip(L1,L2)]
result=[(x+y) for x,y in zip(L1,L2)]
print(result)
print("Python list took:",(time.time()-start)*1000)


# In[9]:


start=time.time()
result=A1+A2
print("Numpy Array took:",(time.time()-start)*1000)


# In[11]:


a=np.array([[1,2],[3,4],[5,6]])
a


# In[12]:


a.ndim


# In[13]:


a.itemsize


# In[14]:


a.shape


# In[15]:


a=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
a


# In[16]:


a.itemsize


# In[17]:


a=np.array([[1,2],[3,4],[5,6]],dtype=np.complex)
a


# In[19]:


np.zeros((3,4))


# In[20]:


np.ones((3,4))


# In[21]:


l=range(5)
l


# In[22]:


np.arange(5)


# In[24]:


print(np.char.add(['Hello:','Hii:'],['abc','xyz']))


# In[26]:


print(np.char.multiply('Shahu ',5))


# In[27]:


print(np.char.center('Hello',20,fillchar="-"))


# In[31]:


print(np.char.capitalize('hello world'))


# In[30]:


print(np.char.title('how are u doing'))


# In[32]:


print(np.char.lower(['HELLO','WORLD']))


# In[34]:


print(np.char.lower('HELLO'))


# In[35]:


print(np.char.upper(['hello','world']))


# In[36]:


print(np.char.upper('hello'))


# In[37]:


print(np.char.split('are u coming to the party'))


# In[38]:


print(np.char.splitlines('Hello\n how are u'))


# In[39]:


print(np.char.strip(['Shahu','Shambhu','Om'],'a'))


# In[41]:


print(np.char.join([':','-'],['dmy','ymd']))


# In[43]:


print(np.char.replace('She is a good dancer','is','was'))


# # Pandas Library

# In[1]:


import pandas as pd


# In[2]:


print(pd.__version__)


# # Series create, Manipulate, Query, Delete

# In[6]:


arr=["Shahu","Om",3,"Shambhu",5]
s1=pd.Series(arr)
s1


# In[7]:


order=[1,2,3,4,5]
s2=pd.Series(arr,index=order)
s2


# In[8]:


import numpy as np
n=np.random.randn(5)
index=['a','b','c','d','e']
s2=pd.Series(n,index=index)
s2


# In[10]:


d={'a':1,'b':2,'c':3,'d':4,'e':5}
s3=pd.Series(d)
s3


# In[11]:


s1[:3]


# In[12]:


s1[-2:]


# In[13]:


s1[:]


# In[14]:


s4=s1.append(s3)
s4


# In[ ]:





# In[ ]:




