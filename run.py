import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import main
bit = platform.architecture()[0]
if bit == '32bit':
	print('Sorry Your Device Is Not Supported')
	
