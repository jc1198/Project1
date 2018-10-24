import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	f = open(file,'r')
	lines = f.readlines()
	headings = lines[0].split(',')
	# divy = lines[1:].split(',')
	# print(divy)
	dictList = []
	for x in lines[1:]:
		d = {}
		values = x.split(',')
		first = values[0]
		last = values[1]
		email = values[2]
		year = values[3]
		dob = values[4][:-1]
		d[headings[0]] = first
		d[headings[1]] = last
		d[headings[2]] = email
		d[headings[3]] = year
		d[headings[4][:-1]] = dob
		dictList.append(d)
	# print(dictList)
	return dictList



test = getData('P1DataA.csv')

# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows



def mySort(data,col):


# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	pass


def classSizes(data):
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	counts = []
	for dic in data:
		year = dic['Class']
		if dic['Class'] == 'Freshman':
			freshman += 1
			fresh_tuple = (year,freshman)
		elif dic['Class'] == "Sophomore":
			sophomore += 1
			soph_tuple = (year,sophomore)
		elif dic['Class'] == "Junior":
			junior += 1
			junior_tuple = (year,junior)
		elif dic['Class'] == 'Senior':
			senior += 1
			senior_tuple = (year,senior)
	counts.append(fresh_tuple)
	counts.append(soph_tuple)
	counts.append(junior_tuple)
	counts.append(senior_tuple)
	counts = sorted(counts, key = lambda x: x[1], reverse = True)
	return counts



# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]


def findMonth(a):
	d = {}
	count = 0
	for x in range(13):
		d[x] = 0
	for dic in a:
		DOB = dic['DOB']
		divy = DOB.split('/')
		month = int(divy[0])
		if month not in d.keys():
			d[month]== 1
		else:
			d[month]+= 1
		# count+=1
		# d[month] == count
	high_month = max(d, key = d.get)
	# print(high_month,d[high_month])
	return high_month
	# for x in d.values():
	# 	max = 0
	# 	if x>max:
	# 		max == x
	# 	else:
	# 		max = 0
	# print(max)
		# max = x.values()
		# if x.values()>max:
		# 	max = x.values()
		# print(max)
	# print(d)

findMonth(test)
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data



def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	current_date = '10/23/2018'
	s = current_date.split('/')
	c_month = int(s[0])
	c_day = int(s[1])
	c_year = int(s[2])
	ages = []
	for x in a:
		DOB = x['DOB']
		divy = DOB.split('/')
		month = int(divy[0])
		day = int(divy[1])
		year = int(divy[2])
		# take total days alive/365 and add to list
		years = (c_year - year)
		months = (c_month - month)
		days = (c_day - day)
		age = round((years*365 + months*30.416667 + days)/365)
		ages.append(age)
	# print(ages)
	avg = sum(ages)/len(ages)
	avg_rounded = round(avg)
	return avg_rounded



# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
