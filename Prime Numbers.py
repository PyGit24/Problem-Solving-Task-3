#Program using function to return the number of prime numbers in a input
def countp(nu):
    count=0
    pr=[]
    for num in nu:
        if(num<2):
            continue
        else:
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                pr.append(num)
                count+=1
                
    return count
z= [10,501,22,37,100,999,87,351]
print("Program to count the prime numbers in a given input")
print("The Given Numbers are:", z)
print ("The Total Number of Prime Numbers are:", countp(z))
