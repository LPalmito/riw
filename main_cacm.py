import nltk
import math
import matplotlib.pyplot as plt
import pprint
import regex


def render_documents(tokens):
    """Return a list of docs created from the tokens (only for CACM)"""
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


def search_term_in_corpus(searched_term, term_termID, termID_docID):
    """Return the list of docIDs where the search term is"""
    if searched_term in term_termID:
        # Retrieve the corresponding termID
        searched_termID = term_termID[searched_term]
        # Retrieve the corresponding docIDs
        searched_docIDs = []
        for termID, docID in termID_docID:
            if termID == searched_termID:
                searched_docIDs.append(docID)
        return searched_docIDs
    else:
        # If the searched term is not in the corpus
        return []


def search_expression_in_corpus(searched_expression, term_termID, termID_docID, len_corpus):
    """Return ths list of docIDs where the searched expression is"""
    # Produce 'search_terms' as a list of list of tuples:
    # ex: A.B+C.-D <=> (A) AND (B OR C) AND (NOT D) <=> [ [(A,True)], [(B,True),(C,True)], [(D, False)] ]
    search_list = searched_expression.split('.')
    searched_terms = []
    for searched_term in search_list:
        tuple_list = []
        for s in searched_term.split('+'):
            if s[0] == '-':
                tuple_list.append((s[1:], False))
            else:
                tuple_list.append((s, True))
        searched_terms.append(tuple_list)
    # Save the sub results in 'result_list'
    result_list = []
    for or_list in searched_terms:
        res = []
        for term, b in or_list:
            r = search_term_in_corpus(term, term_termID, termID_docID)
            if b:
                res.extend(r)
            else:
                not_r = [x for x in range(len_corpus) if x not in r]
                res.extend(not_r)
        res = list(set(res))
        result_list.append(res)
    # Combine the results of 'result_list'
    result = result_list[0]
    for i, r in enumerate(result_list[0]):
        for sub_res in result_list[1:]:
            if r not in sub_res:
                del result[i]
    return result


def docIDs_to_docs(docIDs, doc_docID):
    """Return a list of docs corresponding to the docIDs given"""
    docs = []
    for doc, docID in doc_docID:
        if docID in docIDs:
            docs.append(doc)
    return docs

if __name__ == '__main__':

    # Open and read cacm.all
    cacm = open('./Resources/CACM/cacm.all')
    text = cacm.read()

    # Tokenize the text, render it in docs and filter it
    tokens = nltk.word_tokenize(text.upper())
    docs = render_documents(tokens)
    docs = filter_documents(docs)
    # TODO: Delete it, only for tests purposes
    docs = docs[:4]

    # Keep only the tokens in useful attributes
    useful_tokens = []
    for doc in docs:
        useful_tokens.extend(doc['.T'])
        useful_tokens.extend(doc['.W'])
        useful_tokens.extend(doc['.K'])

# 2.1 Traitements linguistiques

    # Question 1 :
    T = len(useful_tokens)
    print("Le nombre T de tokens dans .T, .W, .K est : ", T)

    # Question 2 :
    unique_useful_tokens = list(set(useful_tokens))
    M = len(unique_useful_tokens)
    print("La taille M du vocabulaire est :", M)

    # Question 3 :
    half_useful_tokens = useful_tokens[:int(len(useful_tokens)/2)]
    unique_half_useful_tokens = list(set(half_useful_tokens))
    T2 = len(half_useful_tokens)
    print("Le nombre T2 de tokens dans .T, .W, .K pour la moitié de la collection est : ", T2)
    M2 = len(unique_half_useful_tokens)
    print("La taille M2 du vocabulaire pour la moitié de la collection est :", M2)
    b = math.log(M/M2, 2)
    print("b = ", b)
    k = M/T**b
    print("k = ", k)

    # Question 4 :
    M_1M = math.floor(k*1000000**b)
    print("La taille M_1M du vocabulaire pour 1 million de tokens est : ", M_1M)

    # Find the frequencies of the words
    frequencies_list = nltk.FreqDist(useful_tokens).most_common()
    frequencies_list.sort(key=lambda t: t[1], reverse=True)

    # Fill the ranks and the frequencies lists
    ranks = []
    frequencies = []
    for rank, frequency in enumerate(frequencies_list):
        ranks.append(rank)
        frequencies.append(frequency[1])

    # Question 5 :
    plt.figure(1)
    plt.subplot(211)
    plt.title('f en fonction de r')
    plt.plot(ranks, frequencies)
    log_ranks = [math.log(rank+1) for rank in ranks]
    log_frequencies = [math.log(frequency) for frequency in frequencies]
    plt.subplot(212)
    plt.title('log(f) en fonction de log(r)')
    plt.plot(log_ranks, log_frequencies)
    plt.show()

# 2.2 Indexation

    # Create the link between terms and their id, and doc and their id
    term_termID = {}
    for tokenID, token in enumerate(useful_tokens):
        term_termID[token] = tokenID
    doc_docID = [(doc['.T']+doc['.W']+doc['.K'], docID) for docID, doc in enumerate(docs)]

    # Create the (termID, docID) tuples and sort them
    termID_docID = []
    for doc, docID in doc_docID:
        for word in doc:
            termID_docID.append((term_termID[word], docID))
    termID_docID.sort(key=lambda t_d: (t_d[0], t_d[1]))

# 2.2.1 Modèle de recherche booléen

    # For a single word as search
    searched_term = input("Entrez un mot à rechercher dans les documents : ").upper()
    searched_docIDs = search_term_in_corpus(searched_term, term_termID, termID_docID)
    searched_docs = docIDs_to_docs(searched_docIDs, doc_docID)
    print(searched_docs)

    # For a normal conjunctive expression
    searched_expression = input("Entrez une expression booléenne sous forme normale conjonctive comme dans l'exemple"
                              "\nex: 1.2+3.4 = (1) AND (2 OR 3) AND (4) : ").upper()
    searched_docIDs_2 = search_expression_in_corpus(searched_expression, term_termID, termID_docID, len(doc_docID))
    searched_docs_2 = docIDs_to_docs(searched_docIDs_2, doc_docID)
    print(searched_docs_2)

    # Close cacm.all
    cacm.close()
