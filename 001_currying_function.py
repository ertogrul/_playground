
def multiply_all(array,number):

    result = []
    def multiply_one(abc):
        #print("multiply_one: "+str(abc))
        return result.append(abc*number)

    for i in range(len(array)):
        #print(array[i])       
        multiply_one(array[i])
    for a in range(len(result)):    
        print ("result: " + str(result[a]))
    return result



array = [1, 5, 3]
number = 2
multiply_all(array,number)












# array = [1, 2, 3]
# number = 2
# result = []

# def multiply_one(abc):
#     print("multiply_one: "+str(abc))
#     return result.append(abc*number)

# def multiply_array(array):
#     for i in range(len(array)):
#         print(array[i])       
#         multiply_one(array[i])
#     for a in range(len(result)):
#         print ("result: " + str(result[a]))
#     return result


# print(multiply_array(array))
