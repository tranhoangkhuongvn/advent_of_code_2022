



if __name__ == '__main__':
	register_val = 1
	values = []
	cycle = 0
	new_val = None
	crt_cycle = 0
	crt_str = "" 
	CRT = []
	while True:
		try:
			line = list(input().split())
			print(line)
			
			if crt_cycle % 40 == 0:
				CRT.append(crt_str)
				crt_str = ""
				#crt_cycle = 0
			
			if len(line) == 2:
				ins, val = line
				val = int(val)
			else:
				ins = line[0]
			
			if ins == "noop":
				if len(values) == 0:
					values.append(1)
				else:
					if new_val is None:
						values.append(values[-1])
					else:
						values.append(new_val)
				cycle += 1
				new_val = None
			else:
				if new_val is None:
					if len(values) == 0:
						values.append(1)
					else:
						values.append(values[-1])	
				else:
					values.append(new_val)
				
				values.append(values[-1])	
				#values.append(new_val)
				new_val = values[-1] + val
				cycle += 2


			print(values)
			crt_pos = crt_cycle % 40
			if (crt_pos == values[crt_cycle]) or (crt_pos == values[crt_cycle]-1) or (crt_pos == values[crt_cycle]+1):
				crt_str += "#"
			else:
				crt_str += "."
			
			
			
			crt_cycle += 1
			
			
			print("crt cycle:", crt_cycle)
			#print(values)
			print(crt_str)
		except Exception as e:
			print(e.args)
			break

	while crt_cycle < 240:
		if crt_cycle % 40 == 0:
			CRT.append(crt_str)
			crt_str = ""
		crt_pos = crt_cycle % 40
		if (crt_pos == values[crt_cycle]) or (crt_pos == values[crt_cycle]-1) or (crt_pos == values[crt_cycle]+1):
			crt_str += "#"
		else:
			crt_str += "."
		
		crt_cycle += 1
		print("crt cycle:", crt_cycle)
		print(crt_str)

	CRT.append(crt_str)	
	print(new_val)
	print(values[20])
	print(values[60])
	print(values[100])
	print(values[140])
	print(values[180])
	print(values[220])


	print("total:", values[19] * 20 + values[59] * 60 + values[99] * 100 + values[139] * 140 +
					values[179]	* 180 + values[219] * 220)
	
	for row in CRT:
		print(row)
