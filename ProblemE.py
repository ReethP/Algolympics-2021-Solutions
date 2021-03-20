inputs = int(input())
for i in range(inputs):
	newPeople = []
	people = list(input())
	wordList = []
	word = ""
	for j in people:
		if j == " ":
			wordList.append(word)
			wordList.append(j)
			word = ""
		else:
			word+=j
	wordList.append(word)
	for group in wordList:
		if(group.islower()):
			newPeople.append(group)
		else:
			newPeople.append(group.upper())
	print("".join(newPeople))
