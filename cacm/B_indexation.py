def indexation(useful_tokens, docs):
    """Return the term_termID (dict), doc_docID (list of tuples), termID_docID (list of tuples)"""
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
    print("Indexation effectuée.")
    return term_termID, doc_docID, termID_docID
