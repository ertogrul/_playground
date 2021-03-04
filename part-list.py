

arr = ["az", "toto", "picaro", "zone", "kiwi"]


def partlist(arr):
	
	# prepare l_part of the pair
	result_list = []
	l_part = ""
	go_finish = 0
	for z in range(len(arr)):
		l_part = l_part + arr[z] + " "
		#print(l_part)
		#print("XXXXX "+str(z+1))

		# prepare r_part of the pair
		r_part = ""
		for x in range(z + 1, len(arr)):
			r_part = r_part + arr[x] + " "
			#print(r_part)

		if r_part == " " or r_part == "":
			print("r_part nie ma elementow")
			go_finish = 1	
			break

		else:
			re_tuple = (l_part.strip(), r_part.strip())
			result_list.append(re_tuple)
			#print (result_arr)

		if go_finish == 1:
			break
		else:
			pass
		#print (pair_arr)
		#print ("--- ")
	return result_list

print (partlist(arr))




'''
def partlist(arr):
	l_part = ""	
	r_part = ""
	l_part = arr[0]
	r_part = arr[1] + " " + arr[2]
	result_arr.append(l_part)
	result_arr.append(r_part)

	return result_arr

'''



'''
[["az", "toto picaro zone kiwi"], 
 ["az toto", "picaro zone kiwi"], 
 ["az toto picaro", "zone kiwi"], 
 ["az toto picaro zone", "kiwi"]]
'''