import os

def find_cur_file(p,f):
	return [x for x in os.listdir(p) if os.path.isfile(x) and os.path.split(x)[1].find(f)!=-1]
	
def find_dir(cur_path):
#pay attention: Here the isdir() just return the current dir name, it doesn't 
#contain the path or other imformation.
	return [os.path.join(cur_path,x) for x in os.listdir(cur_path) if os.path.isdir(os.path.join(cur_path,x))]
	

def find_all(p,f):
	for f in  find_cur_file(p,f):
		print(os.path.join(p,f))
		break
	for i in find_dir(p):
		find_all(i,f)

find_all('/home/shiyanlou','prod.py')
