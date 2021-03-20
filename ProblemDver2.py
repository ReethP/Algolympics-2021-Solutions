test = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
test2 = test.lower()
sort = []
sort2 = []
for i in test:
	sort.append(ord(i))

for i in test2:
	sort2.append(ord(i))
print(sorted(sort))
print(sorted(sort2))