import hashlib
pass_hash = input("enter hash: ")
wordlist = input("file name: ")

flag = 0

try:
	pass_file = open(wordlist, 'r')
except:
	print("file not found")
	quit()

print(hashlib.algorithms_guaranteed)
algo = input("hashing function: ")

for word in pass_file:
	word = word.strip()
	encr_wrd = word.encode("utf-8")
	h = hashlib.new(algo)
	h.update(encr_wrd)
	digest = h.hexdigest()
	print(digest)
	
	if digest == pass_hash:
		print("password found")
		print(word)
		flag = 1
		break

if flag == 0:
	print("password is not in {}".format(wordlist))