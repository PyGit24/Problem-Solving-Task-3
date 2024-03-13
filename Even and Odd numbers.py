#Program to find Even and Odd numbers
numb=[10,501,22,37,100,999,87,351]
even=[]
odd=[]
for i in numb:
    if (i % 2==0):
        even.append(i)
    else:
        odd.append(i)
        
print("Program to find Odd and Even Numbers")
print("The Given input is:", numb)
print("The Odd Numbers are", odd)
print("The Even Numbers are", even)