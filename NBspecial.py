from urllib.request import urlopen, hashlib

#First, get the hash from the user to get the sha1 hash to crack
origin = input("Please input the hash to crack.\n>")

#Second, we'll open a file full of password guesses
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

#Third, we'll take a password from the list of passwords we opened, and split it by line
for password in LIST_OF_COMMON_PASSWORDS.split('\n'):

#Fourth, we'll hash the guess we took from the password list so we can compare it to the hash the user gave us
    setpass = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()

#Fifth, we'll compare the hash the user gave us to the hashed version of the password guess, and set a condition for if they match
    if setpass == origin:
        print("The password is ", str(password))
        quit()

#In the sixth step, we'll tell the program what to do if the password guess doesn't match the hash we're trying to crack, and return to get a new password from the list
    else:
        print("Password guess ",str(password)," does not match, trying next...")

#In the seventh and final step, we'll tell the program what to do if we get all the way through the password list without finding a match.
print("Password not in database, we'll get them next time.")
