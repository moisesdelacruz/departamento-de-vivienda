import sys
import commands
import os
import platform

if sys.argv[1] == 'build':
	os.system('./run_build.sh')

elif sys.argv[1] == 'run':
	if platform.system() == "Windows":
		os.system('python main.pyw')
	else:
		os.system('./run_project.sh')

elif sys.argv[1] == '__createsuperuser':
	if __name__ == "__main__":
		from core.createsuperuser import CreateSuperUser
		CreateSuperUser()

elif sys.argv[1] == 'createsuperuser':
	if platform.system() != "Windows":
		os.system('./run_createsuperuser.sh')
	else:
		os.system('python manage.py __createsuperuser')
