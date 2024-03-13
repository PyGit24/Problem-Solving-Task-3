# Program to fid the happy numbers from the given inputs
a = [10,501,22,37,100,999,87,351]
b = []
def sapy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            b.append(a[i])
    return b
print("Program to find Happy Numbers")
print("The Given inputs are:",a)
print("Happy Numbers are:",sapy(a))