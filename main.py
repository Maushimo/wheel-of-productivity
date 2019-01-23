#projects = ['Personal Website', 'ReactJS game', 'Crazy Taxi Clone', 'VN Review', 'Read/Write', 'New EP']

import random
import csv

projects = []

with open('projects.csv') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in csvReader:
		projects.append(row)


choice = input("PRODUCTIVITY WHEEL:\n [1] Spin the wheel\n [2] Add Items\n [3] Remove Items\n")

if choice == 1:
	random.shuffle(projects)
	garbageChars = "[',]" # string containing random characters that the thing prints for some reason
	print("Work on " + str(projects[0]).translate(None, garbageChars))
elif choice == 2:
	print("Implement feature")
elif choice == 3:
	print("Implement feature")
elif choice == 4:
	for i in range(len(projects)):
		print projects[i]