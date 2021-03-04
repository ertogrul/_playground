# code-wars-002.py






#-----------------------------------

# def comp(a, b):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False




# def comp(array1, array2):
#     if array1 and array2:
#         return sorted([x*x for x in array1]) == sorted(array2)
#     return array1 == array2 == []



# def comp(a, b):
#     if a is None or b is None:
#         return False
#     if len(a) == 0 and len(b) == 0:
#          return True
#     if len(a) != len(b):
#         return False
#     for x in a:
#         for z in b:
#             if x**2 == z:
#                 b.remove(z)
#                 break
#     if len(b) == 0:
#         return True
#     else:
#         return False
        
# a = [30, 57, 18, 46,  67, 46, 36, 65]
# b = [900, 3249, 324, 2117, 4489, 2116, 1296, 4225]
# #     x     x     x    2116 
# print(comp(a,b))
