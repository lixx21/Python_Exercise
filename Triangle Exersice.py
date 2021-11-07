#!/usr/bin/env python
# coding: utf-8

# In[1]:



global h
h = input("Height of Triangle = ")
h = int(h)

print("Normal Triangle")
for i in range(h): # range from 0 to h-1
    for j in range(i):
        print("*", end="") # end = "" appends new space instead of new line after *
    print("*")


print(" ")
print("Reverse Normal Triangle")
for i in range(h):
    for j in range(h-i,1,-1): #start_index, Stop_Index, Step_Index. (if h = 3 then the output is 3, 2. stop before 1 cuz stop_index = 1)
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("*")


print(" ")
print("Backward Triangle")
for i in range(h):
    for j in range(h-i,1,-1 ):
        print("*", end="")
    print("*")


print(" ")
print("Reverse Backforward Triangle")
for i in range(h):
    for j in range(i):
        print(" ", end="")
    for j in range(h-i, 1, -1):
        print("*", end="")
    print("*")


print(" ")
print("Christmas Tree")
for i in range(h):
    for j in range(h-i, 1, -1):
        print(" ", end="")
    for j in range (i+1):
        print("* ", end="")
    print(" ")


print(" ")
print("Backward Christmas Tree")
for i in range (h):
    for j in range(i):
        print(" ", end="")
    for j in range(h-i,1,-1):
        print("* ",end="")

    print("*")


# In[ ]:




