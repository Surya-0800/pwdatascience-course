#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Create one variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple


a = "Surya"
b = [1,2,3,4]
c = 23.4
d = ("Surya","reddy")


# In[ ]:


# Q2. Given are some following variables containing data:
# (i) var1 = ‘ ‘
# (ii) var2 = ‘[ DS , ML , Python]’
# (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# (iv) var4 = 1.


1 = string
2 = string
3 = List
4 = int


# In[ ]:





# In[ ]:


Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **


1 - / is a division operator example

10/2 - output will be 5

2 - Is a reminder operator example
10%2 = 0

3 // - is a integer division it gives out only in integers even if quotient is float it will convert to nearest int value

4 ** is used for sending a number as power 


# In[3]:


# Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

my_list = [10, "Hello", 3.14, True, None, [1, 2, 3], {"name": "John", "age": 30}, (4, 5, 6), {1, 2, 3}, bytearray(b'hello')]

for i in my_list:
    print(i,type(i))


# In[5]:


A = 50
B = 5   

count = 0  

while A % B == 0:
    A = A / B
    count += 1 

if count > 0:
    print(f"divisible by {B} {count} times")
else:
    print(f"not divisible by {B}")


# In[6]:



numbers = [2, 5, 6, 7, 9, 10, 12, 15, 18, 20, 21, 22, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]
for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")


# In[ ]:


Lists: Lists.Dictionary are mutable data types in Python. The elements in a list can be changed after the list is created.
For example:
    
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"
print(fruits)

Strings,tuple are immutable data types in Python. Once a it is created, its value cannot be changed.
For example:
numbers = (1, 2, 3)
numbers[0] = 4  # Output: TypeError: 'tuple' object does not support item assignment

