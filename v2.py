#PBJ
#Goal 1
bread = 6
peanut_butter = 12
jelly = 24

if bread >= 2 and peanut_butter >= 12 and jelly >= 24:
	print "I can make a peanut butter and jelly sandwich"
else:
 	print "Looks like I don't have lunch today"

if bread >= 2 and peanut_butter >=1 and jelly >= 1:
	total = bread / 2
	if peanut_butter < total:
 		total = peanut_butter
 	if jelly < total:
 		total = jelly
 	print "I can make {0} sandwiches!".format(total)
 else:
 	print "No PB&J for me!"	
