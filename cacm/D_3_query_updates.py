def update_termID_docID(query, termID_docID, term_termID):
    """Update the termID_docID with the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_dID = termID_docID
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_dID[term_termID[q_token]].append(-1)
    return tID_dID


def update_docID_termID(query, docID_termID, term_termID):
    """Update the docID_termID with the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    dID_tID = docID_termID
    dID_tID[-1] = []
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            dID_tID[-1].append(term_termID[q_token])
    return dID_tID


def update_docID_mtf(docID_mtf, dID_tID, tID_dID):
    """Update the docID_termID with the query"""
    dID_mtf = docID_mtf
    dID_mtf[-1] = 0
    for t_ID in dID_tID[-1]:
        tfj = 0
        for dID in tID_dID[t_ID]:
            if dID == dID:
                tfj += 1
        if tfj > docID_mtf[dID]:
            docID_mtf[dID] = tfj
    return dID_mtf