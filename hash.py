import hashlib

passw = input("password : ")

encr_wrd = passw.encode("utf-8")
digest = hashlib.md5(encr_wrd.strip()).hexdigest()

print("hash: "+digest)