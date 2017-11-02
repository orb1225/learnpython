import struct
def isbmp(files):
	with open(files,'rb') as fp:
		a=fp.read(30)
		stri=struct.unpack('<ccIIIIIIHH',a)
		if stri[0]==b'B' and stri[1]==b'M':
			print(stri[2],stri[-1])
			print(stri)
		else:
			print('not bmp')
