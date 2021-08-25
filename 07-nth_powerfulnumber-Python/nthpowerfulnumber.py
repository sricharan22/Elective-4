# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isPowerfulNumber(k):
    if(k == 1):
        return True
    for i in range(1,round(k**0.75)):
        for j in range (i,round(k**0.75)):
            if(((i**2)*(j**3) == k) or ((i**3)*(j**2) == k)):
                return True
    return False


def nthpowerfulnumber(n):
	# Your code goes here
	count = 0
	check = 0
	while(count <= n):
		check = check+1
		z = isPowerfulNumber(check)
		if(z):
			count += 1
	return check

