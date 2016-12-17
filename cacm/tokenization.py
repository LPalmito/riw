import nltk
import regex


def prepare_cacm(text):
    """Return a list of the useful tokens"""
    # Tokenize the text, render it in docs and filter it
    tokens = nltk.word_tokenize(text.upper())
    docs = render_documents(tokens)
    docs = filter_documents(docs)
    # TODO: Delete it, only for tests purposes
    # docs = docs[:4]
    # Keep only the tokens in useful attributes
    useful_tokens = []
    for doc in docs:
        useful_tokens.extend(doc['.T'])
        useful_tokens.extend(doc['.W'])
        useful_tokens.extend(doc['.K'])
    return useful_tokens, docs


def render_documents(tokens):
    """Return a list of docs created from the tokens"""
    # Initialisations
    markers = ['.I', '.T', '.W', '.B', '.A', '.N', '.X', '.K']
    current_marker = '.I'
    current_doc = {}
    result = []
    # Prepare the result
    for token in tokens:
        # For each new .I, prepare a new doc and fill it
        if token == '.I':
            if current_doc != {}:
                result.append(current_doc)
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
    return result


def filter_documents(docs):
    """Filter the docs by keeping only words and deleting all the stopwords"""
    stop_word_list = nltk.corpus.stopwords.words('english')
    stop_word_list = [word.upper() for word in stop_word_list]
    stop_word_set = set(stop_word_list)
    for doc in docs:
        for k, texts in doc.items():
            filtered_doc = []
            for text in texts:
                match = regex.match('[A-Z]+', text)
                if match is not None and match.group() not in stop_word_set:
                    filtered_doc.append(match.group())
            doc[k] = filtered_doc
    return docs
