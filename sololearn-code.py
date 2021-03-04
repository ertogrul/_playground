# sololearn-code.py




#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
x = {"gg", "a", "b", "c"}
y = {"m", "a". "c"}

z = x.difference(y) 

print(z)
#------------------------------------------------------------------
# a = {1, 2, 3}
# b = (1, 2, 3)
# c = [1, 2, 3]
# print(type(a))
# print(type(b))
# print(type(c))
#-------------------------
# a = {1, 2, 3}
# b = frozenset([3,4])
# c = b.difference(a)
# print(c)
#t(c.pop())

#------------------------------------------------------------------
# a = {1, 3, 5}
# b = {2, 4, 6}
# for i in range(7):
#     print(i)
#     if i not in a and i not in b:
#         print(False)
#         break
#     else:
#         print(True)
#------------------------------------------------------------------
# REGEX USAGE
# import re
# str = "mystring"
# search = "^mystring"
# if re.match(search,str):
#     print("time")
# else:
#     print("emit")
#------------------------------------------------------------------

# a = [10,3,7]
# y,x,z = a
# print(a)
# print(y%z)
# print(10%7)
# print(10/7)
# print(10//7)
# print(12/7)
# print(3%)
#------------------------------------------------------------------
# a = [{x*2,x+2} for x in range(5)]
# print(type(a[1]))
# answer: class set
#------------------------------------------------------------------
# x = 0
# a = []
# while x <= 3:
#     x *= 2
#     a.append(x)
# print(a)
# answer - this is infinite loop a = [0] and then x does not change into anything
#------------------------------------------------------------------

# s='abc'
# i = iter(s)
# next(i)
# next(i)
# print(next(i))
#------------------------------------------------------------------
# print(3**3%7)
#------------------------------------------------------------------
# CIEKAWY SPOSÓB NA UTWORZENIE INSTANCJI: Go()(5)
# class Go:
#     def __call__(self, x):
#         return x

# try:
#     print(Go()(5))
# except:
#     print(-9)
#-----------------------------------------------------------------

# colors = ['red', 'blue', 'green', 'yellow']
# result = ''.join(colors)
# print (result)
# #------------------------------------------------------------------
# class A():
#     def __init__(self, x=0):
#         self.x = x
#     def __str__(self):
#         self.x += 1
#         return str(self.x)
# a = A()
# print(a)
# print("".join([str(a), str(a)]))

#------------------------------------------------------------------
# text = "SoloLearn"
# print (text[:-1:])
#------------------------------------------------------------------

# a = [2, 3, 1, 0]
# b = [3, 1, 0, 2]
# c = []
# for i in a:
#     if i == b[i]:
#         c.append(i)
#         # print("i " + str(i))
#         # print("b[i] " + str(b[i]))
#     else:
#         continue
# print(len(c))

#------------------------------------------------------------------
# dict = {1:2, 3:4}
# d = dict
# d[1] = 9    #<-------- d[1] TO JEST PIERWSZY A NIE DRUGI ELEMENT
#             # W SLOWNIKACH LICZYMY OD 1, NIE OD 0.
# print(dict)

#------------------------------------------------------------------
# print(2**3**2)
# print(2**9)
#------------------------------------------------------------------
# x = 0
# a = []
# while x <= 3:
#     x *= 2
#     a.append(x)
#     print(a)
# result: infinite loop :)
#------------------------------------------------------------------
# list = ["1", "2", "3"]
# num1 = list[1]
# num2 = str(num1 + "3")
# num3 = list[2]
# print(num2 + num1 + num3)

#------------------------------------------------------------------
# items() uzywamy do wyswieltania slownika (razem key i value)

# calories = {'apple':52, 'banana':89, 'choco':95}
# for k,v in calories.items():
#     print(k) if v > 90 else None
#------------------------------------------------------------------
# word = 'spam'
# print("{}".format(word[::-1]))
# output maps
#------------------------------------------------------------------
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
#------------------------------------------------------------------
# print(type(1J))
# odp type complex
#------------------------------------------------------------------

