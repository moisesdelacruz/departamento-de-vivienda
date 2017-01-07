import sys
import commands
import os

from core.createsuperuser import CreateSuperUser

if sys.argv[1] == 'run':
	os.system('python main.pyw')
elif sys.argv[1] == 'createsuperuser':
	if __name__ == "__main__":
		CreateSuperUser()