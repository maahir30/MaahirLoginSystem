import sys
import simplejson as json
from userlist import users

def saveToFile():
	json_userlist = json.dumps(users) #create python userlist to a json string
	f = open("userlist.py","w")
	f.write('users = '+ json_userlist)
	f.close()

#Initial Login Page for users once they run program
def loginpage():
	while True:
		startup = input("Do you want already have an account? Answer y or n.")
		if startup.lower() == 'y':
			loginuser() 
			break
		elif startup.lower() == 'n':
			asknewuser()
			break
		else: 
			print('Sorry I did not understand your answer. Please type only y or n.')
			continue

#If user has an account, they login using this function
def loginuser():
	#tjson = json.dumps(users)
	loop = True
	while loop:
		olduser = str(input("Username:"))
		for username in users:
			if username == olduser:
				while True:
					oldpwd = str(input("Password:"))
					if users[username] == oldpwd:
						print("Login Success!")
						loop = False
						break
						loop = False
					else:
						print("Password Incorrect!")
						continue


#If user doesn't have an account, he/she can create one here
def asknewuser():
	while True:
		newacc = input("\n\n\nDo you wish to create a new account? Answer y or n.")
		if newacc.lower() == 'y':
			createuser() 
			break
		elif newacc.lower() == 'n':
			break
		else: 
			print('Sorry I did not understand your answer. Please try again.')
			continue

def createuser(): 
	creatinguser = True
	while creatinguser:
		newuser = str(input("Create a username: "))
		confirmnewuser = str(input("Confirm your username: "))
		if newuser == confirmnewuser:
			while True:
				newpwd = str(input("Create a password: "))
				cofirmnewpwd = str(input("Confirm your password: "))
				if newpwd == cofirmnewpwd:
					users[newuser] = newpwd
					print("Account Created!")
					creatinguser = False
					saveToFile()
					break
				else:
					print("Passwords don't match. Please try again.")
					continue
		else:
			print("Usernames don't match. Please try again.")
			continue

loginpage()
#saveToFile()
				