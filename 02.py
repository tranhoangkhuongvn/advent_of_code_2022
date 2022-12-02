


if __name__ == '__main__':
	score = 0
	game_dict_part1 = {
		"A": "Rock",
		"X": "Rock",
		"B": "Paper",
		"Y": "Paper",
		"C": "Scissors",
		"Z": "Scissors"
	}	

	game_dict_part2 = {
		"X": 1,
		"Y": 0, 
		"Z": -1
	}
	
	arr = ["Rock", "Scissors", "Paper"]
	score_dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
	while True:
		try:
			a, b = list(map(str, input().split()))	
			print(a, b)	
			# part 1:	
			# a = game_dict[a]
			# b = game_dict[b]
			# part 2:
			a = game_dict_part1[a]
			b_score = game_dict_part2[b]
			idx_a = arr.index(a)
			idx_b = (idx_a + b_score) % 3
				
			if b == "X":
				score += 0
			elif b == "Y":
				score += 3
			elif b == "Z":
				score += 6
			else:
				print("Wrong input")
				break
			score += score_dict[arr[idx_b]]
			"""	
			# part 1
			if a != b:
				idx_a = arr.index(a)
				idx_b = arr.index(b)
				if (idx_a + 1) % 3 == idx_b:
					# we lost
					score += 0
				else:
					# we win
					score += 6
			else: # draw
				score += 3		
			score += score_dict[b]
			"""
		except Exception as e:
			print(e.args)
			break
	
	print(score)

