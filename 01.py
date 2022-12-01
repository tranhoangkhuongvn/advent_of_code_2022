


if __name__ == '__main__':
	max_so_far = 0
	current_sum = 0	
	total = []
	while True:
		try:		
			line = input()
			if line == "":
				if current_sum > max_so_far:
					max_so_far = current_sum
				total.append(current_sum)
				current_sum = 0
			else:
				cal = int(line)
				current_sum += cal
		except:
			break

	total = sorted(total)
	
	print(max_so_far)
	print(sum(total[-3:]))

