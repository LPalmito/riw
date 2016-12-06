import os
import nltk
import regex

master_path = './Resources/CS276/pa1-data'

folders = ([folder for folder in os.listdir(master_path)])

# Get all words from an input file
def get_words_from_file(fname):
    file = open(path + '/' + fname)
    text = file.read()
    text.lower()
    file.close()
    return text


# Put all words of the files in one unique string
all_words = ''
loop = 0
for folder in folders:
    files = os.listdir(os.path.join(master_path,folder))
    path = os.path.join(master_path, folder)
    for file in files:
        words = get_words_from_file(file)
        all_words += words

# Split the unique string into a list of words
tokens = all_words.split()

# Delete duplicates
tokens = list(set(tokens))

stop_word_list = nltk.corpus.stopwords.words('english')
stop_word_list = [word.lower() for word in stop_word_list]
stop_word_set = set(stop_word_list)

print(len(stop_word_list))

# for token in tokens:
#     match = regex.match('[A-Z]+', token)
#     if token in stop_word_list or match is None or match.group() in stop_word_set:
#         tokens.remove(token)


print(len(tokens))
