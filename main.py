def read_file_content(filename):
    file_content = open(filename,"r")
    data = file_content.read()
    return data


def count_words():
    text = read_file_content("./story.txt")
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts