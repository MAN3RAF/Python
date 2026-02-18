import importlib
import sys

def check_module(module_name):

	try:
		module = importlib.import_module(module_name)
		return f"[OK] {module_name} ({module.__version__}) - Ready"

	except ModuleNotFoundError:
		return f"[ERROR] {module_name} - Was not installed"

def check_all():
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
		return None

	for module in modules:
		print(check_module(module))
	
	return "Good"

def main():

	if not check_all():
		sys.exit(1)

	import matplotlib.pyplot as plt
	import pandas as pd
	import numpy as np

	print("\nAnalyzing Matrix data...")
	

	data = {'GTA III': 250, 'Vice City': 300}

	df = pd.DataFrame(list(data.items()), columns=["Game", "Income (Millions USD)"])
	df.plot.bar(x="Game", y="Income (Millions USD)", legend=False)

	plt.xticks(rotation=0)
	filename = "matrix_analysis"
	plt.savefig(filename)

	print("Analysis complete!")
	print("Results saved to: matrix_analysis.png")

main()