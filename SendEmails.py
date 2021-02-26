# To send an e-mail with python you must do the following:
# 1) connecting to an email server
# 2) confirming connection
# 3) setting a protocol
# 4) logging on
# 5) sending the message


# smtplib library
# SMTP = Simple Mail Transfer Protocol
# each e-mail provider has its own SMTP server
# e.g.:
# Gmail => smtp.gmail.com (will need App password)
# Gmail App password gives gmail know that the etempt to access your account is authorized by you
# before check the firewall. It can block your attempts to connect 

import smtplib
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)   # 587 = number of port, if it won't work than use: 465, or any number
# port 587 means that you are using TLS encryption
print(smtp_object.ehlo()) # ehlo method must be call just after creating the object
print(smtp_object.starttls()) # initiating TLS encryption, when you are using port 465 you can skip, cause it uses SSL encryption
# you should never use raw string of your email and password in a script, cause people can see it
# rather use input function or getpass built in library that will hide your password as asteriks

import getpass
# password = getpass.getpass("Password please: ") # getpass works only in jupyternotebook????
print()


# gmail users need to get APP password (you must activate 2 factor authentication as well)
# link to get app password: 
# https://support.google.com/accounts/answer/185833?hl=en/

email = input("Enter your e-mail: ")
password = input("Enter your password: ")
print(smtp_object.login(email, password))  # calling the login method on your smtp object

from_address = email
to_address = "kamil.klemsa@seznam.cz"
subject = input("Enter the subject: ")
message = input("Enter the body: ")
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address, to_address, msg)










