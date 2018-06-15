# NB Special
# Python Brute Forcer - SHA1
This project is to demonstrate brute-forcing with Python. There are two versions.

Brute force hash function - It will take a SHA1 hash, and compare it to SHA1 hashes of the top 10,000 worst known user passwords, printing the correct password if found.

Installation: Run:"git clone https://github.com/sadmin2001/pythonclass.git" Run: "cd pythonclass" Run "sudo pip3 install -r requirements.txt" Run "python3 NBspecial.py" for the 28 line version or "python3 SHA1BruteForce4Lines.py" for the 4 line version. They work the same.

To see how this works, you can look at the documented code in the NBspecial.py file.

If you get an error that reads: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>

In your terminal, run "/Applications/Python\ 3.6/Install\ Certificates.command" This will update your certificates
