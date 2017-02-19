import os
import nltk
import regex


def get_words_from_file(path, fname):
    """Get all words from an input file"""
    file = open(path + '/' + fname)
    text = file.read()
    text.lower()
    file.close()
    return text


def get_cs276_tokens():
    """Put all words of the files in one list"""

    # Get folders to analyse
    # TODO indicate right path here
    master_path = '/Users/Gus/PycharmProjects/Ri-W/riw/Resources/CS276/pa1-data'
    folders = ([folder for folder in os.listdir(master_path)])

    # Get all words of the files in one unique string
    all_words = ''
    # TODO: expand the function to all folders
    for folder in folders[0]:
        files = os.listdir(os.path.join(master_path, folder))
        path = os.path.join(master_path, folder)
        for file in files:
            words = get_words_from_file(path, file)
            all_words += words

    # Split the unique string into a list of words
    tokens = all_words.split()
    # Filter the list
    useful_tokens = filter_documents(tokens)

    return useful_tokens


def filter_documents(tokens):
    """Filter the docs by keeping only words and deleting all the stopwords"""
    stop_word_list = nltk.corpus.stopwords.words('english')
    stop_word_list = [word.lower() for word in stop_word_list]
    stop_word_set = set(stop_word_list)
    useful_tokens = []
    for token in tokens:
        match = regex.match('[a-z]+', token)
        if match is not None and match.group() not in stop_word_set:
            useful_tokens.append(token)

    return useful_tokens
