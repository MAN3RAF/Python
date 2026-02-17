import importlib
import sys

# try:
# 	import matplotlib
# 	import requests
# 	import pandas
# 	import numpy

# except ModuleNotFoundError as e:
# 	print("LOADING STATUS: Loading programs...\n")
	
# 	print(f"[ERROR] '{str(e).split("'")[1]}' was not installed..!")

# 	print("\nInstall with:")
# 	print("  pip install -r requirements")
# 	print("or\n  poetry install")
# 	sys.exit(1)


# print("\nLOADING STATUS: Loading programs...\n")

# print("Checking dependencies:")
# print(f"[OK] matplotlib ({matplotlib.__version__}) - Data manipulation ready")
# print(f"[OK] requests ({requests.__version__}) - Data manipulation ready")
# print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
# print(f"[OK] numpy ({numpy.__version__}) - Data manipulation ready")



def check_module(module_name):

	try:
		module = importlib.import_module(module_name)
		return f"[OK] {module_name} ({module.__version__}) - Ready"

	except ModuleNotFoundError:
		return f"[ERROR] {module_name} - Was not installed"


modules = ["matplotlib", "requests", "pandas", "numpy"]

all_here =[check_module(module) for module in modules]

all_in = True

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
for i in all_here:
	if i.startswith("[ERROR]"):
		print(i)
		all_in = False

if not all_in:
	print("\nInstall with:")
	print("  pip install -r requirements")
	print("or\n  poetry install")
	sys.exit(1)

for module in modules:
	print(check_module(module))
