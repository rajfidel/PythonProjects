def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions."
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for extra credit
print "Here is the puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) 
#divide(50, 2) = 25
#multiply(180, 25) = 180 * 25
#subtract(74, 180 * 25) = 74 - 180*25
#add(35, (74 - (180*25)))
print "That becomes: ", what, "Can you do it by hand?"