def adder(a: int, b: int) -> int:
	if a < 0 or b < 0:
		print("Only naturel numbers!")
		return
	keep = (a & b) << 1
	res = a ^ b
	if keep == 0:
		return res
	return adder(keep, res)

def main():
	print(adder(5, 7))
	
if __name__ == "__main__":
	main()
