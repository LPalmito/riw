import time


def indexation(useful_tokens, docs):
    """Return the 4 used dicts: term_termID, docID_doc, termID_docID, docID_termID"""
    start = time.time()
    # Create the term_termID
    term_termID = {}
    for tokenID, token in enumerate(useful_tokens):
        term_termID[token] = tokenID
    # Create the docID_doc
    docID_doc = {}
    for docID, doc in enumerate(docs):
        docID_doc[docID] = doc['.T']+doc['.W']+doc['.K']
    # Create the termID_docID
    termID_docID = {}
    for docID, doc in docID_doc.items():
        for word in doc:
            if term_termID[word] not in termID_docID.keys():
                termID_docID[term_termID[word]] = [docID]
            else:
                termID_docID[term_termID[word]].append(docID)
    # Create the docID_termID
    docID_termID = {}
    for docID, doc in docID_doc.items():
        docID_termID[docID] = []
        for word in doc:
            if term_termID[word] not in docID_termID[docID]:
                docID_termID[docID].append(term_termID[word])
    end = time.time()
    duration = (end-start)*1000
    print("Indexation effectuée en", duration, "ms.")
    return term_termID, docID_doc, termID_docID, docID_termID
