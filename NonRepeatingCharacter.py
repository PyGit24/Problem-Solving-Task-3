# program to find first non-repeating element in a List of Integers
def noRepeat(inps, v):
 
    # Loop for checking each element
    for i in range(v):
        j = 0
        # Checking if ith element is present in array
        while(j < v):
            if (i != j and inps[i] == inps[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == v):
            return inps[i]
    return -1
print("\tProgram To find Non Repeating Integers")
inps = input("Enter the Input Integer list")
#arr=[9, 4, 9, 6, 7, 4]
v = len(inps)
print("The Given Input is: ",inps)
print("The First Non Repeating Element is:",noRepeat(inps, v))