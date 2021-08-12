# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
	distSq = ((x1 - x2) **2) + ((y1 - y2) **2)
	radSumSq = (r1 + r2) **2
	if (distSq == radSumSq):
		return True
	elif (distSq > radSumSq):
		return False
	else:
		return True
