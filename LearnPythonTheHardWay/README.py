#Comments start with #
print "This will print" #This will print a statement to console
print "Hens", 25 + 30 / 6 #This prints 'Hens 30' to console
print "We need to put about", 3, "in each car" #This prints 'We need to put about 3 in each car'
my_eyes = 'Blue'
my_hair = 'Brown'
print "I have %s eyes and %s hair" %(my_eyes, my_hair)
x = "There are %d types of people" %10
print "I said: %r" %x #This prints 'I said: 'There are 10 types of people''
hilarious = False	#boolean
joke_eval = "Isn't that a funny joke? %r"
print joke_eval % hilarious	#This prints 'Isn't that a funny joke? False'
end1 = "Cheese "
end2 = "Burger"
print end1,	#Pay attention to the , at the end of the line
print end2	#Prints 'Cheese Burger' on one line, without comma, it would be printed on 2 separate lines
print """This will type
multi lines"""
print "How old are you?",
age = raw_input()	#The function reads a line from input, converts it to string (stripping the trailing newline) and returns that
from sys import argv
script, first, second, third = argv #this assigns script and first 3 arguments to the variables
txt = open(filename) 	#opens file object
print txt.read()		#prints complete contents of file
txt.seek(0)				#resets cursor position to begining of file
print txt.readline()	#prints one line of the file from the current cursor position
from os.path import exists
exists(to_file)			#returns if the file to_file exists
len(in_data)			#returns the lenght of an object
def print_two(*args):		#function definition like with argv
	arg1, arg2 = args
def print_two_again(arg1, arg2):		#function definition with finite args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
int(raw_input())		#converts to int from raw values