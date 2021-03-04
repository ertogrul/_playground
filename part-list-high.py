#part-list-high.py

arr = ["az", "toto", "picaro", "zone", "kiwi"]

def partlist(arr):
    if len(arr) <= 1:
        return []

    result = []

    s = ' '.join(arr)
    #print (s)

    j = len(arr[0])
    #print (s[j+1:])
    for i in range(1, len(arr)):
        result.append((s[:j], s[j + 1:]))
        j += 1 + len(arr[i])
    print(result)
    return result

  
partlist(arr)