
# coding: utf-8

# # Calculator - Python

# In[ ]:


print("\n**************************** Calculator Python **************************************") 


# In[19]:


print("\n Select an option - Operator:\n")
print("1 -> Sum")
print("2 -> Sub")
print("3 -> Multiply")
print("4 -> Divison")
print("5 -> Convert Celsius to Fahrenheit")

option = input("\nType your option (1/2/3/4/5):  ")

def addF(x,y): return x+y
if option == '1':
    x = float(input("What is the first number?  "))
    y = float(input("What is the second number?  "))
    print("\n")
    print(x, "+", y, "=", addF(x,y))
    
def subF(x,y): return x-y
if option == '2':
    x = float(input("What is the first number?  "))
    y = float(input("What is the second number?  "))
    print("\n")
    print(x, "-", y, "=", subF(x,y))

def multF(x,y): return x*y
if option == '3':
    x = float(input("What is the first number?  "))
    y = float(input("What is the second number?  "))
    print("\n")
    print(x, "*", y, "=", multF(x,y))

def divF(x,y): return x/y
if option == '4':
    x = float(input("What is the first number?  "))
    y = float(input("What is the second number?  "))
    print("\n")
    print(x, "/", y, "=", divF(x,y))
 
def F(x): return (1.8 * x) + 32
if option == '5':
    print("\n")
    x = float(input("What is the Celsius?  "))
    print("Celsius = ", x, "\nCelsius to Fahrenheit = ", F(x))

if option > '5':
    print('\nYou choose a wrong option!')
    

