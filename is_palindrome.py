def is_palindrome(a):
	return str(a)==str(a)[::-1]


print(list(filter(is_palindrome,range(1,1000))))
