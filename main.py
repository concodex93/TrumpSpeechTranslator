# Donald Trump text translator
# Used to convert input into something President Trump would say ...
#

import re
from textblob import TextBlob

m_file = "speeches.txt"


# import file
def import_file(file):
    with open(file) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip().split("."))

        return lines


# extract nouns from file
def extract_nouns(file):
    noun_blob = TextBlob(file)
    list_of_nouns = noun_blob.noun_phrases
    return list_of_nouns


# stores nouns in list container
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


# add comma suffix
def adding_comma(_list):
    temp_list = []
    for word in _list:
        comma = (re.findall(r'\w+', word))
        temp_list.append(comma)
    return temp_list


# capitalizes words
def cap_word(_list):
    temp_list = []
    for sub_list in _list:
        for word in sub_list:
            temp_list.append(word.upper())
    return temp_list


# add key value pair of {word : number count}
def most_common(_list):
    _dict = {}
    for word in _list:
        common_blob = TextBlob(word)
        _dict.update({word: common_blob.word_counts[word]})
    return _dict


def main():
    # Extract nouns from file and output to user

    word_list = store_nouns_in_container(m_file)
    print("--------------------------")
    for word in word_list:
        print(word)
    comma_list = adding_comma(word_list)
    print("--------------------------")
    for word in comma_list:
        print(word)
    capitalize_list = cap_word(comma_list)
    print("--------------------------")
    for word in capitalize_list:
        print(word)
    _dict = most_common(capitalize_list)
    print("--------------------------")
    for key in _dict:
        print(key, _dict[key])

if __name__ == '__main__':
    main()
