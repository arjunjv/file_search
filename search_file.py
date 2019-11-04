#!/usr/bin/env python3

import os
import csv
import sys
import socket

# search recusively where the file is existing 
def findAll(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

#read the search path from user
def readPath():
    path = input("Enter the path to search: ")

    if (os.path.exists(path)):
        return path
    else:
        print("Path entered is invalid")
        sys.exit()

#read teh file name from user
def readFileName():
    fileName = input("Enter the name to get the list to search :")
    if (os.path.isfile(fileName)):
        return fileName
    else:
        print("File name entered is not available")
        sys.exit()

#read the list of files from the given csv file
def readListOfFiles(fileName):
	fileList = [] 
	with open(fileName, 'r') as csvfile: 
		csvreader = csv.reader(csvfile) 
		next(csvreader)
  
		for row in csvreader: 
			fileList.append(row) 
		return fileList
	
#read teh username and IP Address
def getHostnameAndIP(): 
	hostName = socket.gethostname()
	hostIp = socket.gethostbyname(hostName)
	outputFile = hostName+str(hostIp)
	return outputFile
		


if __name__ == "__main__":
	
	fileName = readFileName()
	fileList = readListOfFiles(fileName)
	path = readPath()
	newList = []
	
	outputFile = getHostnameAndIP()
	outputFile = outputFile + ".csv"

	print("Output file is :",outputFile)

	# working loop to write the locations of files into csv file
	with open(outputFile, 'w') as csvfile:
		writer = csv.writer(csvfile)
		for subList in fileList:
			for item in subList:
				newList.append(item)
				locations = findAll(item, path)
				writer.writerow([item])
				if (locations):
					for location in locations:
						writer.writerow([location])
				else:
					writer.writerow([])
				writer.writerow([])




				

			
		



