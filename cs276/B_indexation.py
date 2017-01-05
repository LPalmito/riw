def indexation(useful_tokens):
    """stock the term_termID (dict), doc_docID (dict), termID_docID (dict) into 3 documents"""

    # Create the link between terms and their id, and doc and their id
    # TODO what is the best way to save the data? Just dictionnaries? How to adapt cacm code to cs276?
    # data_term = open('/Users/Gus/PycharmProjects/Ri-W/riw/cs276/data_term_termID', 'w')
    # term_termID = {}
    # for tokenID, token in enumerate(useful_tokens):
    #     term_termID[token] = tokenID
    #     set(tuple((a, b) for a in range(3)) for b in range(3))
        # str_tokenID = str(tokenID)
        # data_term.write(token + " : " + str_tokenID + "\n")
    # data_term.close()
