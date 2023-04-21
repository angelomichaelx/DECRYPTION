#Michael Angelo P. Biag
#BSCOE 1-4

#Problem number 2 :DECRYPTION (25 points)

#this is where the user ask to input the string
input_string = input ("INPUT YOUR STRING? ")
output_string = ""

#to check every character
for i in range (len(input_string)):
#if the input string is  *, then change it to letter a
    if input_string [i] == "*":
            output_string += "a"
#if the input string is  &, then change it to letter e
    elif input_string[i] == "&":
                output_string += "e"

#if the input string is  #, then change it to letter i
#if the input string is  +, then change it to letter o
#if the input string is  !, then change it to letter u 
#print output with decoration
#program if you want to repeat it again