import nltk
import regex
import pprint
import copy

def get_docs(text):
    """Return a list of the useful tokens"""
    # Tokenize the text, render it in docs and filter it
    docs = list(render_documents(text))
    docs_backup = copy.deepcopy(docs)
    docs = filter_documents(docs)
    # TODO: Delete it, only for tests purposes
    docs = docs[:49]
    return docs, docs_backup


def get_useful_tokens(docs):
    """Return a list of the useful tokens"""
    useful_tokens = []
    for doc in docs:
        # TODO: Query 2 concerns Authors, what about adding them here?
        useful_tokens.extend(doc['.T'])
        useful_tokens.extend(doc['.W'])
        useful_tokens.extend(doc['.K'])
    return useful_tokens


def render_documents(text):
    """Return a list of docs created from the tokens"""
    # Initialisations
    tokens = nltk.word_tokenize(text)
    markers = ['.I', '.T', '.W', '.B', '.A', '.N', '.X', '.K']
    current_marker, current_doc = '.I', {}
    result = []
    # docs_backup = []
    # Prepare the result
    for token in tokens:
        # For each new .I, prepare a new doc and fill it
        if token == '.I':
            if current_doc != {}:
                result.append(current_doc)
                # docs_backup.append(current_doc)
            current_doc = {}
            for marker in markers:
                current_doc[marker] = []
        # For each other marker, update the current marker
        elif token in markers:
            current_marker = token
        # Else, fill the corresponding attribute
        else:
            current_doc[current_marker].append(token)
    result.append(current_doc)
    # docs_backup.append((current_doc))
    return result


def filter_documents(docs):
    """Filter the docs by keeping only words and deleting all the stopwords"""
    # Prepare the stop word set
    common_words = open('./Resources/CACM/common_words')
    common_text = common_words.read()
    common_tokens = nltk.word_tokenize(common_text)
    stop_word_list = nltk.corpus.stopwords.words('english')
    stop_word_list.extend(common_tokens)
    stop_word_list = [word.upper() for word in stop_word_list]
    stop_word_set = set(stop_word_list)
    common_words.close()
    # Filter every token
    for doc in docs:
        for k, texts in doc.items():
            filtered_doc = []
            for text in texts:
                match = regex.match('[A-Z]+', text.upper())
                if match is not None and match.group() not in stop_word_set:
                    filtered_doc.append(match.group())
            doc[k] = filtered_doc
    return docs
