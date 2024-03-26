# contains python basic

print("hello python")

# this is  comment in python


#variables
v1 = "Pranita"  #string
v2 = 4          #int
v3 = str(3)     #specifying type , 3 will be string
v4 = 1j         #complex
v5 = [ "a" , "b" , "c"]     #list
v6 =  (1,2,3,4)  #tuple
v7 =   range(6)   #range
v8 =  {'name' : 'shubham' , "sname" : "dalvi"}    #distionary (objects)
v9 =  {"a" , "b" , "c"}    #set
v10 = True #bool

print("print to know a varible ==>" , v4 , "and its type is ===>" , type(v4))

# converting type in python , assiyning tyoe indicates in which type it should be converted

convert = float(1)
convert2 = complex(1)
convert3 = int(2.4)

print("converted type value is ===>" , convert2 )


#assigning  values to multiple varibles at same time
a , b , c = "shubham" , "deepak" , "dalvi" 
print(b)


 #unpacking lo lists 
fruits = ["daar" , "ke" , "aage" , "jeethai"]  
l , m , n , o = fruits
print(l)


# local and global varible
g = "hello im global variable"
def localGlobal():
    g = "even though varible name is same i will be only accessable inside of function , im local varible"
    print(g)

localGlobal()
print(g)


# creating global varible inside of function
def localGlobal2():
    global g2
    g2 = "global var created inside of function"

localGlobal2()  #first need to call this function only than varible will be accesable
print(g2)


# for creating random number there is a module in python  , which is first needed to be imported
import random
r = random
print(r.randrange(1 , 10))


# string methods
stringMethod  = "  on this string ,  we will perform all methods   "
stringM1 = (stringMethod[2:5])   #slice methdod
stringM2 = stringMethod.upper()  #converting to uppercase method , lower()
stringM3 =   stringMethod.strip()  #works as trim
stringM4 =   stringMethod.replace("o" , "O")  #replaces 
stringM5 =   stringMethod.split(",")  #split string into part from given value and returs array 

print("normal string  ===> " , stringMethod)
print("method applied ===>" , stringM5)


# format method , can be used as a placeholder
a = "hello my age is {} "
b = 24
newText = a.format(b)
print("this is format text example ==> ",newText)


# booleans
if 10 > 5 :
    print ("from boolean example  \"greater\" ")
else :
    print( "from boolean example  smaller")


# operators = + , - , * , \ , % , ** , //
# assignment X + = 3
x = 4
x += 3     # x = x + 3
print("assignment operator example ===> " ,x)
#comparison : == , <= , >= , != , > , < 
#logical = and , or , not   (returns bool)

# identity = is , isnot    (returns boolean)
# membership = in , notin  [ kind of incudes for objects  (returns bool) ]


# list methods

list = [1,2,3,4 , "shubham" , "deepak" , "dalvi"]
print("this is list ==>" , list)
print(list[0])   # specic index value
print  (list[2:5])   # prints from including till not including 
print(len(list))

if "shubham" in list :
    print("yes exista")
else :
    print("dosen't exist")

list[4] = "kunal"  # replaces item at index 4
print("after changing specific value" , list)

list.insert(4 , "savita")
print("inserts without replacing ===>" , list)

list.append("parivar") # add value to last  (push)
print("we use append insted of push ===>" , list)

# other function , extends , clear , remove , del , pop  , sort
# iterating through loops

for i in list :
    print(i)
    if i == "parivar" :
        print("yes")
    else :
        print("no")

newList = []
for i in list:
    newList.append(i)

print('new list ==>' , newList)


# dictionaries
dict = {
    "name" : "shubham",
    "age" : 23,
    "occupation" : "it",
    "hoobies" : ["frontend" , "backend" ]

}

print("this is dictionary ====> " , dict)
print("specific value ===> ", dict.get("name") )    #getting specific value
key = dict.keys()
print("getting only keys" , key)                    #getting only keys
value = dict.values()                      
print("getting only values" , value)                #getting only values
if "name" in dict :                                 #check if present
    print("yes its present")

dict["age"] = 22                                     #changing age

print("age changes ====> " , dict)

for i in dict:                 # for i in dict.values()  , dict.keys() , for x , y in dict.items()
    print(i)
    print(dict[i])


nestedDict = {
    "detail1" : {
             "name" : "shubham",
             "age" : 22
    },
    "detail2" : {
         "name" : "kunal",
             "age" : 25
    },
    "detail3" : {
         "name" : "atharva",
             "age" : 21
    }
}

print(nestedDict["detail1"]["name"])
# more methods : add , update , pop , del , clear , copy


# if else 
a = 5
b = 5
if a > b :
    print(" a is greater")
elif a == b:
    print("both are equal")
else :
    print("a is smaller")

# ternary operator
print("A") if a > b else print("==") if a == b else print("B")


# while loop
i = 1
while i < 6:
    print(i)
    i += 1

# for loop
a = "hello"
for i in a :
    print("looping through string ==> ",i)


# function
def funcA(name):
    print("my name is :" , name)

def funcB(*names):
    print("my name is" , names[1])

def listFunc(food):
    for f in food:
        print(f)

funcA("shubham")
funcB("shubham" , "kunal" , "atharva")
listFunc(["mango" , "wmelon", "grapes"])


#lambda function
lam = lambda a : a + 10
print(lam(5))