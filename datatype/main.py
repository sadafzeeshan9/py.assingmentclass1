# Data Type 
 
# there are many type of data type of python some are there

# 1.integer (int)  : Integer ek aisa number hota hai jo poora hota hai, bina kisi decimal ya fraction ke.
#  Yeh positive, negative, ya zero ho sakta hai.


num:int = 1235
print(num)
print(type(num))
      

# 2.Floating (float) :  Floating Point Number (Float) ek decimal wala number hota hai. Yeh poora nahi hota, 
# balki isme point (.) ke baad bhi digits hoti hain.


num:float  = 12.35
print(num)
print(type(num))
      

# 3.String(str) : String ek text ya characters ka collection hota hai. Yeh quotation marks (" ") ya (' ') ke andar likha jata hai.
# Strings numbers bhi contain kar sakti hain, lekin agar wo quotes ke andar ho to wo integer ya float nahi hoga.

name:str ="sadaf zeeshan patel"
print(name)


# 4.boolean   (bool) :    Sirf True ya False values ke liye use hoti h .true false me t,f hamesha capital use hote hen .


is_valid:bool = False
print(is_valid)

is_married:bool = True
print(is_married)



# 5.list  (list) : Multiple values ka ordered collection (changeable) ye mutable h
# Mutable ka matlab hai ke list ko change kiya ja sakta hai (elements add, remove ya modify kiye ja sakte hain).

fruite_list : list = ["apple","mango","banana","papaya","grapes","cheery"]
print(fruite_list)

# List ka element change karne k ley ..
fruite_list[2] = "melon"
print(fruite_list)

# List me naya element add karna ho to ..
fruite_list.append("orange")
print(fruite_list) 

# List se element remove karna ho to ..
fruite_list.remove("orange")
print(fruite_list)  

# 6.tuple  (tuple) : tuple means Multiple values ka ordered collection but ye immutable hota h 

numbers = (1, 2, 3)
print(numbers)  

#  Tuple me value change nahi hoti
# numbers[0] = 10   
# error show kare ga

# Tuple immutable hoti hai (iski values change nahi ho sakti).
# Tuple ke andar agar list ho, to wo mutable hoti hai.

# 7.Dictionary  (dict) : Dictionary ek key-value pair ka collection hota hai.
#  Isme har value ek unique key se related hoti hai. Ye ek mutable (changeable) data structure hai.
# just like 

person = {
    "name": "Sadaf",
    "age": 25,
    "city": "Karachi"
}
print(person)  
# Output: {'name': 'Sadaf', 'age': 25, 'city': 'Karachi'}

# ✔ Dictionary key-value pairs ka collection hoti hai.
# ✔ Isme data ko fast retrieve kar sakte hain.
# ✔ Mutable hoti hai, yani update ho sakti hai.
# ✔ Keys unique hoti hain, yani ek key bar bar nahi ho sakti.


# 8.set    (set) : Set ek unordered collection hoti hai jo unique values store karti hai.
#  Matlab, duplicate values store nahi hoti.

colors = {"red", "blue", "green", "red","blue"}
print(colors)  
# is ka print ayga {"red","blue","green"}
#  Sets unordered hote hain, yani values kisi bhi order me print ho sakti hain.
#  Duplicate values nahi hoti:
  
