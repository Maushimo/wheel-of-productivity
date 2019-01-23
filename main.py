import random
import csv

def addProject():
	project = raw_input("What would you like to add?\n")

	with open('projects.csv', 'a') as csvFile:
		csvFile.write(",\n" + project)

	print("You have successfully added " + project)

projects = []

with open('projects.csv') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in csvReader:
		projects.append(row)


choice = input("PRODUCTIVITY WHEEL:\n [1] Spin the wheel\n [2] Add Items\n [3] Remove Items\n")

# SPIN
if choice == 1:
	random.shuffle(projects)
	garbageChars = "[',]" # string containing random characters that the thing prints for some reason
	print("Work on " + str(projects[0]).translate(None, garbageChars))
# ADD
elif choice == 2:
	addProject()
	#print("Implement feature")
# DELETE
elif choice == 3:
	print("Implement feature")
# PRINT (TEST)
elif choice == 4:
	for i in range(len(projects)):
		print projects[i]