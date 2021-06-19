

string1 = 'Have you followed CodeWithJoxia On Instagram???'


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)

    return line


print (split_and_join(string1))


## OUTPUT => Have-you-followed-CodeWithJoxia-On-Instagram?????
