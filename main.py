# Donald Trump text translator
# Used to convert input into something President Trump would say ...
#

import re
from textblob import TextBlob

m_file = "speeches.txt"


def import_file(file):
    with open(file) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip().split("."))

        return lines


def extract_nouns(file):
    noun_blob = TextBlob(file)
    list_of_nouns = noun_blob.noun_phrases
    return list_of_nouns


def most_common(file, word):
    common_blob = TextBlob(file)
    return common_blob.word_counts[word]


def store_nouns_in_container(_file):
    temp_list_of_nouns = []
    noun_container = []
    file = import_file(_file)

    for _list in file:
        for line in _list:
            nouns = extract_nouns(line)
            temp_list_of_nouns.append(nouns)

    for line in temp_list_of_nouns:
        for word in line:
            noun_container.append(word)

    return noun_container


def adding_comma(_list):
    temp_list = []
    for word in _list:
        temp_list.append(re.findall(r'\w+', word))
    return temp_list


def main():
    # Extract nouns from file and output to user

    word_list = store_nouns_in_container(m_file)
    comma_list = adding_comma(word_list)

    for word in comma_list:
        print(word)


if __name__ == '__main__':
    main()
