# Python code for calculating number of ways to distribute m mangoes amongst n people
# where all mangoes and people are identical

# function used binomial coefficient time complexity O(m)
def binoCoef(n, m):
	res = 1

	if m > n - m:
		m = n - m

	for i in range(0, m):
		res *= (n - i)
		res /= (i + 1) 

	return res

# helper function for generating no of ways
# to distribute m mangoes amongst n people
def calculate_ways(m, n):

	# not enough mangoes to be distributed 
	if m<n:
		return 0

	# ways -> (n + m-1)C(n-1)
	ways = binoCoef(n + m-1, n-1)
	return int(ways)

# Input function
if __name__ == '__main__':

	# m represents number of mangoes 
	# n represents number of people
	m = 7 ;n = 5
	print("\tProgram to Distribute M Mangoes to N Persons")
	result = calculate_ways(m, n)
	print("The Given Input(Mangoes) are: ", m)
	print("The Persons to be distributed are:", n)
	
	print("The Number of ways Mangoes can be distributed are:",result)
