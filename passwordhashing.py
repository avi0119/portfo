import hashlib

def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    print(f"hashed pw: {password_hash}")
    return password_hash

def verify_password(stored_password, provided_password, salt):
    password_hash = hashlib.sha256((provided_password + salt).encode('utf-8')).hexdigest()
    print(f"hashed pw: {password_hash} and stored is {stored_password} provided :{provided_password}")
    return password_hash == stored_password
if True==False:
	# Example usage:
	user_password = "Your Passowrd"
	provided_salt = "Your Salt"  # Replace with your specific salt key

	# Hash the password
	hashed_password = hash_password(user_password, provided_salt)
	print("Hashed Password:", hashed_password)

	# Verify a password
	provided_password = "Provided Passowrd"
	password_matched = verify_password(hashed_password, provided_password, provided_salt)
	print("Password Matched:", password_matched)