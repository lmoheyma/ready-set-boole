def adder(a: int, b: int) -> int:
	if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
		print("Only naturel numbers!")
		return
	keep = (a & b) << 1
	res = a ^ b
	if keep == 0:
		return res
	return adder(keep, res)

def multiplier(a: int, b: int) -> int:
	if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
		print("Only naturel numbers!")
		return
	res = 0
	for i in range(b):
		res = adder(res, a)
	return res

def main():
	x = 0
	y = 0
	print(f"{x} * {y} = {multiplier(x, y)}")

	x = 5
	y = 7 
	print(f"{x} * {y} = {multiplier(x, y)}")
	
	x = 101
	y = 101
	print(f"{x} * {y} = {multiplier(x, y)}")

	x = -5
	y = 7 
	print(f"{x} * {y} = {multiplier(x, y)}")

if __name__ == "__main__":
	main()
