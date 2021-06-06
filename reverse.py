# creates a program to reverse a sentence
def reverse(sentence):
    # removes the period from the sentence
    newsentence = sentence.replace(".", "")
    # splits all of the words by finding the space
    words = newsentence.split(" ")
    # connects all of these words in reversed order
    connect = " ".join(reversed(words))
    # adds a period to the end of the sentence
    return connect + "."

