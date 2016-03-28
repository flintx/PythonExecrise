
# Python 2.7

import os
import sys
from hashlib import sha256
from hmac import HMAC

# sys.out = open('hehe.txt','w')

def encrypt_password(password, salt=None):
	if salt is None:
		salt = os.urandom(8) #64-bits

	assert 8 == len(salt)
	assert isinstance(salt, str)

	if isinstance(password, unicode):
		password = password.decode('UTF-8')

	assert isinstance(password, str)

	result = password
	# print result
	for x in xrange(10):
		result = HMAC(result, salt, sha256).digest()
		print result

	# print salt

	return salt + result

def validate_password(hashed, input_password):
	return hashed == encrypt_password(input_password, salt=hashed[:8])

def main():
	my_password = 'niconiconi'
	hashed = encrypt_password(my_password)

	print hashed

	other_password = 'niconiconi'

	print validate_password(hashed, other_password)

if __name__ == '__main__':
	main()
