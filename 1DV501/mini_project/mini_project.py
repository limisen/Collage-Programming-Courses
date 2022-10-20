import os

# Part 1 -  Counting + unique words 1
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

def get_top_10_words(path, file_name):
    os.chdir(path)
    name = open(file_name, encoding='utf-8', mode="r")    # Opening the file
    content = name.read()               # Making the content into one long str
    #                                   # by reading the whole file directly
    name.close()                        # Closing the file
    #
    content = content.split("\n")        # Spliting into a list on given chr
    #
    content = [x.lower() for x in content if len(x) > 4]
    # Removing unwanted elements
    top_10 = {}
    for word in content:
        if word in top_10:
            top_10.update({word: 1 + top_10.get(word)})
        else:
            top_10.update({word: 1})
    
    # Counting the nr of occurenses and creates a dict out of it.
    top_10 = dict(sorted(top_10.items(), key=lambda item: item[1], reverse=True))
    # Sorts the dict so the 10 most frequent words come first in decending order
    top_10 = list(top_10.items())[:10]
    #
    return top_10                     # Returning the list of words


# input_file = 'assignment-03/data/swe_news_15226315_words.txt'
input_file = 'assignment-03/data/brian_13393_words.txt'
path = os.getcwd()

top_10_words = get_top_10_words(path, input_file)

print(f'nr of occurenses for unique words:')
for i in top_10_words:
    print(i)


# Part 2 -  Implementing data structures


# Part 3 -  Counting unique words 2


