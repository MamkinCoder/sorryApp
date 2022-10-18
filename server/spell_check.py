# Code copyied from StackOverflow's answer
# https://stackoverflow.com/a/17706025/14363698

my_file = open("bad_words/en", "r")

data = my_file.read()

arrBad = data.split('\n')


def profanityFilter(text):
    brokenStr1 = text.split()
    badWordMask = '!@#$%!@#$%^~!@%^~@#$%!@#$%^~!'
    for word in brokenStr1:
        if word in arrBad:
            print(word + ' <--Bad word!')
            text = text.replace(word, badWordMask[:len(word)])
    return text


print(profanityFilter("this thing sucks sucks sucks fucking stuff"))
