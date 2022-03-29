#!/usr/bin/python3

import os

def main():
	os.system('clear')
	print("                   __          __")
	print("                   \ \        / /")
	print("  _ __   __ _ ___ __\ \  /\  / / ")
	print(" | '_ \ / _` / __/ __\ \/  \/ /  ")
	print(" | |_) | (_| \__ \__ \\  /\  /   ")
	print(" | .__/ \__,_|___/___/ \/  \/    ")
	print(" | |                             ")
	print(" |_|                             ")
	print("created by goro16")
	a = input("\n1- look the saves passwords\n2- add a new password\n3- delete a password\n4- exit\nchoose a number : ")

	if a == '1':
		os.system('clear')
		passw()

	if a == '2':
		os.system('clear')
		add()

	if a == '3':
		os.system('clear')
		delt()

	if a == '4':
		os.system('clear')
		exit()


def passw():
	os.system('clear')
	print("this is your passwords : ")
	os.system('cat db.txt')
	a = input("\n1- return to menu\n2- find a password\n3- exit\nchoose a number : ")


	if a == '1':
		os.system('clear')
		main()

	if a == '2':
		os.system('clear')
		search()


	if a == '3':
		os.system('clear')
		exit()



def add():
	os.system('clear')
	url = input('what is the url : ')
	user = input('what is the username : ')
	password = input('what is the password : ')
	os.system(f'echo "{url}, {user}, {password}" >> db.txt')
	a = input("\n1- return to menu\n2- exit\nchoose a number : ")


	if a == '1':
		os.system('clear')
		main()


	if a == '2':
		os.system('clear')
		exit()

def delt():
	os.system('clear')
	print ("this is your password : ")
	os.system('cat -n db.txt')
	ligne = input('which line do you want to delete (number) : ')
	os.system('touch db2.txt')
	os.system('chown root db2.txt')
	os.system('chmod a-wrx db2.txt')
	os.system(f"sed '{ligne}d' db.txt >> db2.txt")
	os.system('rm -rf db.txt')
	os.system('mv db2.txt db.txt')
	a = input("\n1- return to menu\n2- exit\nchoose a number : ")


	if a == '1':
		os.system('clear')
		main()


	if a == '2':
		os.system('clear')
		exit()

def search():
	a = input('enter the url to search : ')
	os.system('clear')
	print('here is the result of your search : ')
	os.system(f'cat db.txt | grep {a}')
	b = input("\n1- return to menu\n2- find another password\n3- exit\nchoose a number : ")


	if b == '1':
		os.system('clear')
		main()

	if b == '2':
		os.system('clear')
		search()


	if b == '3':
		os.system('clear')
		exit()





if __name__ == "__main__":
    main()
