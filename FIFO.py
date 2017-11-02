from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity=capacity


	def __setitem__(self,key,value):
		containsKey=1 if key in self else 0
		print self
		print len(self)
		if len(self)-containsKey>=self._capacity:
			last=self.popitem(last=False)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)
	
a=LastUpdatedOrderedDict(7)
for i in range(3):
	a[i]=i
for i in range(3):
	a[i]=i

