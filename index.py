import hashlib
file = open('contract', 'rb').read()
hash = hashlib.md5(file).hexdigest()

print(hash)