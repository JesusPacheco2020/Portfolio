#Extra Credit Program
#This program separates the User's sentence into individual words, and counts the number of letters in each word.

#Program Greeting
print("\n\nWelcome!")
      
#Get Sentence from User
print("\nPlease enter your Sentence:")
Sentence = input()


#Create an empty List of Strings
Words = ['']

#Separate the User's sentence into a List of each word
k = 0
wordnum = 0

while k < len(Sentence):    #Go through every character in the User's sentence.
    if Sentence[k] != ' ' and Sentence[k] != '.' and Sentence[k] != '?' and Sentence[k] != '!':  #If the character is not a space/punctuation mark, 
        Words[wordnum] = Words[wordnum] + Sentence[k]   #then add the character to the word
        k = k + 1
    else:
        #If the character is a space/punctuation mark,
        if Sentence[k] == ' ' or Sentence[k] == '.' or Sentence[k] == '?' or Sentence[k] == '!':
            if k < len(Sentence) - 1:   #and if it is NOT the last character
                Words.append('')        #then start a new word
                wordnum = wordnum + 1
                k = k + 1
            else:   #If the character is a space/punctuation mark and IS the last character in the sentence then stop
                break   
           
#Display the List of words.
print("\nWord=", Words)


#Create a List of number of letters in each word.
LetterCount = []
for i in range(wordnum + 1):
    LetterCount.append(len(Words[i]))

#Display the List of number of letters in each word.
print("\nLetterCount =", LetterCount )
