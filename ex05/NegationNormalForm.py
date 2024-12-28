import sys

sys.path.append("../")
from cls.ASTNode import ASTNode

class NegationNormalForm:
	def __init__(self) -> None:
		self.NNF = ""

	def formulaToAST(self, formula: str) -> str:
		AST = ASTNode(None)
		rootNode = AST.tree_generation(list(formula))
		# if rootNode.value == "!":
		# 	for element in formula:
		# 		if element == "&":
		# 			NNF += "|"
		# 		elif element == "|":
		# 			NNF += "&"
		# 		else:
		# 			NNF += element + "!"	
		AST.print_tree(rootNode, 0)
		# rootNode = rootNode.left
		# AST.parsing(rootNode)
		# AST.print_tree(rootNode, 0)
		self.ASTToNNF(rootNode)
		print()

	def ASTToNNF(self, node):
		if node is not None:
			self.printNNF(node.right)
			self.NNF += node.value
			self.printNNF(node.left)


def main():
	def preEvaluating(formula: str):
		special_cases = {
			'AB>': 'A!B|',
			'AB=': 'AB&A!B!&|'
		}
		for case in special_cases:
			if case in formula:
				startIndex = formula.find(case)
				formula = formula[:startIndex] + special_cases[case] + formula[startIndex + 3:]
	# NNF = NegationNormalForm()
	# NNF.formulaToAST("AB&!")
	formula = 'AB&!'
	res = ''
	preEvaluating(formula)
	if formula[-1]:
		for element in formula:
			if element.isalpha():
				res.append(element + '!')

	# NegationNormalForm("A!B!&C!|")

if __name__ == "__main__":
	main()