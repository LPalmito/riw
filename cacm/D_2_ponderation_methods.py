import math


def tf_idf(termID, docID, termID_docID, N_docs):
    """Return the tf-idf"""
    tf, df, idf = 0, 0, 0
    df = len(termID_docID[termID])
    for dID in termID_docID[termID]:
        if dID == docID:
            tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    return tf*idf


def n_tf_idf(termID, docID, termID_docID, N_docs):
    """Return the normalized tf-idf"""
    tf, df, idf, n_tf = 0, 0, 0, 0
    df = len(termID_docID[termID])
    for dID in termID_docID[termID]:
        if dID == docID:
            tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    if tf != 0:
        n_tf = 1 + math.log(tf, 10)
    return n_tf*idf


def n_freq(termID, docID, termID_docID, docID_mtf):
    """Return the normalized frequency"""
    tf = 0
    max_tf = docID_mtf[docID]
    for dID in termID_docID[termID]:
        if dID == docID:
            tf += 1
    if max_tf == 0:
        return 0
    else:
        return tf/max_tf