import re
from collections import namedtuple

HashCategory = namedtuple('HashCategory', ['regex', 'modes'])

HashCategories = [
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{32}(:.+)?$', re.IGNORECASE),
		modes=['MD5']),
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{40}(:.+)?$', re.IGNORECASE),
		modes=['SHA1']),
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{56}$', re.IGNORECASE),
		modes=['SHA224', 'SHA3_224']),
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{64}(:.+)?$', re.IGNORECASE),
		modes=['SHA256', 'SHA3_256', 'blake2s']),
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{96}$', re.IGNORECASE),
		modes=['SHA384', 'SHA3_384']),
	HashCategory(
		regex=re.compile(r'^[a-f0-9]{128}(:.+)?$', re.IGNORECASE),
		modes=['SHA512', 'SHA3_512', 'blake2b']),
]

def identifyHash(hash):
	for category in HashCategories:
		hash = hash.strip()
		if category.regex.match(hash):
			for algo in category.modes:
				yield algo

hash = input("submit the hash: ")
for algo in identifyHash(hash):
	print(algo)
