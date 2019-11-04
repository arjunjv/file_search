#!/usr/bin/env python3

import os
import csv
import sys

# to read the path nad validate
def readPath():
	path = input("Enter the path for the project files : ")
	if (os.path.exists(path)):
		return path
	else:
		print("Path entered is invalid")
		sys.exit()
		



if __name__ == "__main__":
	path = readPath();
	print("path is :",path)
	fileName = input("Enter the name of file to store the list :")
	fileName = fileName + ".csv"
	fields = ["File Name"]
	
	#wite the files in given path recusively to a csv file
	with open(fileName, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(fields)
    
		for root, dirs, files in os.walk(path):
			for filename in files:
				writer.writerow([filename])


