
def classification(inputSentence, word):
	if "de" in word or "het" in word or "dat" in word or "en" in word or "een" in word or "voor" in word or "van" in word or "welke" in word or "te" in word or "hij" in word or "zij" in word or "op" in word or "ik" in word or "bij" in word:
		if "come" in word or "a" in word:
			return 'ITALIAN'
		else:
			if "aa" in inputSentence or "ee" in inputSentence or "ii" in inputSentence or "uu" in inputSentence:
				if inputSentence.count("i") >= 11:
					return 'DUTCH'
				else:
					if inputSentence.count("i") >= 11:
						return 'ITALIAN'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'DUTCH'
			else:
				if "the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word:
					if "is" in word or "of" in word or "was" in word or "all" in word:
						return 'DUTCH'
					else:
						if inputSentence.count("i") >= 11:
							return 'DUTCH'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'DUTCH'
				else:
					if inputSentence.count("i") >= 11:
						return 'DUTCH'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'DUTCH'
	else:
		if "che" in word or "il" in word or "ll" in word or "e" in word or "un" in word or "di" in word or "per" in word or "era" in word:
			if "the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word:
				if "is" in word or "of" in word or "was" in word or "all" in word:
					if "come" in word or "a" in word:
						return 'ITALIAN'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
				else:
					if inputSentence.count("i") >= 11:
						if inputSentence.count("i") >= 11:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
						else:
							return 'ITALIAN'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
			else:
				if inputSentence.count("i") >= 11:
					if inputSentence.count("i") >= 11:
						if inputSentence.count("i") >= 11:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
						else:
							return 'ITALIAN'
					else:
						return 'ITALIAN'
				else:
					if inputSentence.count("i") >= 11:
						return 'ITALIAN'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
		else:
			if "si" in word or "le" in word or "ma" in word or "la" in word or "mi" in word or "se" in word:
				if inputSentence.count("i") >= 11:
					return 'ITALIAN'
				else:
					if inputSentence.count("i") >= 11:
						return 'ITALIAN'
					else:
						if inputSentence.count("i") >= 11:
							return 'ITALIAN'
						else:
							if inputSentence.count("i") >= 11:
								return 'ITALIAN'
							else:
								return 'ITALIAN'
			else:
				if "à" in inputSentence or "è" in inputSentence or "ì" in inputSentence or "ò" in inputSentence or "ù" in inputSentence:
					return 'ITALIAN'
				else:
					if "ijk" in inputSentence or "sch" in inputSentence or "ijn" in inputSentence:
						if "aa" in inputSentence or "ee" in inputSentence or "ii" in inputSentence or "uu" in inputSentence:
							return 'DUTCH'
						else:
							return 'DUTCH'
					else:
						if ("l'") in inputSentence or ("d'") in inputSentence:
							return 'ITALIAN'
						else:
							if "the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word:
								return 'ENGLISH'
							else:
								return 'ENGLISH'

if __name__ == "__main__":
    inputSentence = input("Enter the sentence you want to predict")
    wordArray = inputSentence.split()
    results = classification(inputSentence, wordArray)
    print(results)
