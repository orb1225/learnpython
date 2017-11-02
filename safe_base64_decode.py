import base64

def safe_base64_decode(s):
	if(len(s)%4==0):
		return base64.b64decode(s)
	if(len(s)%4==1):
		return base64.b64decode(s+'=')
	if(len(s)%4==2):
		return base64.b64decode(s+'==')
	
		 



