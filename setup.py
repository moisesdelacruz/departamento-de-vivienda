from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.pyw",
								base = base,
								icon = "views/images/home.ico")]
 
build_exe_options = {"packages": [],
					 "include_files":[]}

setup(name = "main",
	version = "0.1",
	description = "main",
	options={"build_exe": build_exe_options},
	executables = executables)