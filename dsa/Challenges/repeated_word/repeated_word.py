# Write a function that accepts a lengthy string parameter.
# Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.
from collections import Counter

def repeated_word_return(string):
    new_string = string.lower()

    words = new_string.split(" ")

    for i in range(0, len(words)):
        count = 1
        for j in range(i+1,len(words)):
            if(words[i] == words[j]):
                count = count + 1
                words[j] = 0

        if(count > 1 and words[i] != 0):
            return words[i]


if __name__ == "__main__":
    string = "I love soda and soda loves me"
    print(repeated_word(string))
