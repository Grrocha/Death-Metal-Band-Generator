import pandas as pd
import numpy as np
import math
import nltk
df = pd.read_csv("bands.csv", delimiter=';', encoding="utf-8-sig")
print(df.ix[:,'name'])
global DfLength
DfLength = len(df) + 1
global Complementaries
Complementaries = ["Of the", "From", "Of"]
def GetName():
	namestring = ""
	NameLen = math.floor(np.random.random()*10)
	for i in range(0, NameLen):
		RandomCell = math.floor(np.random.random()*(DfLength))
		print(df.ix[RandomCell,'name'])
		Name = df.ix[RandomCell,'name']
		PossibleWords = nltk.tokenize.word_tokenize(Name)
		print(PossibleWords)
		print(i)
		if i%2 == 0 and i != 0 and i != NameLen-1:
			namestring = namestring + " " + np.random.choice(Complementaries)
		else:
			namestring = namestring + " " + np.random.choice(PossibleWords)
	print(namestring)

GetName()