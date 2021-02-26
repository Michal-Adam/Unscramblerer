import string
import sys

# Opening the file
with open("words_alpha.txt") as file:
    scrambledWord = input("Your scrambled word: ")
    print("Processing...")

    # Checking if the word has numbers or special characters
    for character in scrambledWord:
        if character not in string.ascii_letters:
            print("Unsupported character")
            sys.exit()

    # Writing the length and characters
    scrambledWordLength = len(scrambledWord)
    scrambledWordCharacters = []

    # Making a list of characters in the scrambled word
    for word in scrambledWord:
        scrambledWordCharacters.append(word)

    # Checking all word lengths for the same amount of characters
    unscrambledWord = []
    for line in file.readlines():
        if scrambledWordLength == len(line.rstrip('\n')):
            unscrambledWord.append(line)

    # Counting each character occurrence in the scrambled word
    characterCount = {}
    for character in scrambledWordCharacters:
        if character not in characterCount:
            characterCount[character] = 0
        if character in characterCount:
            characterCount[character] += 1
    for character in list(characterCount):
        if characterCount[character] < 2:
            characterCount.pop(character)

    # Checking similarity by every letter
    for character in scrambledWordCharacters:
        for word in unscrambledWord[:]:
            if character not in word:
                unscrambledWord.remove(word)
                pass

    # Checking for multiple character occurrences
    for word in unscrambledWord[:]:
        for letter in list(characterCount):
            if characterCount[letter] != word.count(letter):
                unscrambledWord.remove(word)
                break
            else:
                continue

    # Printing out the results
    print("The unscrambled words: ")
    print("".join(unscrambledWord))
