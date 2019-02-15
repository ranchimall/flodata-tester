import re
import testcases

marker=None
operation=None
address=None
amount=None

def extractMarkers(text):
    returnval = None
    text = text.lower()
    text = ' '.join(text.split())
    textlst = text.split(' ')

    for part in textlst:
        if part[-1] == '#' and len(part)>1:
            if returnval is not None:
                return 'od'
            returnval = part
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
        word = word.replace('rmt', '')
        try:
            float(word)
            count = count + 1
            returnval = float(word)
        except ValueError:
            pass

        if count > 1:
            return 'od'
    return returnval

def isIncorp(text):
    wordlist = ['incorporate','create','start']
    cleantext = re.sub(' +', ' ',text)
    textList = cleantext.split(' ')
    for word in wordlist:
        if word in textList:
            return True
    return False

def extractIncMarker(text):
    cleantext = re.sub(' +', ' ',text)
    textList = cleantext.split(' ')
    for word in textList:
        if word[-1] == '#':
            return word
    return False

def extractInitTokens(text):
    base_units = {'thousand':10**3 , 'million':10**6 ,'billion':10**9, 'trillion':10**12}
    cleantext = re.sub(' +', ' ',text)
    textList = cleantext.split(' ')
    for idx,word in enumerate(textList):
        try:
            result = float(word)
            if textList[idx+1] in base_units:
                return result*base_units[textList[idx+1]]
            return res
        except:
            continue

# Combine test
def parse_flodata(string):

    if not isIncorp(string):
        operationList = ['send', 'transfer', 'give']
        marker = extractMarkers(string)
        operation = extractOperation(string, operationList)
        amount = extractAmount(string)
        parsed_data = {'type': 'transfer', 'flodata': string, 'marker': marker, 'operation': operation,
                       'amount': amount}
    else:
        incMarker = extractIncMarker(string)
        initTokens = extractInitTokens(string)
        parsed_data = {'type': 'incorporation', 'flodata': string, 'marker': marker, 'initTokens': initTokens}

    return parsed_data
