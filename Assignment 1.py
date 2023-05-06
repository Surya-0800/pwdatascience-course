#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Explain with an example each when to use a for loop and a while loop.

#for loop - Used for loop to print all the sum values of n without any conditon

n = 10
a = 0
for i in range(n):
    a+=i
    print(a)
    
    
#while loop - USed for loop to print sum of n values only till 10.
n =1

while n < 10:
    a +=n
    n=n+1
    print(a)


# In[17]:


# Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop.

#for loop

n = 10
a = 0
for i in range(n+1):
    a+=i
    print(a)
    
    
#while loop
n =1
b=0
while n < 11:
    b +=n
    n=n+1
    print(b)
    
  
#Product

#for loop

n = 10
x = 1
for i in range(1,n+1):
    x = x*i
    print(x)
    
    
#while loop
n =1
y=1
while n < 11:
    y *=n
    n=n+1
    print(y)




# In[18]:





# In[ ]:





# In[25]:


4.5,6,10,20

first = 4.5
second = 6
third = 10
fourth = 20

units = int(input("Enter no of units"))

if units <=100:
    cost = 100*4.5
    print(cost)
elif units <=200:
    cost = 100*4.5
    cost += (units - 100)*6
    print(cost)
elif units <=300:
    cost = 100*4.5+(units - 100)*6+(units-200)*10
    print(cost)
else:
    cost = 100*4.5+(units - 100)*6+(units-200)*10+(units - 300)*20
    print(cost)


# In[29]:


# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list.

lis = []

for i in range(1,101):
    if i%4==0 or i%5==0:
        lis.append(i)
print(lis)

n=1

while n <=100:
    if n%4==0 or n%5==0:
        lis.append(n)
    n+=1
print(lis)    


# In[30]:


# Write a program to filter count vowels in the below-given string.
string = "I want to become a data scientist"


voewls = ["a","e","i","o","u"]
n = 0

string = string.lower()

for i in string:
    if i in voewls:
        n+=1
print(n)        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




