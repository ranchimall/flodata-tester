import re
import testcases

marker=None
operation=None
address=None
amount=None

def extractMarkers(text, markerList):
	count = 0
	returnval = None
	text = text.lower()
	for marker in markerList:
		if marker[-1] != '#':
			marker = marker + '#'
		marker = marker.lower()

		count = count + text.count(marker)
		if count > 1:
			return 'od'
		if count == 1 and (returnval is None):
			returnval = marker
	return returnval


def extractOperation(text, operationList):
	count = 0
	returnval = None
	text = text.lower()
	for operation in operationList:
		operation = operation.lower()

		count = count + text.count(operation)
		if count > 1:
			return 'od'
		if count == 1 and (returnval is None):
			returnval = operation
	return returnval


def extractAmount(text):
	count = 0
	returnval = None
	text = text.lower()
	splitText = re.split("\W+", text)

	for word in splitText:
		word = word.replace('rmt','')
		try:
		    float(word)
		    count = count + 1
		    returnval = float(word)
		except ValueError:
			pass

		if count > 1:
			return 'od'
	return returnval

# Combine test
operationList = ['send','transfer','give']
markerList = ['ranchimall','rmt']
for string in testcases.testStrings:
	marker = extractOperation(string, markerList)
	operation = extractOperation(string, operationList)
	amount = extractAmount(string)

	print('text - ' + string)
	print('Marker - '+str(marker))
	print('Operation - '+str(operation))
	print('Amount - '+str(amount)+'\n\n')


# Marker test
'''markerList = ['ranchimall','rmt']
for string in testcases.testStrings:
	returnval = extractMarkers(string, markerList)
	if returnval is not None:
		if returnval == 'od':
			print('text - ' + string)
			print('Transaction reject\nMore than one marker present\n\n')
		else:
			print('text - ' + string)
			print('Marker - '+str(returnval)+'\n\n')
	else:
		print('text - ' + string)
		print('Marker not found\n\n')

# Operator test
operationList = ['send','transfer','give']
for string in testcases.testStrings:
	returnval = extractOperation(string, operationList)
	if returnval is not None:
		if returnval == 'od':
			print('text - ' + string)
			print('Transaction reject\nMore than one operation present\n\n')
		else:
			print('text - ' + string)
			print('Operation - '+str(returnval)+'\n\n')
	else:
		print('text - ' + string)
		print('Operation not found\n\n')'''


'''
GRAVEYARD
----------

def extractAddress(text):
	count = 0
	returnval = None

	for operation in operationList:
		operation = operation.lower()

		count = count + text.count(operation)
		if count > 1:
			return 'od'
		if count == 1 and (returnval is None):
			returnval = operation
	return returnval'''
