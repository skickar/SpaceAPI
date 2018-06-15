#Condensed python code for sha1 hash cracker - using ternary operator. Example: <expression1> if <condition> else <expression2>
from urllib.request import urlopen, hashlib; origin = input("Input SHA1 hash to crack\n>")
for password in str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8').split('\n'):
    [print("The password is ", str(password)), quit()] if (hashlib.sha1(bytes(password, 'utf-8')).hexdigest()) == origin else print("Password not in database, we'll get them next time.") if password == "" else print("Password guess ", str(password), " does not match, trying next...")
