"""unpack a collection"""
fruits_list = ["oragnge", "banana", "grapes", "mango"]
a,b,c,d = fruits_list
print(a)


"""Global Variable and Local Variables"""
"""Variables Created Outside of Function Called Global Variables and can be
   used any where inside or outside of function,
   but The Variables Created inside function Called Local Variables
   and we can access them inside function
"""
"""Global Var"""
global_var = "awesome"

def globalFun():
    print("Python is " + global_var)
globalFun()

"""Global Var & Local Var/how to accessable inside & outside from function"""
global_var2 = "great !!!" # Global Var, since it is not inside function, can be 
                       # reach from any where

def localFun():
 local_var2 = "nice"  #Local variable
 print("Python is " + local_var2)
localFun()

print("Python is " + global_var2 )


"""USE Global KEYWORD"""
"""
Normally when declare a variable inside function, it is called Local Variable
and can be access only from inside that function, BUT if we use keyword 'global' 
we can use that vaiable GLOBALLY
"""
def globalKeyword():
   global user
   user = "UserName"

globalKeyword()

print("Please Mention " + user)

""" ************Data Types In Python************ """
"""
Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

None Type:	NoneType

"""
"""
**** Example	Data Type
x = "Hello World"	  (DATA TYPE: str)	
x = 20               (DATA TYPE:int)	
x = 20.5            (DATA TYPE:	float	)
x = 1j             (DATA TYPE:	complex)	
x = ["apple", "banana", "cherry"]	 (DATA TYPE:list)	
x = ("apple", "banana", "cherry")   (DATA TYPE:	tuple	)
x = range(6)	   (DATA TYPE:range)	
x = {"name" : "John", "age" : 36}    (DATA TYPE:	dict)	
x = {"apple", "banana", "cherry"}	  (DATA TYPE:set	)
x = frozenset({"apple", "banana", "cherry"})	 (DATA TYPE:frozenset)	
x = True	   (DATA TYPE:bool)
x = b"Hello"	  (DATA TYPE:bytes)	
x = bytearray(5)	(DATA TYPE:bytearray	)
x = memoryview(bytes(5))	(DATA TYPE:memoryview)	
x = None	  (DATA TYPE:NoneType)
    *****************************************
"""
# There are 3 Types of Numbers in Python:
# 1. int 2.float 3.Complex

# 1. int:
"""
Int, or integer, is a whole number, positive or negative, without decimals, 
of unlimited length.
"""
n1 = 34
print(type(n1))  # int example: a = -32 , b = 00765 , c = 0

"""
Float can also be scientific numbers with 
an "e" to indicate the power of 10.
"""
# 2. float :
n2 = 2.3
b1 = -879.3e10
print(type(n2))  # float , example: a= 35e2 , b = 32.2e4 , c = 12E4

# 3. complex :

"""
Complex numbers are written with a "j" as the imaginary part:
"""
n3 = 3j
print(type(n3)) # complex example:a = 2.6j , b= -67j


# TYPE CONVERGION:
"""
we can convert one type of numbers into other type with int() , float() ,
complax()  methods . 
"""
s = 7 # int
print(float(s)) # 7.0

w = 6.72 # float
print(int(w))  # 6
print(complex(w)) # 6.72+0j

k = 8j
# print(int(k)) # error idk why ?????
# Note: You cannot convert complex numbers into another number type.

"""
Random Number
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:

Example
Import the random module, and display a random number between 1 and 9:
"""
import random
print(random.randrange(1,10))

# =========================================================== 
frozset = ({"pawan","deep","naugain"})
print(frozset)

y = ({"tree","plants","flowers","seeds"})
print(y)






   


