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
	bigs = ['Big 1', 'Big 2', 'Big 3', 'Big 4', 'Big 5']
	littles = ['Little 1' ,'Little 2', 'Little 3', 'Little 4', 'Little 5']
	littlesPreferences = {
		'Little 1': ['Big 2', 'Big 3', 'Big 1', 'Big 4', 'Big 5'],
		'Little 2': ['Big 1', 'Big 2', 'Big 4', 'Big 3', 'Big 5'],
		'Little 3': ['Big 3', 'Big 1', 'Big 4', 'Big 2', 'Big 5'],
		'Little 4': ['Big 5', 'Big 1', 'Big 4', 'Big 2', 'Big 3'],
		'Little 5': ['Big 3', 'Big 5', 'Big 2', 'Big 1', 'Big 4']
	}
	bigsPreferences = {
		'Big 1': ['Little 2', 'Little 3', 'Little 5', 'Little 1', 'Little 4'],
		'Big 2': ['Little 3', 'Little 5', 'Little 4', 'Little 1', 'Little 2'],
		'Big 3': ['Little 1', 'Little 2', 'Little 4', 'Little 3', 'Little 5'],
		'Big 4': ['Little 3', 'Little 2', 'Little 4', 'Little 1', 'Little 5'],
		'Big 5': ['Little 1', 'Little 4', 'Little 2', 'Little 3', 'Little 5']
	}
	pairs = pairBigLittles(bigs, littles, bigsPreferences, littlesPreferences)
	print(pairs)
main()