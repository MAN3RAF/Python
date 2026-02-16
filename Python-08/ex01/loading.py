import importlib
import sys

try :
	import matplotlib
	import requests
	import pandas
	import numpy

except ModuleNotFoundError as e:
	print("LOADING STATUS: Loading programs...\n")
	
	print(f"[ERROR] '{str(e).split("'")[1]}' was not installed..!")

	print("\nInstall with:")
	print("  pip install -r requirements")
	print("or\n  poetry install")
	sys.exit(1)


print("\nLOADING STATUS: Loading programs...\n")

print("Checking dependencies:")
print(f"[OK] matplotlib ({matplotlib.__version__}) - Data manipulation ready")
print(f"[OK] requests ({requests.__version__}) - Data manipulation ready")
print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
print(f"[OK] numpy ({numpy.__version__}) - Data manipulation ready")

