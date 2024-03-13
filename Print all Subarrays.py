# Python3 program to print all subarrays in the array which has sum 0
 
# Function to get all subarrays in the array which has sum 0
def FsArray(sub,n):
     # create a python dict
    hashMap = {}
     # create a python list equivalent to ArrayList
    out = []
     
    # tracker for sum of elements
    sum1 = 0
    for i in range(n):
         
        # increment sum by element of array
        sum1 += sub[i]
         
        # if sum is 0, we found a subarray starting from index 0 and ending at index i
        if sum1 == 0:
            out.append((0, i))
        al = []
         
        # If sum already exists in the map there exists at-least one subarray ending at index i with 0 sum 
        if sum1 in hashMap:
             
            # map[sum] stores starting index of all subarrays
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return out
 
# Utility function to print all subarrays with sum 0 
def printOutput(output):
    for i in output:
        print ("Subarray Found From Index " +
                str(i[0]) + " to " + str(i[1]))
 
# Driver Code
if __name__ == '__main__':
    sub=[4,2,-3,1,6]
    n = len(sub)
    print("\tProgram for Array with Sum Zero")
    print("The Given Input is:", sub)
    out = FsArray(sub, n)
     
    # if we did not find any subarray with 0 sum, then subarray does not exists 
    if (len(out) == 0):
        print ("No Subarray Exists")
    else:
        printOutput (out) 