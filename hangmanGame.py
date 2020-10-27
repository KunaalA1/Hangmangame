import numpy
possibleWords = ["hello", "chocolate", "apple","orange","memelord", "pineapple", "papaya", "strawberry"]

def main():
	print("The game starts!")
	
	wordPick = numpy.random.randint(8)
		
	correctWord = possibleWords[wordPick]

	correctWordList = split(correctWord)
		
	tempWordList = ["_" for x in range(len(correctWord))]

	gameDone = False

	guesses = 10

	while(not gameDone and guesses > 0):

		guessCorrect = False

		letterGuess = str(input("What letter do you guess?"))

		for i in range(0,len(correctWordList)):
			
			if (letterGuess == correctWordList[i]):
				
				tempWordList[i] = letterGuess
				
				guessCorrect = True

		if(guessCorrect):
			
			print("Correct! You still have " + str(guesses) + " guesses")

		
		else:
			
			guesses -= 1
			
			print("Wrong! you still have " + str(guesses) + " guesses")
			
		
		tempWord = ""
		
		print(tempWord.join(tempWordList))
		
		gameDone = True

		for x in range(len(tempWordList)):

			if(tempWordList[x] == "_"):
				gameDone = False



def split(word):

	array = []

	for element in word:
		
		array.append(element)
	
	return array

if __name__ == '__main__':
	
	main()
