def eval_formula(formula: str) -> bool:
	stack = []
	symbol = ["&", "|", "^", ">", "="]
	negation = False

	for element in formula:
		if element == ' ':
			continue
		if element == "!":
			if negation:
				negation = False
			else:
				negation = True
			continue
		if element in symbol:
			if len(stack) < 2:
				return "Error"
			nb2 = int(stack[-1])
			stack.pop()
			nb1 = int(stack[-1])
			stack.pop()
			match element:
				case "|":
					res = nb1 | nb2
				case "&":
					res = nb1 & nb2
				case "^":
					res = nb1 ^ nb2
				case ">":
					res = (nb1 ^ 1) | nb2
				case "=":
					res = nb1 == nb2
			stack.append(res)
		elif element == "0" or element == "1":
			if negation:
				stack.append(str(int(element) ^ 1))
				negation = False
			else:
				stack.append(element)
		else:
			return "Error"
	return stack[-1]
