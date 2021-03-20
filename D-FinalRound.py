def check_right(diagram, tRow, tCol, cRow, cCol):
	if(cCol == tCol-1 or cCol == tCol-2):
		return 0
	connected = 0
	for i in range(cCol+1,tCol):
		if(diagram[cRow][i].isalnum()):
			if(i == cCol+1):
				return 0
			if(connected == 1):
				return i
		else:
			if diagram[cRow][i] == "|":
				return 0
			else:
				connected = 1
	return 0

def check_down(transpose, diagram, tRow, tCol, cRow, cCol):
	if(cRow == tRow-1 or cRow == tRow-2):
		return 0
	connected = 0
	for i in range(cRow+1,tRow):
		if(transposed[cCol][i].isalnum()):
			if(i == cRow+1):
				return 0
			if(connected == 1):
				return i
		else:
			if transposed[cCol][i] == "-":
				return 0
			else:
				connected = 1
	return 0


def check_connected_row(diagram, tRow, tCol, cRow, cCol):
	right = check_right(diagram, tRow, tCol, cRow, cCol)
	if(right):
		return right
	return 0

def check_connected_col(transpose, diagram, tRow, tCol, cRow, cCol):
	down = check_down(transpose, diagram, tRow, tCol, cRow, cCol)
	if(down):
		return down
	return 0

def transpose(input_arr,r,c):
	transposed = [[0 for i in range(r)] for i in range(c)]
	for i in range(c):
		for j in range(r):
			transposed[i][j] = input_arr[j][i]
	return transposed

cases = int(input())
for iteration in range(cases):
	r,c = list(map(int,input().split()))
	diagram = []
	for per_line in range(r):
		line = input()
		diagram.append(line)
	transposed = transpose(diagram,r,c)
	connected = []
	connected_out = []
	not_connected = []

	for row in range(r):
		for col in range(c):
			if(diagram[row][col].isalnum() and diagram[row][col] not in connected):

				row_connect = check_connected_row(diagram, r, c, row, col)
				if(row_connect != 0):
					connected.append(diagram[row][col])
					connected.append(diagram[row][row_connect])
					ans = []
					ans.append(diagram[row][col])
					ans.append(diagram[row][row_connect])
					ans.sort()
					connected_out.append("".join(ans))
					continue
				col_connect = check_connected_col(transposed,diagram, r, c, row, col)
				if(col_connect != 0):
					connected.append(diagram[row][col])
					connected.append(diagram[col_connect][col])
					ans = []
					ans.append(diagram[row][col])
					ans.append(diagram[col_connect][col])
					connected_out.append("".join(ans))
					continue
				not_connected.append(diagram[row][col])
	print(len(not_connected))
	if(len(not_connected) != 0):
		print(" ".join(not_connected))
	print(len(connected_out))
	print(" ".join(connected_out))
