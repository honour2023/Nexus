


# Determine if a word or phrase is an isogram.
#
# An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.
#
# Examples of isograms:
#
# lumberjacks
# background
# downstream
#
# The word isograms, however, is not an isogram, because the s repeats
word = input("enter a word or phrase: ")

def count_(name):
    new_word = {}
    for letters in word:
        if letters in new_word.keys():
            new_word[letters] += 1

        else:
            new_word[letters] = 1
    return new_word

def is_isogram(d):
    for k in d.keys():
        if d[k] != 1:
            return False

        else: continue
    return True


if is_isogram(count_(word)):
    print("it is an isogram")

else:
    print ("it is not an Isogram")