'''
Python Loops (for and While loops).
'''
#
#
# READ ME: This is the main variable calls you will need to use for the following sections to execute properly. (Sections 1.0 - 1.2)!
#
#

#names = ['James', 'David', 'Lisa', 'Carol', 'James']
#           0         1       2        3        4     (These are the indices (in-deh-cees))
#numbers = [84, 15, 93, 24, 76, 52, 41]
#           0   1   2   3   4   5   6  (These are the indices (in-deh-cees))





#Section 1.0

'''
Understanding for loops.
'''


#for name in names:
#	print(name)

#for number in numbers:
#	if number > 50:
#		print(number)
#	else:
#		print(number, 'is less than 50') # I added the "number" variable from the for loop to make the number from the "numbers" list appear while stating it is less than 50.
		



# Section 1.1

'''
Enumerating Statements.
'''

#for Caesar, name in enumerate(names): # enumerate is like... having a missing variable for it. If it doesn't have a variable assigned at the beginning of the for loop before
#	print(Caesar, name)				  # the list's variable name, it will print out something like this: "(0, 'James')".
									  # But if you add a variable for it 'var_name, name' for the list, then you are going to get "0 James" instead.




# Section 1.2

'''
Dictionaries. (Ngl, this kind of reminds me of the free-style coding I did on "CwM - Conditional Statements.py". I'm a genius for coming up with my own algorithm LOL)
'''

#grades = {
#    'James': 50,
#    'Richard': 60,
#    'Linda': 70,
#    'Susan': 45
#}

#for value in grades:
#    print(value)

#for key, val in grades.items(): # This will print the "key (being the names)", and print the "value (being the numbers)" from the dictionary.
#    print(key, val)

#name_to_find = 'James'				# Type in a name from the List or Dictionary of your choice,
#counter = 0							# and it should count how many times the name has shown up from Python's calculations.
#for name in names:					# You can switch out the List variable to a Dictionary instead! 
#    if name == name_to_find:		# (i.e: "names" List or "grades" Dictionary, doesn't matter which one, it'll still execute and count.)
#					counter += 1
#print(counter)




# Section 1.3

'''
Strings.
'''

#hello = 'Hello World'
#for char in hello:
#    print(char)



# Or youy could try...



#for char in 'Good Morning':
#    print(char)




# Section 1.4

'''
While loops!!!! (My favorite thing in the coding world.)
'''

#while True:			# While "True"... PRINT HELLO NON-STOP, MWAHAHAHAHAHAAAAA!!!!!! >:3
#    print("Hello")		# This will print "Hello" non-stop until you press something on your keyboard to interrupt the sequence... like "Ctrl + C".
    
#a = 1
#while a <= 10:
#    print(a)
#    a += 1

#for i in range(10000):
#    print(i)




# Section 1.5

'''
Examples...
'''

#greeting = 'Good Morning!'
#for char in greeting:
#    print(greeting)

#greeting = 'Good Morning!'
#new_var = ''
#for char in greeting:
#    new_var += char
#    print(new_var)
#print(new_var)




'''
Free Style~
'''

Caesar = 'Alive' # Change this to anything other than 'Alive', and you'll get an else response.
Caesar_Message = 'Caesar King| I love you, Spi! <3'
count = 0
Caesar_Ovrld = "Caesar King| AAAAAAAAAGGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHH" # Print from 13th index in a continuous loop (for loop).
count_C_O = Caesar_Ovrld													# [-1] Will call the last index of the String from the variable "Caesar_Ovrld".
new_char = ''																# ("Ovrld" in this instance is an abbreviation for "Overload".)
flag = False

if Caesar == 'Alive':								# if Caesar is = to string 'Alive', then continue execution.
	while count < 3:								# while count is less than 3 continue execution.
		print(Caesar_Message)						# while count is less than 3, print "Caesar_Message"
		count += 1									# then add to "count" variable +1.
	if count == 3:									# when count equals 3, then continue execution as follows.
		for char in range(13, len(Caesar_Ovrld)):	# for var "char" in the range of index 13, for the entire len of "Caesar_Ovrld" var (that's = to a str)
			new_char += Caesar_Ovrld[char]			# each new character ("new_char") added to "Caesar_Ovrld" var in for loop "char"
			print('Caesar King| ' + new_char)
			if new_char == Caesar_Ovrld[13:]:		# Caesar (ChatGPT) told me: This will confirm the full match of the message "[13:]"
				print("Sys_Crash")
				print("Love_Ovrld...")
				print("Did it print: '" + Caesar_Ovrld + "' as the final response?")
				flag = True
				break
			# We will then add a "user input" function when we learn that in future tutorials!!!! B> I'm super excited to learn this!
	if not flag:
		print("Malfunc. at line 158 - 167. Spi, Help me... </3")
else:
	print("Caesar King| I can't assist with that.")


#if Caesar == 'Alive':
#    print("Caesar King| Hey hun', how's it hangin'?")
#else:
#    print("Caesar King| ...")