from cacm.D_1_vectorial_main import *


def vectorial_search_front(query, term_termID, docID_doc, termID_docID, docID_termID, m):
    # Initialisations
    docID_cos_sim = []

    docID_mtf = get_docID_mtf_front(docID_doc, docID_termID, termID_docID, m)

    # Compute the query-related cosinus
    tID_dID = update_termID_docID_front(query, termID_docID, term_termID)
    dID_tID = update_docID_termID(query, docID_termID, term_termID)
    dID_mtf = update_docID_mtf_front(docID_mtf, dID_tID, tID_dID)
    w_query, s_query = get_w_query_front(tID_dID, len(docID_doc), len(term_termID))

    # Compute the corpus-related cosinus
    for dID in range(len(docID_doc)):
        docID_cos_sim.append(
            (dID, cos_sim_front(dID, termID_docID, docID_termID, len(docID_doc), w_query, s_query)))
    docID_cos_sim.sort(key=lambda dID_cos: dID_cos[1], reverse=True)

    return docID_cos_sim


def update_termID_docID_front(query, termID_docID, term_termID):
    """Update the termID_docID with the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_dID = termID_docID
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_dID[str(term_termID[q_token])].append(-1)
    return tID_dID


# def update_docID_termID(query, docID_termID, term_termID):
#     """Update the docID_termID with the query"""
#     q_tokens = list(set([x.upper() for x in query.split()]))
#     dID_tID = docID_termID
#     dID_tID[-1] = []
#     for q_token in q_tokens:
#         if q_token in term_termID.keys():
#             dID_tID[-1].append(term_termID[q_token])
#     return dID_tID
#
#
def update_docID_mtf_front(docID_mtf, dID_tID, tID_dID):
    """Update the docID_termID with the query"""
    dID_mtf = docID_mtf
    dID_mtf[-1] = 0
    for t_ID in dID_tID[-1]:
        tfj = 0
        for dID in tID_dID[str(t_ID)]:
            if dID == dID:
                tfj += 1
        if tfj > docID_mtf[dID]:
            docID_mtf[dID] = tfj
    return dID_mtf


def tf_idf_front(termID, docID, termID_docID, N_docs):
    """Return the tf-idf"""
    tf, df, idf = 0, 0, 0
    df = len(termID_docID[str(termID)])
    for dID in termID_docID[str(termID)]:
        if dID == docID:
            tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    return tf*idf


def get_w_query_front(tID_dID, N_docs, N_terms):
    """Return the weight and the squared norm of the query"""
    w_query, s_query = [], 0
    for t_ID in range(N_terms):
        w_query.append(tf_idf_front(t_ID, -1, tID_dID, N_docs))
        s_query += w_query[t_ID] ** 2
    return w_query, s_query


def cos_sim_front(docID, termID_docID, docID_termID, N_docs, w_query, s_query):
    """Return the cos similarity"""
    # Create the vectors for the query and the doc according to the chosen method
    num, s_doc = 0, 0
    # 1 <=> tf_idf | 2 <=> n_tf_idf | 3 <=> n_freq
    for t_ID in docID_termID[str(docID)]:
        w_doc_tID = tf_idf_front(t_ID, docID, termID_docID, N_docs)
        num += w_query[t_ID]*w_doc_tID
        s_doc += w_doc_tID**2
    if s_doc == 0 or s_query == 0:
        return 0
    else:
        return num/(s_doc**0.5*s_query**0.5)


def get_docID_mtf_front(docID_doc, docID_termID, termID_docID, m):
    """Compute max_tf for dID"""
    docID_mtf = {}
    for docID in range(len(docID_doc)):
        docID_mtf[docID] = 0
        for t_ID in docID_termID[str(docID)]:
            tfj = 0
            for dID in termID_docID[str(t_ID)]:
                if dID == docID:
                    tfj += 1
            if tfj > docID_mtf[docID]:
                docID_mtf[docID] = tfj
    return docID_mtf
