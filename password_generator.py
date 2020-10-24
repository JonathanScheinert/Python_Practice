#password generator 
import random 
#init
# n = number of characters in password
n = 12
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()-+=_ '
chars = ''
# l = lower_case , U = upper_case , 0 = digits , $ = symbols
complexity = 'lU0$'
# complexity = combination of characters
password = ''
#characters we are going to use for password

if 'l' in complexity:
	chars += lower_case
if 'U' in complexity:
	chars += upper_case
if '0' in complexity:
	chars += digits
if '$' in complexity:		
	chars += symbols

for i in range(n):
	password += chars[random.randrange(0,len(chars))]

print('Password: ',password)