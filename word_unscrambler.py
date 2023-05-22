import itertools

FILE_NAME = "english_words.txt"


def main():
    # Read and store the clean words from the file
    try:
        with open(FILE_NAME) as f:
            clean_words = {line.strip() for line in f.readlines()}
    except IOError:
        print(f"Error: Unable to read the file {FILE_NAME}")
        return

    # Get the input from the user
    while True:
        word = input("Enter a word to unscramble: ")
        if word.isalpha():
            break
        print("Invalid input. The word should only contain alphabetic characters.")

    # Generate unique permutations of the input word
    unique_permutations = set(''.join(perm)
                              for perm in itertools.permutations(word))

    # Find unscrambled words from the permutations
    unscrambled_words = []

    for permutation in unique_permutations:
        if permutation in clean_words:
            unscrambled_words.append(permutation)

    # Print the unscrambled words
    print("Unscrambled words found:")
    if unscrambled_words:
        for word in unscrambled_words:
            print(word)
        print(f"Total unscrambled words found:{len(unscrambled_words)}\n")
    else:
        print("No unscrambled words found.\n")

    input("Press ENTER to exit...")


if __name__ == "__main__":
    main()
