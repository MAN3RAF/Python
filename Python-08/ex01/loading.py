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

	import matplotlib.pyplot as plt
	import pandas as pd
	import numpy as np


	if not check_all():
		sys.exit(1)

	print("\nAnalyzing Matrix data...")

	np.random.seed(1337)
	size = 1000

	time = np.arange(size)
	signal = np.sin(time *0.02) + np.random.normal(0, 0.5, size)

	df = pd.DataFrame({"time": time, "signal": signal})

	print(f"Processing {len(df)} data points...")
	plt.figure(figsize=(10, 5))
	plt.plot(df["time"], df["signal"], label="Matrix Signal")
	plt.title("Matrix Data Simulation")
	plt.xlabel("Time")
	plt.ylabel("Signal Strength")
	plt.legend()
	plt.tight_layout()
	plt.savefig("matrix_analysis.png")


main()