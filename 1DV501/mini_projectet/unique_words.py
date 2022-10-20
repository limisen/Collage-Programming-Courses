# Quack
import os


def get_unique_words(path, file_name):
    os.chdir(path)
    name = open(file_name, encoding='utf-8', mode="r")    # Opening the file
    content = name.read()               # Making the content into one long str
    #                                   # by reading the whole file directly
    name.close()                        # Closing the file
    #
    content = content.split("\n")        # Spliting into a list on given chr
    #
    content = {x for x in content if x.strip()}
    # Removing unwanted elements
    #
    return content                     # Returning the list of words


# input_file = 'assignment-03/data/brian_13393_words.txt'
input_file = 'assignment-03/data/swe_news_15226315_words.txt'
path = os.getcwd()

words = get_unique_words(path, input_file)

print('nr of unique words', len(words))
