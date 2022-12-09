from pprint import pprint


def rotate_left(matrix):
	num_row = len(matrix)
	num_col = len(matrix[0])
	new_matrix = [[0 for i in range(num_row)] for j in range(num_col)]
	for r in range(num_row):
		for c in range(num_col-1, -1, -1):
			new_matrix[num_col-1-c][r] = matrix[r][c]

	return new_matrix

def check_left_to_right(matrix, visible):
	num_row = len(matrix)
	num_col = len(matrix[0])
	for r in range(1, num_row-1):
		max_by_row = matrix[r][0]
		visible[r][0] = True
		for c in range(1, num_col):
			if matrix[r][c] > max_by_row:
				visible[r][c] = True
				max_by_row = matrix[r][c]
	return visible

if __name__ == "__main__":
	matrix = []
	while True:
		try:
			line = list(map(int, input()))
			matrix.append(line)
		except Exception as e:
			print(e.args)
			break
	
	num_col = len(matrix[0])
	num_row = len(matrix)
	
	visible = [[False for c in range(num_col)] for r in range(num_row)]
	visible[0] = [True for _ in range(num_col)]
	visible[-1] = [True for _ in range(num_col)]
	scenic_count = [[0 for c in range(num_col)] for r in range(num_row)]
	print("Round 1:")
	pprint(matrix)
	visible = check_left_to_right(matrix, visible)
	pprint(visible)
	print("-------------")
	print("Round 2:")
	new_matrix = rotate_left(matrix)
	visible = rotate_left(visible)
	pprint(new_matrix)
	visible = check_left_to_right(new_matrix, visible)
	pprint(visible)
	print("-------------")
	print("Round 3:")
	new_matrix = rotate_left(new_matrix)
	visible = rotate_left(visible)
	pprint(new_matrix)
	visible = check_left_to_right(new_matrix, visible)
	pprint(visible)
	print("-------------")
	print("Round 4:")
	new_matrix = rotate_left(new_matrix)
	visible = rotate_left(visible)
	pprint(new_matrix)
	visible = check_left_to_right(new_matrix, visible)

	print("Final:")
	pprint(rotate_left(new_matrix))
	pprint(rotate_left(visible))

	count = 0
	for r in range(num_row):
		for c in range(num_col):
			if visible[r][c] == True:
				count += 1

	print(count)

