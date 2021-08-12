# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.


import math
def fun_nearestbusstop(street):
	x = street%8
	if(x<=4):
		x = 0
	else:
		x = 1
	k = math.floor(street/8)
	return (k+x)*8
