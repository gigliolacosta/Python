
# coding: utf-8

# # Calculator - Python

# In[ ]:


print("\n**************************** Calculator Python **************************************") 


# In[6]:


print("\n Select an option - Operator:\n")
print("1 -> Sum")
print("2 -> Sub")
print("3 -> Multiply")
print("4 -> Divison")

option = input("\nType your option (1/2/3/4):  ")

x = int(input("What is the first number?  "))
y = int(input("What is the second number?  "))

def addF(x,y): return x+y
if option == '1':
    print("\n")
    print(x, "+", y, "=", addF(x,y))
    
def subF(x,y): return x-y
if option == '2':
    print("\n")
    print(x, "-", y, "=", subF(x,y))

def multF(x,y): return x*y
if option == '3':
    print("\n")
    print(x, "*", y, "=", multF(x,y))

def divF(x,y): return x/y
if option == '4':
    print("\n")
    print(x, "/", y, "=", divF(x,y))

if option > '4':
    print('\nYou choose a wrong option!')

