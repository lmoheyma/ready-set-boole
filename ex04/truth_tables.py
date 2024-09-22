import itertools
import sys

sys.path.append("../")
from ex03.BooleanEvaluation import eval_formula

def print_truth_table(formula: str) -> None:
	counter = 0
	letters = []
	for i in range(len(formula)):
		if (formula[i] >= "A" and formula[i] <= "Z"):
			counter += 1
			letters.append(formula[i])
			for j in range(i + 1, len(formula)):
				if formula[i] == formula[j]:
					print("Error")
					return
	combinations = list(itertools.product([0, 1], repeat=counter))
	for letter in letters:
		print(f"| {letter}", end=" ")
	print("| = |")
	for _ in letters:
		print("|---", end="")
	print("|---|")
	for k in range(len(combinations)):
		l = 0
		new_formula = ""
		for element in formula:
			if (element >= "A" and element <= "Z"):
				new_formula += str(combinations[k][l])
				l+=1
			else:
				new_formula += element
		for value in combinations[k]:
			print(f"| {value} ", end="")
		print(f"| {int(eval_formula(new_formula))} |")
