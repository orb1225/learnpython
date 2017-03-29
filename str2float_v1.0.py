from functools import reduce
from sys import argv
script,s=argv
def str2float(s):
	str_arr=s.split('.')
	dic= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def str2int(x,y):
		return x*10+y
	return reduce(str2int,map(lambda x:dic[x],str_arr[0]+str_arr[1]))/float(10**len(str_arr[1]))

print str2float(s),type(str2float(s))


