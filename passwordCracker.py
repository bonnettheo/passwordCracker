import hashlib
pass_hash = input("enter hash: ")
wordlist = input("file name: ")

flag = 0

try:
	pass_file = open(wordlist, 'r')
except:
	print("file not found")
	quit()

for word in pass_file:
	encr_wrd = word.encode("utf-8")
	digest = hashlib.md5(encr_wrd.strip()).hexdigest()
	
	if digest == pass_hash:
		print("password found")
		print(word)
		flag = 1
		break

if flag == 0:
	print("password is not in {}".format(wordlist))