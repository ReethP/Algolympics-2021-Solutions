ngredients = int(input())
budget = int(input())
grams = list(map(int,input().split()))
p = list(map(int,input().split()))
totalCost = 0
for i in range(len(grams)):
	totalCost+= (grams[i] * p[i])
servings = budget/totalCost
print(int(servings))