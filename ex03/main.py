from RPN import eval_formula

def main():
	print(eval_formula("10&"))
	print(eval_formula("10|"))
	print(eval_formula("11>"))
	print(eval_formula("10="))
	print(eval_formula("1011||="))
	print(eval_formula("101|&"))
	print(eval_formula("!01&"))
	print(eval_formula("!10|"))
	return 0

if __name__ == "__main__":
	main()