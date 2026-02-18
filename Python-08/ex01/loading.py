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

	years = np.arange(2015, 2023)
	
	base_players = 8

	growth = np.linspace(0, 12, len(years))
	spikes = np.random.normal(0, 0.8, len(years))
	
	players = base_players + growth + spikes

	df = pd.DataFrame({
		"Year": years,
		"Active_Players_Millions":players
		})

	print(f"Processing {len(df)} data points...")

	print("Generating visualization...\n")

	plt.figure(figsize=(10, 6))
	plt.plot(df["Year"], df["Active_Players_Millions"], marker="o")
	plt.title("GTA V Active Players (2015-2026)")
	plt.xlabel("Year")
	plt.ylabel("Active Players (Millions)")
	plt.grid(True)

	filename = "matrix_analysis"
	plt.savefig(filename)

	print("Analysis complete!")
	print("Results saved to: matrix_analysis.png")

main()