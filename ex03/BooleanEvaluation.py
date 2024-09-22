import sys

sys.path.append("../")
from cls.ASTNode import ASTNode

def compute(node: ASTNode):
	ops = {
			'&': lambda a, b: a & b,
			'|': lambda a, b: a | b,
			'=': lambda a, b: a == b,
			'^': lambda a, b: a ^ b,
			'>': lambda a, b: (a ^ True) | b,
			'!': lambda a: not a
		}
	if node.value not in ops:
		try:
			if node.value.isdigit():
				return bool(int(node.value))
			else:
				return node.value
		except ValueError:
			raise ValueError(f"Invalid Value: {node.value}")
	token_list = {"&": 2, "|": 2, "^": 2, ">": 2, "=": 2, "!": 1}
	if token_list[node.value] == 1:
		operand = compute(node.left)
		res = ops[node.value](operand)
	else:
		left = compute(node.left)
		right = compute(node.right)
		res = ops[node.value](left, right)
	return res

def eval_formula(expression: str) -> bool:
	AST = ASTNode(None)
	rootNode = AST.tree_generation(list(expression))
	return compute(rootNode)


def main():
	print(eval_formula("10&"))
	print(eval_formula("10|"))
	print(eval_formula("11>"))
	print(eval_formula("10="))
	print(eval_formula("1011||="))
	print(eval_formula("101|&"))
	print(eval_formula("01&!"))
	print(eval_formula("10|!"))
	return 0

if __name__ == "__main__":
	main()
