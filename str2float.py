from functools import reduce
def str2float(s):
	str_arr=s.split('.')
	dic= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def str2int(x,y):
		return x*10+y
	def float_str(a):
		return reduce(str2int,map(lambda x:dic[x],a))/float(10**len(a))
	return reduce(str2int,map(lambda x:dic[x],str_arr[0]))+float_str(str_arr[1])
L=str2float('123.456')
print(L)


