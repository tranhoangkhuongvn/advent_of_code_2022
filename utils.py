from typing import *
import re

def map_tuple(func, sequence):
	
	return tuple(map(func, sequence))


def find_int(text):
	"""
	return a tuple of all the numeric characters in the text
	"""
	return map_tuple(int, re.findall(r'-?[0-9]+', text))


if __name__ == "__main__":
	
	# test find_int
	test1 = "324asdb $234r 2i@3431-454--454"
	print(f"Test 1: {test1}")
	result1 = find_int(test1)
	print(f"Result 1: {result1}")
	print("-"*20)
	test2 = ["a1", "b445-45@", "c-3i2345vds5"]
	result2 = map_tuple(find_int, test2)	
	print(f"Test 2: {test2}")
	print(f"Result 2: {result2}")
	print("-"*20)

