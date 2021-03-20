old = int(input())
oldWords = {}

for i in range(old):
	note = input().lower().split()
	filteredNote = []
	for word in note:
		actualWord = "".join(filter(str.isalpha,word))
		try:
			oldWords[actualWord]+=1
		except:
			oldWords[actualWord] = 1

new = int(input())
for i in range(new):
	numNotes = int(input())
	# newWordList = {}
	numWords = 0
	inOld = 0
	for j in range(numNotes):
		note = input().lower().split()
		for word in note:
			numWords+=1
			newWord = "".join(filter(str.isalpha,word))
			try:
				oldWords[newWord]
				inOld+=1
			except:
				continue

	if inOld >= numWords/2:
		print("GOOD BOY!")
	else:
		print("BIG HANDS!")
