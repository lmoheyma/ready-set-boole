class ASTNode:
	def __init__(self, root_value) -> None:
		self.value = root_value
		self.left = None
		self.right = None


	def tree_generation(self, expression: list):
		token_list = {"&": 2, "|": 2, "^": 2, ">": 2, "=": 2, "!": 1}
		stack = []
		for token in expression:
			if token not in token_list:
				node = ASTNode(token)
				stack.append(node)
			else:
				arity = token_list[token]
				if len(stack) < arity:
					print("Stack Error")
					exit(1)
				operator = ASTNode(token)
				if arity == 1:
					operand = stack.pop()
					operator.left = operand
				else:
					right = stack.pop()
					left = stack.pop()
					operator.left = left
					operator.right = right
				stack.append(operator)
		if len(stack) != 1:
			print("Too Small Stack")
			exit(1)
		return stack[0]

	def parsing(self, node):
		if node is not None:
			self.parsing(node.right)
			if node.value == "&":
				node.value = "|"
			elif node.value == "|":
				node.value = "&"
			if node.value.isalpha():
				node.value += "!"
			self.parsing(node.left)


	def print_tree(self, node, level=0):
		if node is not None:
			self.print_tree(node.right, level + 1)
			print('    ' * level + f'-> {node.value}')
			self.print_tree(node.left, level + 1)


if __name__ == "__main__":
	expression = list("10|")
	AST = ASTNode(None)
	rootNode = AST.tree_generation(expression)
	AST.print_tree(rootNode)
	print(AST.tree_computation(rootNode))
	# binary_tree.print_tree()