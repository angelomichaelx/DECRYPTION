#Michael Angelo P. Biag
#BSCOE 1-4

#Problem number 2 :DECRYPTION (25 points)
def main():
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
        elif input_string[i] == "#":
                output_string += "i"
    #if the input string is  +, then change it to letter o
        elif input_string[i] == "+":
                output_string += "o"
    #if the input string is  !, then change it to letter u 
        elif input_string[i] == "!":
                output_string += "u"

        else:
            output_string += input_string[i]
    #print output with decoration
    print("\033[1;36m" +"=" * 20)
    print( output_string)
    print("=" * 20)
    #program if you want to repeat it again
Repeat = input("Would you like to try again? (yes/no) : ").lower()
if Repeat == "yes":
            main()
else:
            print("Thank you!!")
            exit()
main()