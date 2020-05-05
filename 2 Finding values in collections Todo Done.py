#!/usr/bin/env python
# coding: utf-8

# In[101]:


import random
random.seed(1000)
import matplotlib.pyplot as plt
import time
import pandas as pd 
from timeit import default_timer as timer


# # Create Data

# In[82]:


# number of elements in list
n = 250

# list of unsorted items
items = [int(random.random()*n) for _ in range(n)]

# value to be searched in list
value = int(random.random()*n)

# sorted list 
sorted_items = sorted(items)


# # Find Value in Unsorted List with Linear Search
# 
# Animation: https://yongdanielliang.github.io/animation/web/LinearSearchNew.html

# In[83]:


def get_item(items, index):
    """value of of an item in a list based on the index of the value
        args:
            - items: List of items
            - index: index of the requested item
        return:
            - value of the requested item
    """
    if index == -1:
        print("Not in the list")
        return None
    else:
        return items[index] 


# In[84]:


def find_element(items, value):
    

    """Linear search for a value in a list of items
        args:
            - items: unsorted list of items
            - value: searched value
        return:
            - index of value or -1 if not in list
    """
    # TODO
    for i in range(len(items)):
       curr_item = get_item(items,i) 
       if(curr_item == -1):
            return -1
       if(curr_item == value):
           return i
        
    return -1
    pass


# In[95]:


print(value)
index = find_element(items, value)
print(index)


# In[94]:


print(value)
get_item(items, index)


# ### Question: 
# * Time your function with differently sized inputs by
# * searching for each input size for a non-existing element
# * and plot the change of the time to the size of the input
# 
# (see 1 Timing Algorithms)

# In[109]:


list_of_n = [10, 50, 100, 200, 300, 400, 600, 800]
value = -10
measures = []
for n in list_of_n:
    items = [int(random.random()*n) for _ in range(n)]
    time = get_ipython().run_line_magic('timeit', '-o find_element(items, value)')
    measures.append((n, time.average))
plt.plot(*zip(*measures))
plt.ylim(ymin=0)
plt.show()


# ### Question: What is the time complexity of searching for a value in an unsorted list?
# 
# Big O Notation

# TODO: o(n) 

# # Find Value in Sorted list with Binary Search

# Animation: https://yongdanielliang.github.io/animation/web/BinarySearchNew.html

# In[170]:


def find_sorted(items, value):
    """Bineary search for a value in a list of sorted items
        args:
            - items: sorted list of items
            - value: searched value
        return:
            - index of value or -1 if not in list
    """
    # TODO
    low = 0
    highest = len(items) - 1
    #print ('val: ' , value)
    mid = int((low+highest) / 2)
    while low <= highest:
       # if mid >= len(items):
        #    return -1
        #print ('low' , low, mid ,' = ', items[mid] , 'highest' , highest)
        if(items[mid] == value):
            return mid
        elif (low == highest):
            return -1
        elif (items[mid] > value):
            highest = mid - 1
            mid = int((low+highest) / 2)
        elif (items[mid] < value):
            low = mid + 1
            mid = int((low+highest) / 2)
        else  :
            return -1

    
pass
    


# In[171]:


value = sorted_items[6] 
print(sorted_items)
find_sorted(sorted_items, value)


# In[172]:


# a value that is not in the list so that we get the worst case time
value = n+1 
print (items[49])
find_sorted(sorted_items, value)


# In[173]:


n = 100
items = [int(random.random()*n) for _ in range(n)]
value = n+1 
find_sorted(sorted_items, value)


# In[174]:


n = 200
items = [int(random.random()*n) for _ in range(n)]
value = n+1 
find_sorted(sorted_items, value)


# ### Question: 
# * Time your function with differently sized inputs by
# * searching for each input size for a non-existing element
# * and plot the change of the time to the size of the input
# 
# (see 1 Timing Algorithms)

# In[178]:


# TODO
list_of_n = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
value = -1
measures = []
for n in list_of_n:
    value = n+1
    items = [int(random.random()*n) for _ in range(n)]
    items = sorted(items)
    time = get_ipython().run_line_magic('timeit', '-o find_sorted(items, value)')
    measures.append((n, time.average))
plt.plot(*zip(*measures))
plt.ylim(ymin=0)
plt.show()


# ### Question: What is the time complexity of binary search? 
# 
# Big O Notation

# TODO: Your answer o(logn) 
