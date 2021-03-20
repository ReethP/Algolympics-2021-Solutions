meetings = int(input())
for i in range(meetings):
	attendees = int(input())
	aList = []

	for k in range(attendees):
		aList.append(input())
	present = int(input())
	pList = []

	for l in range(present):
		pList.append(input())
	countedAttendees = 0
	stopp = 0

	for p in range(len(pList)):
		if pList[p] in aList:
			countedAttendees+=1
		else:
			print("STAR STREAM HACKED!!!")
			stopp = 1
			break
	if stopp:
		break
	half = 0
	a = len(aList)
	if a % 2 == 0:
		half = a / 2
	else:
		half = a // 2 + 1
	if countedAttendees >= half:
		print("START THE MEETING.")
	else:
		print("NO STARS IN THE NIGHT SKY.")