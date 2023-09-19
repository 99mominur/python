import hashlib

email = "99moinu@gmail.com"

password = "99mominur"

pass_hash = hashlib.md5(password.encode()).hexdigest()


print(pass_hash)
