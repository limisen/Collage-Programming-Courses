# ha
from random import randint
answers = ["Ask again later", "As I see it, yes", "Concentrate and ask again"]
answers += ["Better not tell you now", "Very doubtful"]
x = "Helllo world"

while x != "stop":
    x = input("Ask the magic 8-ball your question: ")
    x = x.lower()
    if x == "stop":
        break
    rng = randint(0, len(answers) - 1)

    print(f"The magic 8-ball says: {answers[rng]}")
