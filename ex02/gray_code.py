def gray_code(nb: int):
	return nb ^ (nb >> 1)

def main():
	x = 0
	print(f"G({x}) = {gray_code(x)}")

	x = 1
	print(f"G({x}) = {gray_code(x)}")

	x = 2
	print(f"G({x}) = {gray_code(x)}")

	x = 3
	print(f"G({x}) = {gray_code(x)}")

	x = 4
	print(f"G({x}) = {gray_code(x)}")

	x = 5
	print(f"G({x}) = {gray_code(x)}")

	x = 6
	print(f"G({x}) = {gray_code(x)}")

	x = 7
	print(f"G({x}) = {gray_code(x)}")

	x = 8
	print(f"G({x}) = {gray_code(x)}")

if __name__ == "__main__":
	main()