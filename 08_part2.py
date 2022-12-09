from pprint import pprint


def rotate_left(matrix):
	num_row = len(matrix)
	num_col = len(matrix[0])
	new_matrix = [[0 for i in range(num_row)] for j in range(num_col)]
	for r in range(num_row):
		for c in range(num_col-1, -1, -1):
			new_matrix[num_col-1-c][r] = matrix[r][c]

	return new_matrix

def check_left_to_right(matrix, visible, scenic_count):
	num_row = len(matrix)
	num_col = len(matrix[0])
	for r in range(1, num_row-1):
		max_by_row = matrix[r][0]
		prev_val = matrix[r][0]
		visible[r][0] = True
		count = 0
		for c in range(1, num_col):
			if matrix[r][c] > prev_val:
				count += 1
				prev_val = matrix[r][c]
			if matrix[r][c] > max_by_row:
				visible[r][c] = True
				max_by_row = matrix[r][c]
				
				
			
				
	return visible, scenic_count

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
	
	dx = [1,0,-1,0]
	dy = [0,1,0,-1]

	pprint(matrix)
	scenic_count = [[1 for c in range(num_col)] for r in range(num_row)]

	for r in range(1,num_row-1):
		for c in range(1,num_col-1):
			print(r, c, matrix[r][c])
			for i in range(4):
				dr = r
				dc = c
				temp_count = 0
				while (0 < dr < num_row-1) and (0 < dc < num_col-1):
					dr += dy[i]
					dc += dx[i]
					temp_count += 1
					if matrix[dr][dc] >= matrix[r][c]:
						break
				scenic_count[r][c] *= temp_count

	max_view = 0
	for r in range(num_row):
		for c in range(num_col):
			if scenic_count[r][c] > max_view:
				max_view = scenic_count[r][c]
	
	pprint(max_view)
					



	