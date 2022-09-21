# Sentence builder, Builds a sentence using three functions that randomly
# pick a word out of 3 set lists of pronouns, verbs andn nouns.
# then prints the sentence ten times
from random import randrange


def pronoun():
    pron = ["I ", "You ", "It ", "We ", "They ", "He ", "She "]
    x = randrange(0, len(pron))
    return(pron[x])


def verb():
    verb = ["see ", "touch ", "steal ", "hug ", "drive "]
    x = randrange(0, len(verb))
    return(verb[x])


def noun():
    noun = ["coin", "pen", "car", "pc", "girl"]
    x = randrange(0, len(noun))
    return(noun[x])


for i in range(0, 11):
    print(pronoun() + "will " + verb() + "a " + noun())
