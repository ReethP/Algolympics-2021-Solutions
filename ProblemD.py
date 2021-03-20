cases = int(input())
for i in range(cases):
	safe = True
	characters = input()
	binary = input()
	unsafe = []
	for k in range(len(binary)):
		if(binary[k] == "1"):
			unsafe.append(k)
	for ind in unsafe:
		if(ind == 0):
			if ord(characters[ind+1]) <= 90:
				safe = False
				break
		elif(ind == 7):
			if ord(characters[ind-1]) <= 90:
				safe = False
				break
		else:
			if ord(characters[ind-1]) <= 90:
				safe = False
				break
			if ord(characters[ind+1]) <= 90:
				safe = False
				break
	if(safe):
		print("made some spaCe, welcome to the Bar!")
	else:
		print("not enough spaCe, please Bounce!")