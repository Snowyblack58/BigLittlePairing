from openpyxl import load_workbook

def getCellName(row, col):
	alpha = ''
	while col > 0:
		d = int(col % 26)
		if d == 0:
			d = 26
		col -= d
		alpha = str(chr(65+d-1)) + alpha
		col = col / 26
	return alpha + str(row)

def grabListsFromSheet(sheet):
	persons = []
	prefs = {}
	row = 1
	while sheet[getCellName(row, 1)].value != None:
		person = sheet[getCellName(row, 1)].value
		persons.append(person)
		prefs[person] = []
		col = 2
		while sheet[getCellName(row, col)].value != None:
			prefs[person].append(sheet[getCellName(row, col)].value)
			col += 1
		row += 1
	return persons, prefs

def completePreferences(prefs, prefValues):
	for person in prefs:
		for prefValue in prefValues:
			if prefValue not in prefs[person]:
				prefs[person].append(prefValue)
	return prefs

def initializeLists():
	wb = load_workbook('biglittlepreferences.xlsx')
	bigs, bigsPreferences = grabListsFromSheet(wb.worksheets[0])
	littles, littlesPreferences = grabListsFromSheet(wb.worksheets[1])
	bigsPreferences = completePreferences(bigsPreferences, littles)
	littlesPreferences = completePreferences(littlesPreferences, bigs)
	return bigs, littles, bigsPreferences, littlesPreferences

'''
Initializes dictionaries with the list as the keys and boolean Falses as the values
'''
def convertListToDict(list):
	toDict = {}
	for el in list:
		toDict[el] = False
	return toDict

'''
Returns the pair with the person
'''
def pairWith(pairs, person):
	for pair in pairs:
		if person in pair:
			return pair
	assert 'Pair not found'

'''
Uses the Gale-Shapley algorithm to pair up bigs and littles based upon their preferences
A big and a little cannot be paired with another respective little or big if they prefer each other.
'''
def pairBigLittles(bigs, littles, bigsPreferences, littlesPreferences):
	pairs = []
	bigsDict = convertListToDict(bigs)
	littlesDict = convertListToDict(littles)
	#Bigs propose to their top little
	for big in bigsDict:
		little = bigsPreferences[big].pop(0)
		print('Looking at ' + big + ' who prefers ' + little)
		#Littles only accept proposal if from top bigs
		print(big + ' =?= ' + littlesPreferences[little][0])
		if big == littlesPreferences[little][0]:
			pairs.append([big, little])
			bigsDict[big] = True
			littlesDict[little] = True
	#while any bigs don't have a little
	while False in bigsDict.values():
		for big in bigsDict:
			#skip bigs that already have littles
			if bigsDict[big]:
				continue
			little = bigsPreferences[big].pop(0)
			print('Looking at ' + big + ' who next prefers ' + little)
			#if little does not have a big, pair big/little
			if not littlesDict[little]:
				print(big + ' and ' + little + ' were paired because they were previously unpaired')
				bigsDict[big] = True
				littlesDict[little] = True
				pairs.append([big, little])
			#if little does have a big but prefers this new big, remove old pair and pair big/little
			else:
				otherPair = pairWith(pairs, little)
				if littlesPreferences[little].index(big) < littlesPreferences[little].index(otherPair[0]):
					print(big + ' and ' + little + ' were paired because little prefers new big')
					bigsDict[otherPair[0]] = False
					bigsDict[big] = True
					littlesDict[little] = True #should be redundant
					pairs.remove(otherPair)
					pairs.append([big, little])
				else:
					print(big + ' and ' + little + ' were not paired because little prefers current big')
	return pairs

def main():
	bigs, littles, bigsPreferences, littlesPreferences = initializeLists()
	pairs = pairBigLittles(bigs, littles, bigsPreferences, littlesPreferences)
	print(pairs)
main()