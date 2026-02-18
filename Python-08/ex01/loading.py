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
	print("")

	signal = np.full(1, 1000)
	print(f"Processing {signal[0]} data points...")

	# Create dataset
	data = {
		"Game": [
			"GTA III",
        	"Vice City",
        	"San Andreas",
        	"GTA IV",
        	"GTA V",
			],
    	"Revenue (Billion USD)": [
        	1.0,   # GTA III
        	1.2,   # Vice City
        	1.7,   # San Andreas
        	2.0,   # GTA IV
        	8.8,   # GTA V
			]
	}

	print("Generating visualization...\n")

	df = pd.DataFrame(data)

	# Create bar chart
	plt.figure(figsize=(10, 6))
	plt.bar(df["Game"], df["Revenue (Billion USD)"])

	# Add labels and title
	plt.title("Estimated Revenue of GTA Series")
	plt.xlabel("Game")
	plt.ylabel("Revenue (Billion USD)")
	plt.xticks(rotation=15)
	plt.tight_layout()
	filename = "matrix_analysis.png"
	plt.savefig(filename)

	print("Analysis complete!")
	print("Results saved to: matrix_analysis.png")

main()