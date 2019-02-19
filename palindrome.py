first_string = input("Enter your maybe palindrome maybe not a palindrome here.")

no_spaces = first_string.replace(" ", "").replace("!", "").replace(",", "").replace(":", "")
#Firstly, removes spaces, then removes !'s, then removes ,'s, then removes :'s. 



no_lowers = no_spaces.lower()
#Changes all uppercase letters to lowercase



#print(no_lowers)

if no_lowers[:] == no_lowers[::-1]:
    print('This is a palindrome.')
else:
    print("This is not a palindrome.")
