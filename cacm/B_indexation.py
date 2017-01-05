import time


def indexation(useful_tokens, docs):
    """Return the term_termID (dict), doc_docID (list of tuples), termID_docID (dict)"""
    start = time.time()
    # Create the link between terms and their id, and doc and their id
    term_termID = {}
    for tokenID, token in enumerate(useful_tokens):
        term_termID[token] = tokenID
    # TODO: Why not use a dict for doc_docID?
    doc_docID = [(doc['.T']+doc['.W']+doc['.K'], docID) for docID, doc in enumerate(docs)]
    # Create the (termID, docID) tuples and sort them
    termID_docID = {}
    for doc, docID in doc_docID:
        for word in doc:
            if term_termID[word] not in termID_docID.keys():
                termID_docID[term_termID[word]] = [docID]
            else:
                termID_docID[term_termID[word]].append(docID)
    end = time.time()
    duration = (end-start)*1000
    print("Indexation effectuée en", duration, "ms.")
    return term_termID, doc_docID, termID_docID
