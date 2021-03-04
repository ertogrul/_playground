#code-wars-001.py

# word = "din"
# word = "recede"


from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    print(counter) # <----- TU MAMY WYMIENIONE ILE RAZY KAZDA LITERA WYSTEPUJE :)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

print(duplicate_encode("Q@HRJI)w@RRTb(adIkwFOFwu"))



# WORKING CODE!!!
# def duplicate_encode(word):
#     word = word.lower()
#     n = len(word)
#     new_word = ""
#     duplicates = []
#     for x in range(n):
#         duplicate = False
#         if word[x] in duplicates:
#             duplicate = True
#             new_word = new_word + ")"
#             continue

#         for z in range(x+1,n,1):
#             if word[x] == word[z]:
#                 duplicate = True
#                 new_word = new_word + ")"
#                 duplicates.append(word[x])
#                 break
#         if duplicate == False:
#             new_word = new_word + "("
#     print(new_word)
        
# duplicate_encode("Q@HRJI)w@RRTb(adIkwFOFwu")





#--------------------------------------------------
# inspiration: 
# Python program for implementation of Bubble Sort
 
# def bubbleSort(arr):
#     n = len(arr)
 
#     # Traverse through all array elements
#     for i in range(n):
 
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
 
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
 
# bubbleSort(arr)
 
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]), 
