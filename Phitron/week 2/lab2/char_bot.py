greeting_words = ["hi", 'hello', "wassup", "hola", "hey"]
bye_words = ["bye", "tata", "adios"]
bad_words = ["dog", "mad", 'pocha', "chhagol"]


def listen():
    return input("\nSay something: ")


def decide(commad):
    broken_words = commad.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word.lower() in greeting_words:
            talk_back("Hi man\n")
            return
        elif word.lower() in bye_words:
            talk_back("Tata bye bye\n")
            return
        elif word.lower() in bad_words:
            talk_back("Behave yourself.\n")
            return


def talk_back(response):
    print(response)


while True:
    command = listen()
    decide(command)
# print(command)
