import random
import csv
import os

# FUNCTIONS
def addProject():
	project = raw_input("What would you like to add?\n")

	with open('projects.csv', 'a') as csvFile:
		csvFile.write(",\n" + project)

	print("You have successfully added " + project)

def remProject(projects):
	# empty string to put the list of projects in
	projectList = ""
	for i in range(len(projects)):
		projectList += ("[" + str(i) + "]" + str(projects[i]) + "\n")

	garbageChars = "'," # string containing random characters that the thing prints for some reason
	#print("You can remove the following:\n\n" + projectList.translate(None, garbageChars) + "\n")
	choice = input("Which project do you want to remove?\n" + projectList.translate(None, garbageChars) + "\n")
	
	# remove project
	projects.pop(choice)
	
	# fill new list
	for i in range(len(projects)):
		projectList += ("[" + str(i) + "]" + str(projects[i]) + "\n")
	print(projectList.translate(None, garbageChars))

	with open('projects.csv', 'w+') as csvFile:
		fileWriter = csv.writer(csvFile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
		for i in range(len(projects)):
			fileWriter.writerow([projects[i]])


# MAIN BIT
if os.path.exists('./projects.csv'):
	projects = []
	with open('projects.csv') as csvFile:
		csvReader = csv.reader(csvFile, delimiter=',')
		for row in csvReader:
			projects.append(row)

	# Make the choice
	choice = input("PRODUCTIVITY WHEEL:\n [1] Spin the wheel\n [2] Add Items\n [3] Remove Items\n")
	# SPIN
	if choice == 1:
		random.shuffle(projects)
		garbageChars = "[',]" # string containing random characters that the thing prints for some reason
		print("Work on " + str(projects[0]).translate(None, garbageChars))
	# ADD
	elif choice == 2:
		addProject()
	# DELETE
	elif choice == 3:
		remProject(projects)
		#print("Implement feature")
	# PRINT (TEST)
	elif choice == 4:
		for i in range(len(projects)):
			print(projects[i])
	else:
		print("Invalid input")
else:
	print("Unable to locate 'projects.csv' file")