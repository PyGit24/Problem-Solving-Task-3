# Python3 program to Find total number of triplets in a temp_list with given h
 
def fTriplet(st, h):
    t_count = 0
    f_temp_list =[]
     
    for i in range(0, len(st)-1): 
        s = set() 
        temp_list = []
 
        # Adding first element
        temp_list.append(st[i])
 
        curr_k = h - st[i] 
         
        for j in range(i + 1, len(st)): 
             
            if (curr_k - st[j]) in s: 
                t_count += 1
                 
                # Adding second element
                temp_list.append(st[j])
 
                # Adding third element
                temp_list.append(curr_k - st[j])
                 
                # Appending tuple to the final list
                f_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(st[j])
             
    return f_temp_list
     
# Driver Code
#st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st=[10,20,30,9]
h = 59
print("\tProgram for finding Triplets")
print("The Given input is:",st)
print("The Sum of Triplets are:",h)
print("\nThe Triplets are:", fTriplet(st, h))