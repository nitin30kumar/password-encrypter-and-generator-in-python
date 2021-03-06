# Python code to encrypt your password

#                      ------------------------------------------------------
#                      -            Random Password Generator               -
#                      ------------------------------------------------------


# Importing random module of python
import random
import datetime

# Empty list
pswd=[]
ans = 'y'

# file open for passwords to save
savefile = open("passwords.txt","a")

# Loop for menu-driven
while(ans=='y' or ans=='Y'):
    
    # Take input from user for password
    pswd = input("\nEnter your password to encrypt: ")

    # List for encryption
    # Numbers, lowercase alphabets, uppercase alphabets, special characters
    st = [1,2,3,4,5,6,7,8,9,0,
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '~','!','@','#','$','%','^','&','*','(',')','_','+','{']

    # Empty string
    rslt=''

    # Loop to run encryption
    for i in pswd:
        # logic to generate password with random characters
        rslt+=str(random.choice(st))
    print("\nEncrypted password hence generated:",rslt.replace(',',''))


    # to save the passwords and date time in a file
    savefile.write("Stored at "+str(datetime.datetime.now()))

    # password input by user stored
    savefile.write("\n\nPassword input by user is - "+pswd)

    # password generated by code in stored
    savefile.write("\nPassword hence generated by code - "+rslt.replace(',',''))
    savefile.write("\n\n==================================================\n\n")
    
    # user message
    print("Please see the file passwords.txt file in same directory for your saved passswords.")
    
    # Asking user to exit or oontinue
    ans=input("\n\nDo you want more password to encrypt ? (y or Y)\t")

# file is closed
savefile.close()
#--------------------------------------------------------------

