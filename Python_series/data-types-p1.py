# data types in python
# numeric- integer, float , complex number
# sequence- string , list , tuple
# Dictionary
# Set
# mutable  data types  can change its state or contents and immutable objects cannot.
# mutable  data types: list, Dictionary, byte array
# immutable data types: int, float, complex,sting, tuple, set

a=5 
print(a,"is a type",type(a))
#5 is of type <class 'int'>

a=2.0
print(a,"is a type",type(a))
#2.0 is of type <class 'float'>

a=1+2j
print(a,"is a type",type(a))
#1+2j is of type <class 'complex'>

a="Rajan Raj"
print(a,"is a type",type(a))
#Rajan Raj is of type <class 'string'>

a='''
    Hello
     I, Rajan Raj 
     pursuing Btech in CSE in GGV Bilaspur
     My interest is DSA, and web dev .

  '''
print(a,"is a type",type(a))
a ='10'
print(a,type(a))

#list -> is an ordered sequence of items and is flexible means able to change data inside it.
l = [2,2.2,'Rajan']
print(l,type(l))
l[1]=9.2
print(l,type(l))

# tuple
# no difference between list and tuple except  you can not change value 
# in tuple it is immutable and initilized as (,,) it is also ordered sequence of items.
