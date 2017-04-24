while True:
	try:
		x = int(input("Please enter anumber: "))
		break
	except ValueError:
		print("No")