import hashlib

passw = input("password : ")

print(hashlib.algorithms_guaranteed)
algo = input("hashing function: ")

h = hashlib.new(algo)
h.update(passw.encode("utf-8"))
digest = h.hexdigest()

print("hash: "+ digest)