# var = 1
# temp = 0
# if var == 1:
#     var += 10
# else:
#     var = 2
# while var<11 and temp < 10:
#     var -= 1
#     temp += 1
# print(var)
# odp: var to 11
#------------------------------------------------------------------

# def add(x,y):
#     return x + y
# def fun(func, x, y):
#     return func(func(x,y),func(x,y))
# a = 5
# b = 10
# print(fun(add,a,b))


#------------------------------------------------------------------
# print(2*(2000*2000000)+4000000+200*3.134)
#------------------------------------------------------------------
# nums = [x for x in range(5)]
# print(nums)
# nums = [x for x in range(-2, 4, 2)]
# print (nums)
# nums *=5
# print (nums)
# print(sum(nums))
#------------------------------------------------------------------

# class Go:
#     def __call__(self,x):
#         self.x = x
#         self.x = self.x + 1
#         return x

# print(Go(1))

# try:
#     print(Go(1))
# except:
#     print(0)


#------------------------------------------------------------------
# def func(named_args,*args):
#     print (named_args)
#     return *args

# func(1,2,3,4,5)
# -----> `OUTPUT IS ERROR`

#------------------------------------------------------------------
# print((("hey").upper()).lower())
#------------------------------------------------------------------
# x = 1
# while x < 5:
#     if x == 3:
#         print(x + 10)
#     x += 1
#------------------------------------------------------------------
13
14
# a = 'spam'
# b = 'eggs'
# a,b = b,a
# print(a+b)

#------------------------------------------------------------------
# x = lambda a : a + 10
# print(x(5))

# my_list = ["apples","tomato", "banana", "orange", "melons" ]

# # my_list.sort()
# my_list.sort(key = lambda x:x[3])
# print(my_list[1])


#------------------------------------------------------------------
# nums = [10, 5, 38]
# nums.append(45)
# print(nums)
# nums.pop()
# print(nums)
# # nums.pop()
# # print(nums)

# nums = [4, 4, 1, 1, 1]
# print(len(nums*nums[1]))


#------------------------------------------------------------------
# b = 3
# a = 1
# for i in range(b):
#     print(i)
#     a = a + a * i
#     print(a)
#print(a)
#------------------------------------------------------------------
# x = [2, 3, 4]
# y = x
# print(y is x)
#------------------------------------------------------------------
# fill in the blanks(...) to print the squares of the list in the reverse order

# >>> del a[:] # <-- oznacza wszystko
# >>> a
# a[3:10:2] <-- oznacza od, do, jaki krok 

# a= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::-1])


# x = [x**2 for x in range(1,6)]
# # print(x)
# print(x[::-1])

#------------------------------------------------------------------
 
# range(start, stop, step)
# print(list(range(100)))
# print(list(range(12)))
# print(list(range(50, 100, 3)))


# lambda syntax
# lambda arguments : expression
""" x = lambda a : a + 10
print(x(5)) """


# print(list(map(lambda x, y : x + y, list(range(100)), list(range(12)))))


# k = list(map(lambda x, y : x + y, list(range(100)), list(range(12))))
# print(len(k))

#------------------------------------------------------------------

""" 
numbers = [11,12,13,14]
res=list(numbers)
print(res[3])
print(list(numbers))
 """

""" 
def do_twice(x):
    return x*2
numbers = [11,12,13,14]
res=list(map(do_twice,numbers))
print(res[1]) """

#------------------------------------------------------------------
""" 
# bool function returns boolean value of arg
a = not bool("False")
if (not a):
    a = a + 1
print(a)

 """

# empty dictionary:
# new_dict = {}
# new_dict = dict()
#
# empty list:
# a = []
# a = list() 
#
# tuple
# thistuple = ("apple", "banana", "cherry")

""" 
print(0==0)
print(0==False)
print(0==(0))
print(0==[0])
 """

""" 
# fill in the blank to convert the string into the following list ['Hello', 'world']
Hello = "Hello world"
print(Hello.split(' '))

 """




