#!/usr/bin/env python
# coding: utf-8

# In[8]:


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# In[6]:


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range((n+1)-i,0,-1):
        print(i,end=" ")
    print()


# In[9]:


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[11]:


n=int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()


# In[16]:


n=int(input("Enter the number of rows:"))
for i in range(n+1,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print()


# In[30]:


n=int(input("Enter the number of rows:"))
a=1
n1=1
for i in range(n):
    for j in range(n1):
        print(a,end=" ")
        a+=1
    n1+=2
    print()


# In[23]:


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(end="  ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()


# In[26]:


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(n,end=" ")
    print()


# In[37]:

n=int(input("Enter the last digit:"))
a=0
prev=[]
for i in range(1,n+1):
    prev=[]
    for j in range(n,i,-1):
        print(end="  ")
    a=i-1
    for k in range(0,i):
        a+=1
        print(a,end=" ")
        prev.append(a)
    prev=prev[0:len(prev)-1]
    for z in range(0,len(prev)):
        print(prev[-(z+1)],end=" ")
    prev=[]
    print()
    




