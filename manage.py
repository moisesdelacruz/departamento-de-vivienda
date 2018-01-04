import sys
import commands
import os

if sys.argv[1] == 'build':
	os.system('./run_build.sh')

elif sys.argv[1] == 'run':
	os.system('./run_project.sh')

elif sys.argv[1] == 'createsuperuser':
	if __name__ == "__main__":
		from core.createsuperuser import CreateSuperUser
		CreateSuperUser()

elif sys.argv[1] == 'createuser':
	os.system('./run_createuser.sh')
