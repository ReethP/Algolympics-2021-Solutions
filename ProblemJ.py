cases = int(input())
for i in range(cases):
	stars = int(input())
	initial = list(map(int,input().split()))
	final = list(map(int,input().split()))
	last = initial[len(initial)-1]
	print(initial.index(last) - final.index(last))