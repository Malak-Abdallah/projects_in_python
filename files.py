# Write a function in python to count the number of lines from a text file "story.txt"
# which is not starting with an alphabet "T".

# Write a function in Python to read lines from a text file "notes.txt".
# Your function should find and display the occurrence of the word "the"

# If Aditi has stored the following content in the file WORDS.TXT:
# WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE
# The function JTOI() should display the following content:
# WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE

def JToI():
    file = open("words.txt","r+")
    data = file.read()
    file.write("\n")
    for letter in data:
        if letter == 'J':
            file.write("I")
        else:
            file.write(letter)

    file.close()


def occurrence():
    print("number of repeated word 'the' is printed in a 'result.txt' file ")
    f = open("notes.txt", "r")
    out = open("result.txt", "w")
    count = 0
    for x in f.readlines():
        for y in x.split():
            if y == "the":
                count += 1
    out.write("word 'the' repeated " + str(count) + " times in notes.txt")
    f.close()
    out.close()

if __name__ == '__main__':
    occurrence()
    JToI()
    lines = 0
    twords = 0
    f = open("story.txt", "r")
    for x in f.readlines():
        if x[0] != "T":
            lines += 1
            for w in x.split():
                twords += 1
        else:
            for w in x.split():
                twords += 1

    print("\nthere are " + str(lines) + " lines not starting with 'T' in this text file")
    print("number of words in this text file = " + str(twords))
    f.close()
