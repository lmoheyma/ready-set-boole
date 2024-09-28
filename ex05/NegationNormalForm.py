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
		rootNode = rootNode.left
		AST.parsing(rootNode)
		# AST.print_tree(rootNode, 0)
		self.printNNF(rootNode)
		print()

	def printNNF(self, node):
		if node is not None:
			self.printNNF(node.right)
			self.NNF += node.value
			self.printNNF(node.left)


def main():
	NNF = NegationNormalForm()
	# NegationNormalForm("AB&!")
	NNF.formulaToAST("AB|C&!")
	NNF.NNF = NNF.NNF[::-1]
	for i in range(len(NNF.NNF)):
		if NNF.NNF[i].isalpha():
			NNF.NNF[i] = "!"
		elif NNF.NNF[i] == "!":
			
	# NegationNormalForm("A!B!&C!|")

if __name__ == "__main__":
	main()