# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def happy(k,n):
    sum = 0
    temp = k
    while(temp > 0):
        a = temp % 10
        temp = temp // 10
        sum += ((a) ** 2)
    if(sum ==1 or sum ==7):
        return True
    elif(sum < 10):
        return False
    elif(sum == n):
        return False
    else:
        return happy(sum,n)  


def nth_happy_number(n):
	count = 0
	k = 1
	while(True):
		if(happy(k,k) == True):
			count = count + 1
		if(count == n):
			return k   
		k = k + 1
